'''
author : himanshu rawat 
date : 22-05-22
'''
#imports
import json
import pandas as pd
from helper import *


# this is initial function that be entry point for cloud function .
def get_data(request):
   #you can also secure here by passing header keys 
   if request.headers.get("content-type"):
      print('getting data ....')
      data =request.json

      #get data and extract pull reuest
      #as seen in json extract action and number are outside pull request data

      dd= data['pull_request']
      dd['action']=data['action']
      dd['number']=data['number']
      
      #create df and upload to dataset
      df=pd.dataFrame([dd], columns=schema_pr)
      df['updated_at'] = pd.to_datetime(df['updated_at'])
      load_data(df , project_id, datasetid, tableid,"WRITE_APPEND")

      #repeat abive steps for user data 
      user= data['pull_request']['user']
      user['action']=data['action']
      user['number']=data['number']
      user['pull_id']=data['pull_request']['id']
      df_user=pd.dataFrame([user], columns=schema_user)
      df_user['raised_at']=df['updated_at']
      df_user['site_admin']=df_user['site_admin'].astype(str)
      load_data(df_user , project_id, datasetid, tableid_users,"WRITE_APPEND")
   else:
      #ideally you should send notification , but this is what you will get in 1 day .
      print('no data found')
      exit(0)
