import os
import time
from datetime import datetime, timedelta
import requests
import pandas as pd
import numpy as np
from pymongo import MongoClient
import boto3
import sys
import json
import traceback
import json


class NorthbeamService:
    def __init__(self, NORTHBEAM_API_KEY, NORTHBEAM_DATA_CLIENT_ID, COLLECTION_NAME, DBNAME, MONGO_CONNECTION_URL):

        self.northbeam_api_key = NORTHBEAM_API_KEY
        self.nortbeam_data_client_id = NORTHBEAM_DATA_CLIENT_ID
        self.collection_name = COLLECTION_NAME
        self.dbname = DBNAME
        self.mongo_connection_url = MONGO_CONNECTION_URL

        self.lambda_client = boto3.client('lambda', region_name='us-east-1') # invoke the function in us-east-1

    def notify_on_slack(self, status, message, error="", stackTrace="",client=""):
        payload = json.dumps({
            'message': message,
            'status': status,
            'errorLogs': error,
            'stackTrace': stackTrace,
            'client':client
        })
        # trigger the lambda function to send a slack notification about the status of the glue job
        response = self.lambda_client.invoke(
            FunctionName='trigger-slack-notification', 
            InvocationType='RequestResponse',      # Synchronous invocation
            Payload=payload
        )
        return response['Payload'].read()   # returns the output of the lambda FunctionName

    def get_export_status(self, export_id, max_retries=5, delay=10): 
        url = f"https://api.northbeam.io/v1/exports/data-export/result/{export_id}"
        headers = {
            "accept": "application/json",
            "Authorization": self.northbeam_api_key,
            "Data-Client-ID": self.nortbeam_data_client_id
        }
        for attempt in range(max_retries):
            export_response = requests.get(url, headers=headers)
            export_result = export_response.json()
            export_status = export_result.get('status')

            if export_status == 'SUCCESS':
                result_url = export_result.get('result')[0]
                return result_url
            elif export_status != 'PENDING':
                raise Exception(f"Export status is not 'success': {export_status}")
            if attempt < max_retries - 1:
                time.sleep(delay)
        raise Exception("Max retries exceeded, export status not 'success'")

    def upload_file_to_s3(self, bucket_name, folder_name,file_name, file_path):
        s3_client = boto3.client(
            's3',
            region_name='ap-south-1'
        )
        s3_key = f"{folder_name}/{file_name}"
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f'File uploaded to s3://{bucket_name}/{s3_key}')
    
    def transfer_to_mongodb(self, csv_file_path, mongodb_connection_string, dbname, collection_name):
        # Print MongoDB connection string and database name for CloudWatch logs
        # print(f"MongoDB Connection String: {mongodb_connection_string}")
        # print(f"Database Name: {dbname}")
        client = MongoClient(mongodb_connection_string)
        db = client[dbname]
        collection = db[collection_name]
        collection.drop() # getting rid of the collection
        collection = db[collection_name]
        df = pd.read_csv(csv_file_path, parse_dates= ['date'])
        df.replace({np.nan: None}, inplace=True)
        print(df['date'].head(10))
        print(df.dtypes)
        df['date'] = pd.to_datetime(df['date']).dt.tz_localize('US/Central').dt.tz_convert('UTC') # will likely have to change this since data might be in GMT time zone
        data = df.to_dict(orient='records')
        collection.insert_many(data)
        client.close()
    
    def northbeam_data_pipeline(self):
        try:
            # Northbeam API call for export
            url = "https://api.northbeam.io/v1/exports/breakdowns"
            headers = {
                "accept": "application/json",
                "Authorization": self.northbeam_api_key,
                "Data-Client-ID": self.nortbeam_data_client_id
            }
            response = requests.get(url, headers=headers)
            breakdown_result = response.json()
            filtered_break_downs = [breakdown for breakdown in breakdown_result.get('breakdowns') if breakdown.get('key') == 'Platform (Northbeam)']
    
            print("breakdown>>", filtered_break_downs)

            today = datetime.utcnow()
            two_years_ago = today - timedelta(days=2*365)
            four_years_ago = today - timedelta(days=4*365)

            gmt_start_time = two_years_ago - timedelta(hours=1)
            gmt_end_time = today - timedelta(hours=1)
    
            start_time = gmt_start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
            end_time = gmt_end_time.strftime('%Y-%m-%dT%H:%M:%SZ')

            payload = {
                "level": "platform",
                "time_granularity": "DAILY",
                # "period_type": "YESTERDAY",
                "period_type": "FIXED",
                "period_options": {
                    "period_starting_at": start_time,
                    "period_ending_at": end_time
                },
                "breakdowns": filtered_break_downs,
                "options": {
                    "export_aggregation": "DATE",
                    "remove_zero_spend": False,
                    "aggregate_data": True
                },
                "attribution_options": {
                    "attribution_models": ["northbeam_custom__va", "northbeam_custom", "last_touch","last_touch_non_direct","first_touch","linear"],
                    "accounting_modes": ["accrual", "cash"],
                    "attribution_windows": ["1", "3","7","14","30","60","90"],
                },
                "metrics": [
                    {"id": "spend"},
                    {"id": "cac"},
                    {"id": "cacFt"},
                    {"id": "cacRtn"},
                    {"id": "ctr"},
                    {"id": "ecr"},
                    {"id": "revAttributed"},
                    {"id": "revAttributedFt"},
                    {"id": "revAttributedRtn"},
                    {"id": "roas"},
                    {"id": "roasFt"},
                    {"id": "roasRtn"},
                    {"id": "txns"},
                    {"id": "txnsFt"},
                    {"id": "txnsRtn"},
                    {"id": "visits"},
                    {"id": "newVisits"},
                    {"id": "newVisitsPercentage"},
                    {"id": "meta3SVideoViews7DClick"},
                    {"id": "meta3SVideoViews7DClick1DView"},
                    {"id": "meta3SVideoViewsDefault"},
                    {"id": "impressions"},
                ]
            }
            response = requests.post("https://api.northbeam.io/v1/exports/data-export", json=payload, headers=headers)
            result = response.json()
            print("result>>>", result)
            export_id = result.get('id')
            print("export_id>>>", export_id)
    
            url = self.get_export_status(export_id)
            print("url>>>", url)
            if url:
                yesterday = datetime.now() - timedelta(1)
                # file_name = f"data_{yesterday.year}_{yesterday.month}_{yesterday.day}.csv"
                file_name = f"data_historical.csv"
        
                response = requests.get(url)

                file_path = f"/tmp/{file_name}"  # Use /tmp for Glue job compatibility
                with open(file_path, 'wb') as f:
                    f.write(response.content)
        
                s3_bucket_name = "shoplc-processed-datalake"
                folder_name = "tjc-northbeam-data"
                self.upload_file_to_s3(s3_bucket_name, folder_name,file_name, file_path)
        
                # Write as parquet file so it can be transferred to Athena as well
                parquet_file_path = "/tmp/data_historical.parquet"  
                with open(parquet_file_path, 'wb') as f:
                    f.write(response.content)
                self.upload_file_to_s3("tjc-processed-data", "processed-files/northeam_data_v2", "northeam_data_v2.parquet", parquet_file_path)
    
                self.transfer_to_mongodb(file_path, self.mongo_connection_url, self.dbname, self.collection_name)
                print("Data transferred to MongoDB successfully")
            else:
                print("No file URL found in the export result.")
        
            message = f"Glue job 'banavo_tjc_northbeam_data_pipeline' was successful!"
            status = 'SUCCESS'
            client="TJC"
            output = self.notify_on_slack(message=message, status=status,client=client)
            print(output)
        except Exception as e:
            message = 'banavo_tjc_northbeam_data_pipeline'
            status = 'FAILURE'
            error = str(e)
            stackTrace = traceback.format_exc()
            client="TJC"
    
            # print(status, message, error, stackTrace)
    
            output = self.notify_on_slack(message=message, status=status, error=error, stackTrace=stackTrace,client=client)
            print(output)
            raise Exception(f"banavo_tjc_northbeam_data_pipeline - job failed. {e}")