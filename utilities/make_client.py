import requests
import json

def client(app_id,app_secret):

    # URL to create an organization
    org_url = 'http://localhost:8088/apps/'

    headers = {"Content-Type":"application/json"}
    payload = {"app_id":app_id,"app_secret":app_secret}

    # Convert to json
    payload=json.dumps(payload)

    r = requests.post(org_url, headers=headers, data=payload)

    return r.status_code
