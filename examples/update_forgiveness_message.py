from PPPForgivenessSDK.client import Client

# to run file 'read_forgiveness_message.py', use valid token and slug associated with a valid thread
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

message_api = client.messages

result = message_api.update('{{SLUG_HERE}}', int('{{DOCUMENT_TYPE_ID_HERE}}'),'{{DOCUMENT_NAME}}', '{{PATH_TO_DOCUMENT_FILE_HERE}}', '{{MESSAGE}}')


if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])



# read info for single forgiveness request
# result = message_api.update(slug='{{SLUG HERE}}', document_type, document_name, document, message_text=''):
# if result['status'] == 200:
#     print(result['data'])
# else:
#     print("An error occurred." + str(result['status']))
#     print(result['data'])
