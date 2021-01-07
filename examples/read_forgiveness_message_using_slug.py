from PPPForgivenessSDK.client import Client

# to run file 'read_forgiveness_message.py', use valid token and slug associated with a valid thread
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

message_api = client.messages

# read info for single forgiveness request
result = message_api.get(slug='{{SLUG HERE}}') # get a single forgiveness message

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
