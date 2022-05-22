from helper import *
import pandas as pd
import json


def get_data(request):
    if request.headers.get("content-type"):  # calling json objects
        print('getting data ....')
        data =json.dumps(request.json)
    else:
        print('no data found')
        exit(0)
    d= data['pull_request']
    d['action']=data['action']
    d['number']=data['number']

    df=pd.DataFrame([d], columns=schema_pr)
    df['updated_at'] = pd.to_datetime(df['updated_at'])
    load_data(df , project_id, datasetid, tableid, )