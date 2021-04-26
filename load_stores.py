import requests
import json
from utilities.get_token import token

app_id = 'sample'
app_secret = 'test'
hostip = '10.132.0.18'

headers = {"Content-Type":"application/json"}
payload = {"app_id":app_id,"app_secret":app_secret}

# Convert to json
payload=json.dumps(payload)

r = token(app_id,app_secret,hostip)

print(r)

token = r[0]

# Load db
count = 0
cr = '\n'
# Get number of lines from file
num_lines = sum(1 for line in open("stores1.csv"))

fi = open("stores1.csv", 'r')

# print (num_lines)
line = fi.readline()
count = count + 1
line=line.strip("\n")

while count <= num_lines:
    print(count)

    # print ('..............read line')


    element = line.split(",")
    # print ('this is the regular element %s' % (element))

    name = element[0]
    street_address = element[1]
    city = element[2]
    state = element[3]
    zip = element[4]
    phone = element[5]
    neighborhood = element[6]
    store_id = element[7]

    out = [name,street_address,city,state,zip,phone,neighborhood,store_id]
    print(out)



    # Create new store
    store = {
      "neighborhood":element[6],
      "name":element[0],
      "street_address":element[1],
      "city":element[2],
      "state":element[3],
      "zip":element[4],
      "phone":element[5],
      "store_id":element[7]
    }


    # Convert to json
    store=json.dumps(store)
    print(store)

    # Now get the list of stores
    store_url ='http://'+hostip+':8088/stores/'
    headers = {"X-APP-ID":app_id,"X-APP-TOKEN":token,"Content-Type":"application/json"}

    print('--------------------posting store---------------------')
    try:
        r = requests.post(store_url, headers=headers, data=store)
        print(r)
    except:
        print('blow')
    line = fi.readline()
    count = count + 1
    line=line.strip("\n")


# print('--------------------printing all stores---------------------')
# r = requests.get(store_url, headers=headers)
# r = json.loads(r.text)
# print(r.text)
