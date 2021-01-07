from PPPForgivenessSDK.client import Client

# to run file 'create_origination_request.py', make sure python path includes path to sba_ppp_forgiveness-sdk
# aknd use a valid token
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox',
)

origination_api = client.origination_requests

business = {
    "owners": [
        {
            "business_name": "ABCD Corp",
            "owner_type": 2,
            "legal_name": "abcd inc",
            "duns_number": "047302511",
            "business_type": 2,
            "ownership_percentage": 25,
            "tin": "252751624",
            "tin_type": 0,
            "address_line_1": "123 Second St",
            "address_line_2": "",
            "city": "Manhattan",
            "state": "NY",
            "zip_code": "10004",
            "zip_code_plus4": "1234",
            "position": "Director",
            "veteran_status": "1",
            "gender": "M",
            "ethnicity": "N",
            "race": [
                "1",
                "2"
            ]
        }
    ],
    "naics_code": "722513",
    "business_type": 2,
    "dba_tradename": "XYZ Corp",
    "duns_number": "047302512",
    "legal_name": "ABC Corp",
    "address_line_1": "5050 Ritter Rd",
    "address_line_2": "Suite B",
    "city": "Mechanicsburg",
    "state": "PA",
    "zip_code": "17055",
    "zip_code_plus4": "1234",
    "tin": "670051470",
    "tin_type": 0,
    "phone_number": "5482562187",
    "primary_contact": "James",
    "primary_contact_email": "user@example.com",
    "is_franchise": False,
    #"franchise_code": None,
    "date_of_establishment": "2019-01-01"
}

result = origination_api.create(
    business=business,
    average_monthly_payroll=1000,
    loan_amount=2500,
    number_of_employees=1,
    period_1_revenue=10000,
    period_2_revenue=6000,
    purpose_of_loan_payroll=True,
    purpose_of_loan_mortgage=False,
    purpose_of_loan_utilities=False,
    purpose_of_loan_covered_operations_expenditures=False,
    purpose_of_loan_covered_property_damage=False,
    purpose_of_loan_covered_supplier_costs=False,
    purpose_of_loan_covered_worker_protection_expenditure=False,
    purpose_of_loan_other=False,
    purpose_of_loan_other_info="",
    ineligible_general=True,
    ineligible_bad_loan=True,
    ineligible_criminal_charges=True,
    ineligible_felony=True,
    has_other_businesses=True,
    received_eidl=True,
    all_employees_residency=True,
    second_draw_ppp_loan=True,
    ppp_first_draw_sba_loan_number='6900051470',
    ppp_first_draw_loan_amount=900000.00,
    applicant_meets_size_standard=1,
    number_of_employees_at_time_of_application=10,
    anticipated_number_of_employees_retained=10,
    applicant_is_eligible=True,
    applicant_meets_revenue_test_and_size_standard=True,
    applicant_no_shuttered_venue_grant=True,
    loan_request_is_necessary=True,
    applicant_has_reduction_in_gross_receipts=True,
    applicant_wont_receive_another_second_draw=True,
)


if result['status'] == 201:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
