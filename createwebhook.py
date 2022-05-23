import requests
import json
import sys
from config import *
import sys
payload_url = str(sys.argv[1])
token = str(sys.argv[2])

url = "https://api.github.com/repos/"+repo_owner+"/"+repo_name+"/hooks"

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

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
