import json
import pandas as pd
from helper import *

def get_data(request):
   if request.headers.get("content-type"):
      print('getting data ....')
      data =request.json
      print(type(data))
      dd= data['pull_request']
      dd['action']=data['action']
      dd['number']=data['number']
      df=pd.dataFrame([dd], columns=schema_pr)
      df['updated_at'] = pd.to_datetime(df['updated_at'])
      load_data(df , project_id, datasetid, tableid,"WRITE_APPEND")

      user= data['pull_request']['user']
      user['action']=data['action']
      user['number']=data['number']
      user['pull_id']=data['pull_request']['id']
      df_user=pd.dataFrame([user], columns=schema_user)
      df_user['raised_at']=df['updated_at']
      df_user['site_admin']=df_user['site_admin'].astype(str)
      load_data(df_user , project_id, datasetid, tableid_users,"WRITE_APPEND")
   else:
      print('no data found')
      exit(0)
