''' Author : Himanshu
    Date : 2022-05-22
'''

#imports
import requests
from config import *
from helper import *
import json
import pandas as pd

#generate url this is imported from configs

#entry point for cloud function
def get_data(request,context):
	url = "https://api.github.com/repos/"+repo_owner+"/"+repo_name+"/pulls?state=all"
	print(url)

	payload={}
	headers = {
  	'Accept': 'application/vnd.github.v3+json',
	}

	response = requests.request("GET", url, headers=headers, data=payload)
	
	data = json.loads(response.text)
	df = pd.DataFrame([data])
	print(df.head(5))

	load_data(df , project_id, datasetid, tableid_batch,"WRITE_TRUNCATE" )


