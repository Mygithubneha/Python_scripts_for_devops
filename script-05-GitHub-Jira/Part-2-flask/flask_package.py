from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

#creating a flask application instance
app = Flask(__name__)

#Creating decorators
@app.route("/createJIRA", methods=['POST'])
def createJIRA():


    url = "https://nehaavasekar.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0SVo_4xj3MOO7Yp_ns0-zA9gFU2aTZ6URQUl6VEmksffSDeClWneApNIyjPkz_Hke_FmZbIRdYep2VlhVFN-H7H6ZKH2ts6Z1xZEl_sTTQSDn4athicwlMzLj4QDwnzTvLHtr7VNkVC_onYays0_CEF-t-n0BrmJoAM5ECf5uDoU=4414EF25"

    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "AB"
        },
        "issuetype": {
        "id": "10006"
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.', port=5000)