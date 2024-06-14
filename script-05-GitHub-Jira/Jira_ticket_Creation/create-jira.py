# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nehaavasekar.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0SVo_4xj3MOO7Yp_ns0-zA9gFU2aTZ6URQUl6VEmksffSDeClWneApNIyjPkz_Hke_FmZbIRdYep2VlhVFN-H7H6ZKH2ts6Z1xZEl_sTTQSDn4athicwlMzLj4QDwnzTvLHtr7VNkVC_onYays0_CEF-t-n0BrmJoAM5ECf5uDoU=4414EF25"

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {

    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "10001"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))