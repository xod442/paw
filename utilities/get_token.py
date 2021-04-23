import requests
import json

def token(app_id,app_secret,hostip):
    # headers
    headers = {"Content-Type":"application/json"}
    payload = {"app_id":app_id,"app_secret":app_secret}

    # Convert to json
    payload=json.dumps(payload)

    # URL for requesting token
    tok_url = 'http://'+hostip+':8088/apps/access_token/'

    # Make request
    r = requests.post(tok_url, headers=headers, data=payload)

    # Check the response
    search_key = 'expires'
    if search_key in r.text:
        # Get status code
        code = r.status_code

        # Get token
        r = json.loads(r.text)
        token = r['token']
        # return token and code
        return token, code
    else:
        token = 'login failure'
        code = '666'
        return token, code
