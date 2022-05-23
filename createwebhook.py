'''
Author : Himanshu
Date : 2022-05-22
'''
#imports
import requests
import json
import sys
from config import *
import sys

#Takes two argument first payload url to which data is delivered and token with right permission.
payload_url = str(sys.argv[1])
token = str(sys.argv[2])

#url of repo is generated using configs variables .
url = "https://api.github.com/repos/"+repo_owner+"/"+repo_name+"/hooks"

#generate payload
payload = json.dumps({
  "name": "web",
  "active": True,
  "events": [
    "pull_request"
  ],
  "config": {
    "url": payload_url,
    "content_type": "json",
    "insecure_ssl": "0"
  }
})
headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': 'Bearer '+token,
  'Content-Type': 'application/json',
}

#Api call ideally handle it using report.code with 200.
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
