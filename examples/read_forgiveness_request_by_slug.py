from PPPForgivenessSDK.client import Client

# to run file 'read_forgiveness_requests.py', use valid token and slug associated with a valid forgiveness request
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

forgiveness_api = client.forgiveness_requests

# read info for single forgiveness request
result = forgiveness_api.get(slug='{{SLUG HERE}}') # get a single forgiveness request

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
