from utilities.get_token import token

app_id = 'sample'
app_secret = 'test'
hostip = '10.132.0.18'

token = token(app_id,app_secret,hostip)

print(token)
print(type(token))


if token[1] == 200:
    print('You are logged in')
    print(token[0])
else:
    print(token[0])
# print(token['error']['code'])
#print(token[1])
#print(type(token[1]))
#print(type(token))
