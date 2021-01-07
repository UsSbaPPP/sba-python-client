from PPPForgivenessSDK.client import Client

# to run file 'create_forgiveness_request_3508s.py', make sure python path includes path to sba_ppp_forgiveness-sdk
# , use a valid token and insure loan information matches a valid loan without a previous forgiveness request
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox',
)

forgiveness_api = client.forgiveness_requests

# create a new forgiveness request
# etran_loan must pass validation against SBA records based on amounts, full disbursement, ein match, sba number match and amount match
result = forgiveness_api.create(
                                bank_notional_amount='12345.67',
                                sba_number=int('12311'),
                                loan_number=int('12311'),
                                entity_name='Test Entity',
                                ein='111223456',
                                funding_date="2020-07-06",
                                forgive_eidl_amount=100.00,
                                forgive_eidl_application_number=123456789,
                                address1="5050 Ritter Road – Suite B",
                                address2="Mechanicsburg, PA",
                                dba_name="Abc Inc",
                                phone_number= "6102342123",
                                forgive_fte_at_loan_application= 10,
                                demographics= [],
                                forgive_amount= 1666.66,
                                forgive_fte_at_forgiveness_application= 10,
                                primary_email= "user@example.com",
                                primary_name= "Jason",
                                ez_form= False,
                                forgive_lender_confirmation= True,
                                forgive_lender_decision= 1,
                                s_form=True,
                    )


if result['status'] == 201:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
