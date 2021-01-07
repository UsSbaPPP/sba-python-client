from PPPForgivenessSDK.client import Client

# to run file 'list_forgiveness_messages.py', use valid token (page parameter can be changed )
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

lookup_api = client.validations

result = lookup_api.list(sba_number="{{SBA_NUMBER}}")

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
