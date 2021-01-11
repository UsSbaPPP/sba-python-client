import json
from .base_api import BaseApi, UnknownException



class OriginationRequestApi(BaseApi):

    def delete(self, slug):
        """

        :param slug:
        :return:
        """

        http_method = "DELETE"
        endpoint = "origination/{0}/".format(slug)

        uri = self.client.api_uri + endpoint

        try:
            response = self.execute(http_method=http_method,
                                    url=uri)

            try:
                return {'status': response.status_code, 'data': json.loads(response.text)}
            except:
                return {'status': response.status_code, 'data': response.text}
        except:
            raise UnknownException # TODO: what about 405?

    def list(self, page=1):
        """

        :param page:
        :return:
        """
        assert isinstance(page, int), "Page must be a valid integer"

        http_method = "GET"
        endpoint = "ppp_loan_forgiveness_requests/"

        uri = self.client.api_uri + endpoint

        params = {'page': page}
        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    query_params=params)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def get(self, slug):
        """
        :param slug:
        :return:
        """

        http_method = "GET"
        endpoint = f"origination/{slug}"

        uri = self.client.api_uri + endpoint

        try:
            response = self.execute(http_method=http_method,
                                    url=uri)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def create(self,
            business,
            average_monthly_payroll,
            loan_amount,
            number_of_employees,
            purpose_of_loan_payroll,
            purpose_of_loan_mortgage,
            purpose_of_loan_utilities,
            purpose_of_loan_covered_operations_expenditures,
            purpose_of_loan_covered_property_damage,
            purpose_of_loan_covered_supplier_costs,
            purpose_of_loan_covered_worker_protection_expenditure,
            purpose_of_loan_other,
            purpose_of_loan_other_info,
            ineligible_general,
            ineligible_bad_loan,
            ineligible_criminal_charges,
            ineligible_felony,
            has_other_businesses,
            received_eidl,
            all_employees_residency,
            second_draw_ppp_loan,
            applicant_meets_size_standard,
            number_of_employees_at_time_of_application,
            anticipated_number_of_employees_retained,
            applicant_is_eligible,
            applicant_meets_revenue_test_and_size_standard,
            applicant_no_shuttered_venue_grant,
            loan_request_is_necessary,
            ppp_first_draw_sba_loan_number=None,
            ppp_first_draw_loan_amount=None,
            applicant_has_reduction_in_gross_receipts=None,
            applicant_wont_receive_another_second_draw=None,
            period_1_revenue=None,
            period_2_revenue=None,
            period_1_quarter=None,
            period_2_quarter=None,
            refinance_of_eidl_amount=None,
            refinance_of_eidl_loan_number=None,            
        ):

        """
        :return:
        """
        http_method = "POST"
        endpoint = "origination/"

        uri = self.client.api_uri + endpoint

        for field in [
                'owners',
                "naics_code",
                "business_type",
                "duns_number",
                "address_line_1",
                "address_line_2",
                "city",
                "state",
                "zip_code",
                "zip_code_plus4",
                "tin",
                "tin_type",
                "phone_number",
                "primary_contact",
                "primary_contact_email",
                "is_franchise",
                "is_sba_listed_franchise",
                "date_of_establishment",
                ]:
            assert field in business, f'{field} is missing from Business'

        if business['tin_type'] == 0: #EIN
            for field in [
                    "legal_name",
                    "dba_tradename",
                    ]:
                assert field in business, f'{field} is missing from Business with tin_type EIN'
        else: #SSN
            for field in [
                    "first_name",
                    "last_name",
                    "title",
                    ]:
                assert field in business, f'{field} is missing from Business with tin_type SSN'

        if business['is_sba_listed_franchise'] or business['is_franchise']:
            assert 'franchise_code' in business, f'franchise_code is missing from Business that has set is_sba_listed_franchise to True'

        if period_1_revenue or period_2_revenue:
            assert period_1_quarter is not None
            assert period_2_quarter is not None

        for owner in business['owners']:
            for field in [
                    "owner_type",
                    "duns_number",
                    "ownership_percentage",
                    "tin",
                    "tin_type",
                    "address_line_1",
                    "address_line_2",
                    "city",
                    "state",
                    "zip_code",
                    "zip_code_plus4",
                    "position",
                    "veteran_status",
                    "gender",
                    "ethnicity",
                    "race",
                    ]:
                assert field in owner, f'{field} is missing from BusinessOwner'

            if owner['tin_type'] == 0: #EIN
                for field in [
                        "business_name",
                        "business_type",
                        ]:
                    assert field in owner, f'{field} is missing from BusinessOwner with tin_type EIN'
            else: #SSN
                for field in [
                        "first_name",
                        "last_name",
                        "title",
                        ]:
                    assert field in owner, f'{field} is missing from BusinessOwner with tin_type SSN'

        params = {
            "business": business,
            "average_monthly_payroll": average_monthly_payroll,
            "loan_amount": loan_amount,
            "number_of_employees": number_of_employees,
            "period_1_revenue": period_1_revenue,
            "period_1_quarter": period_1_quarter,
            "period_2_revenue": period_2_revenue,
            "period_2_quarter": period_2_quarter,
            "purpose_of_loan_payroll": purpose_of_loan_payroll,
            "purpose_of_loan_mortgage": purpose_of_loan_mortgage,
            "purpose_of_loan_utilities": purpose_of_loan_utilities,
            "purpose_of_loan_covered_operations_expenditures": purpose_of_loan_covered_operations_expenditures,
            "purpose_of_loan_covered_property_damage": purpose_of_loan_covered_property_damage,
            "purpose_of_loan_covered_supplier_costs": purpose_of_loan_covered_supplier_costs,
            "purpose_of_loan_covered_worker_protection_expenditure": purpose_of_loan_covered_worker_protection_expenditure,
            "purpose_of_loan_other": purpose_of_loan_other,
            "purpose_of_loan_other_info": purpose_of_loan_other_info,
            "ineligible_general": ineligible_general,
            "ineligible_bad_loan": ineligible_bad_loan,
            "ineligible_criminal_charges": ineligible_criminal_charges,
            "ineligible_felony": ineligible_felony,
            "has_other_businesses": has_other_businesses,
            "received_eidl": received_eidl,
            "all_employees_residency": all_employees_residency,
            "second_draw_ppp_loan": second_draw_ppp_loan,
            "applicant_meets_size_standard": applicant_meets_size_standard,
            "number_of_employees_at_time_of_application": number_of_employees_at_time_of_application,
            "anticipated_number_of_employees_retained": anticipated_number_of_employees_retained,
            'applicant_is_eligible': applicant_is_eligible,
            'applicant_meets_revenue_test_and_size_standard': applicant_meets_revenue_test_and_size_standard,
            'applicant_no_shuttered_venue_grant': applicant_no_shuttered_venue_grant,
            'loan_request_is_necessary': loan_request_is_necessary,
            'applicant_has_reduction_in_gross_receipts': applicant_has_reduction_in_gross_receipts,
            'applicant_wont_receive_another_second_draw': applicant_wont_receive_another_second_draw,
            'refinance_of_eidl_amount': refinance_of_eidl_amount,
            'refinance_of_eidl_loan_number': refinance_of_eidl_loan_number,  
        }

        
        if second_draw_ppp_loan:
            assert ppp_first_draw_sba_loan_number is not None, 'ppp_first_draw_sba_loan_number can not be None if submitting a Second Draw Loan'
            assert ppp_first_draw_loan_amount is not None, 'ppp_first_draw_loan_amount can not be None if submitting a Second Draw Loan'
            params['ppp_first_draw_sba_loan_number'] = ppp_first_draw_sba_loan_number
            params['ppp_first_draw_loan_amount'] = ppp_first_draw_loan_amount

        headers = {'Content-Type': 'application/json'}
        try:
            response = self.execute(http_method=http_method,
                                    headers=headers,
                                    url=uri,
                                    data=json.dumps(params))

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException
