from PPPForgivenessSDK.client import Client

# to run file 'create_forgiveness_request.py',  use a valid token and insure slug is associated with a valid loan
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

loan_documents_api = client.loan_documents

# create and upload a new loan_document
result = loan_documents_api.create('{{NAME_HERE}}', int('{{DOCUMENT_TYPE_ID_HERE}}'), '{{SLUG_HERE}}', '{{PATH_TO_DOCUMENT_FILE_HERE}}')

if result['status'] == 201:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
