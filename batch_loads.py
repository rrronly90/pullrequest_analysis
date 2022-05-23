''' Author : Himanshu
    Date : 2022-05-22
'''
#imports
import requests
from config import *
from helper import *
import json
import pandas as pd

def get_data(request,context):
    #set up git url end point
    url = "https://api.github.com/repos/rrronly90/casestudy1/pulls?state=all"
    print(url)
    payload={}
    #headers as recommended by api doc
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    #get response
    response = requests.request("GET", url, headers=headers, data=payload)
    #define empty list
    df_list = []
    data = json.loads(response.text)
    #iterate rows one by one . 
    for d in data:
        temp_df=pd.DataFrame([d] )
        df_list.append(temp_df)
    #create final dataset 
    df = pd.concat(df_list)
    load_data(df , project_id, datasetid, tableid_batch,"WRITE_TRUNCATE" )


