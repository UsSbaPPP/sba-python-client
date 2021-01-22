from PPPForgivenessSDK.client import Client

# to run file 'lookup_eidl_validation.py', use valid token (page parameter can be changed )
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

eidl_api = client.eidl_validations

result = eidl_api.list(eidl_loan_number="{{EIDL_LOAN_NUMBER}}")

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
