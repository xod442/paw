import requests
import json

app_id = 'wendys'
app_secret = 'test'

headers = {"Content-Type":"application/json"}
payload = {"app_id":app_id,"app_secret":app_secret}

# Convert to json
payload=json.dumps(payload)

# URL for requesting token
tok_url = 'http://localhost:8088/apps/access_token/'

r = requests.post(tok_url, headers=headers, data=payload)

r = json.loads(r.text)

token = r['token']
print('-------------------------------------------------------------------')
print(r)
