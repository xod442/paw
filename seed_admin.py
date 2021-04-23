from utilities.make_client import client

app_id = 'sample'
app_secret = 'test'

r = client(app_id,app_secret)

print(r)
