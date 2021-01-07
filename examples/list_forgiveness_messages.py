from PPPForgivenessSDK.client import Client

# to run file 'list_forgiveness_messages.py', use valid token (page parameter can be changed )
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

message_api = client.messages

# list first page of document types  an SBA Number and/or a true or false for is_complete can be added
result = message_api.list(page=1) # get a paginated list of forgiveness requests

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
