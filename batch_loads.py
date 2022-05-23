import requests
from config import *
from helper import *
import json

url = "https://api.github.com/"+repo_owner+"/"+repo_name+"/pulls?state=all"

payload={}
headers = {
  'Accept': 'application/vnd.github.v3+json',
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)
df = pd.DataFrame(data)

load_data(df_user , project_id, datasetid, tableid_batch,"WRITE_TRUNCATE" )

