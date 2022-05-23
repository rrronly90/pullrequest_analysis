import json
import pandas as pd
from helper import *

def get_data(request):
   if request.headers.get("content-type"):
      print('getting data ....')
      dAta =request.json
      print(type(dAta))
      dD= dAta['pull_request']
      dD['action']=dAta['action']
      dD['number']=dAta['number']
      dF=pd.DataFrame([dD], columns=schema_pr)
      dF['updated_at'] = pd.to_datetime(dF['updated_at'])
      load_data(dF , project_id, datasetid, tableid,"WRITE_APPEND")
      
      uSer= dAta['pull_request']['user']
      uSer['action']=dAta['action']
      uSer['number']=dAta['number']
      uSer['pull_id']=dAta['pull_request']['id']
      dF_user=pd.DataFrame([uSer], columns=schema_user)
      dF_user['raised_at']=dF['updated_at']
      dF_user['site_admin']=dF_user['site_admin'].astype(str)
      load_data(dF_user , project_id, datasetid, tableid_users,"WRITE_APPEND")
   else:
      print('no data found')
      exit(0)
