from PPPForgivenessSDK.client import Client

# to run file 'list_forgiveness_requests.py', use valid token (page parameter can be changed )
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

forgiveness_api = client.forgiveness_requests

# list first page of document types
result = forgiveness_api.list(page=1) # get a paginated list of forgiveness requests

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
