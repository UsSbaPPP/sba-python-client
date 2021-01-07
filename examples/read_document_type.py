from PPPForgivenessSDK.client import Client

# to run file 'read_document_types.py', use valid token and valid DOCUMENT_TYPE_ID (int)
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

document_type_api = client.document_types

# read info for single document type
result = document_type_api.get(id=int('{{DOCUMENT_TYPE_ID_HERE}}'))

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
