from utilities.get_token import token
import json
import requests

app_id='sample'
app_secret='test'
hostip='10.132.0.18'

get_token = token(app_id,app_secret,hostip)
token = get_token[0]

# headers
headers = {"Content-Type":"application/json", "X-APP-ID":app_id, "X-APP-TOKEN":token}

# URL for requesting token
# store_url = 'http://10.132.0.18:8088/stores/'
store_url = 'http://'+hostip+':8088/stores/'

# Make request
stores = requests.get(store_url, headers=headers)

print(stores.text)
print(type(stores))
