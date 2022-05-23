''' Author : Himanshu
    Date : 2022-05-22
'''

#imports
import requests
from config import *
from helper import *
import json

#generate url this is imported from configs
url = "https://api.github.com/"+repo_owner+"/"+repo_name+"/pulls?state=all"

#entry point for cloud function
def get_data(request,context):
	payload={}
	headers = {
  	'Accept': 'application/vnd.github.v3+json',
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	data = json.loads(response.text)
	df = pd.DataFrame(data)

	load_data(df_user , project_id, datasetid, tableid_batch,"WRITE_TRUNCATE" )

