# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nehaavasekar.atlassian.net/rest/api/3/project"

API_TOKEN = "<api-token>"

auth = HTTPBasicAuth("email@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

for project in output:
    name = project["name"]
    print(name)