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

    API_TOKEN = ""

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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)