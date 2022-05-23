'''
Author : Himanshu
Date : 2022-05-22
'''

#import
import json
from google.cloud import bigquery
import pandas
from google.oauth2 import service_account
from config import *

#Load credentials , this is picked from KEY_path variable , you dont have to change as it is copied from local while you deploy .
credentials = service_account.Credentials.from_service_account_file(key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
client = bigquery.Client(credentials=credentials, project=project_id,)


#function to load data from dataframe to bigquery
def load_data(df , project_id, datasetid, tableid,disposition ):

    job_config = bigquery.LoadJobConfig(
        write_disposition=disposition,
    )

    tid = project_id+'.'+datasetid+'.'+tableid
    job = client.load_table_from_dataframe(
        df, tid, job_config=job_config
    )  # Make an API request.
    job.result()

