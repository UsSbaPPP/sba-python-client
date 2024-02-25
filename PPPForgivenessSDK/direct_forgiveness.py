import json
from .base_api import BaseApi



class DirectForgivenessApi(BaseApi):

    def status(self, sba_number):
        http_method = "GET"
        endpoint = "direct_forgiveness_status/{0}/".format(sba_number)

        uri = self.client.api_uri + endpoint

        response = self.execute(http_method=http_method,
                                url=uri)

        return {'status': response.status_code,
                'data': json.loads(response.text)}

    def eligibility(self, sba_number, tin):
        http_method = "GET"
        endpoint = "direct_forgiveness_eligibility/?sba_number={0}&tin={1}".format(sba_number, tin)

        uri = self.client.api_uri + endpoint

        response = self.execute(http_method=http_method,
                                url=uri)

        return {'status': response.status_code,
                'data': json.loads(response.text)}

    def submit(self,
        bank_notional_amount,
        sba_number,
        loan_number,
        entity_name,
        ein,
        funding_date,
        address1,
        address2,
        phone_number,
        forgive_fte_at_loan_application,
        forgive_amount,
        forgive_fte_at_forgiveness_application,
        primary_email,
        primary_name,
        ez_form,
        ppp_loan_draw,
        naics_code,
        forgive_lender_confirmation,
        forgive_lender_decision,
        forgive_payroll,
        forgive_2_million=None,
        forgive_rent=None,
        forgive_utilities=None,
        forgive_mortgage=None,
        forgive_covered_operations_expenditures=None,
        forgive_covered_property_damage_costs=None,
        forgive_covered_supplier_costs=None,
        forgive_covered_protection_expenditures=None,
        forgive_line_6_3508_or_line_5_3508ez=None,
        forgive_payroll_cost_60_percent_requirement=None,
        no_reduction_in_employees=None,
        no_reduction_in_employees_and_covid_impact=None,
        forgive_covered_period_from=None,
        forgive_covered_period_to=None,
        demographics=[],
        dba_name=None,
        forgive_modified_total=None,
        forgive_schedule_a_line_1=None,
        forgive_schedule_a_line_2=None,
        forgive_schedule_a_line_3_checkbox=None,
        forgive_schedule_a_line_3=None,
        forgive_schedule_a_line_4=None,
        forgive_schedule_a_line_5=None,
        forgive_schedule_a_line_6=None,
        forgive_schedule_a_line_7=None,
        forgive_schedule_a_line_8=None,
        forgive_schedule_a_line_9=None,
        forgive_schedule_a_line_10=None,
        forgive_schedule_a_line_10_checkbox=None,
        forgive_schedule_a_line_11=None,
        forgive_schedule_a_line_12=None,
        forgive_schedule_a_line_13=None,
        s_form=False,
        loan_increase=None,
        loan_increase_date=None
    ):
        """
        This is an updated create method that supports 3508 FUll and EZ forms in addition to 3508 S.
        """
        http_method = "POST"
        endpoint = "direct_forgiveness_submit/"
        uri = self.client.api_uri + endpoint

        if not s_form:
            # enforce fields not previously allowed as None for 3508/3508EZ
            assert (forgive_utilities is not None), "forgive_utilities cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_mortgage is not None), "forgive_mortgage cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_rent is not None), "forgive_rent cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_operations_expenditures is not None), "forgive_covered_operations_expenditures cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_property_damage_costs is not None), "forgive_covered_property_damage_costs cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_supplier_costs is not None), "forgive_covered_supplier_costs cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_protection_expenditures is not None), "forgive_covered_protection_expenditures cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_line_6_3508_or_line_5_3508ez is not None), "forgive_line_6_3508_or_line_5_3508ez cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_payroll_cost_60_percent_requirement is not None), "forgive_payroll_cost_60_percent_requirement cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_period_to is not None), "forgive_covered_period_to cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_period_from is not None), "forgive_covered_period_from cannot be None when 3508 or 3508EZ is selected"

        if not s_form and not ez_form:
            assert (no_reduction_in_employees is not None), "no_reduction_in_employees cannot be None when 3508 or 3508EZ is selected"
            assert (no_reduction_in_employees_and_covid_impact is not None), "no_reduction_in_employees_and_covid_impact cannot be None when 3508 or 3508EZ is selected"

        if loan_increase or loan_increase_date:
            assert (loan_increase is not None), "loan_increase cannot be None when a loan_increase_date is supplied"
            assert (loan_increase_date is not None), "loan_increase_date cannot be None when a loan_increase is supplied"

        # mandatory fields for all forms, Full, EZ, S
        params = {
            "bank_notional_amount": bank_notional_amount,
            "sba_number": sba_number,
            "loan_number": loan_number,
            "entity_name": entity_name,
            "ein": ein,
            "funding_date": funding_date,
            "address1": address1,
            "address2": address2,
            "phone_number": phone_number,
            "forgive_fte_at_loan_application": forgive_fte_at_loan_application,
            "forgive_amount": forgive_amount,
            "forgive_fte_at_forgiveness_application": forgive_fte_at_forgiveness_application,
            "primary_email": primary_email,
            "primary_name": primary_name,
            "ez_form": ez_form,
            'forgive_lender_confirmation': forgive_lender_confirmation,
            'forgive_lender_decision': forgive_lender_decision,
            's_form': s_form,
            "forgive_2_million": forgive_2_million,
            "forgive_covered_period_from": forgive_covered_period_from,
            "forgive_covered_period_to": forgive_covered_period_to,
            "forgive_payroll": forgive_payroll,
            "ppp_loan_draw": ppp_loan_draw,
            "naics_code": naics_code,
            "loan_increase": loan_increase,
            "loan_increase_date": loan_increase_date
        }

        if not s_form:
            # mandatory fields for EZ, Full
            params.update({
                "forgive_rent": forgive_rent,
                "forgive_utilities": forgive_utilities,
                "forgive_mortgage": forgive_mortgage,
                "forgive_covered_operations_expenditures": forgive_covered_operations_expenditures,
                "forgive_covered_property_damage_costs": forgive_covered_property_damage_costs,
                "forgive_covered_supplier_costs": forgive_covered_supplier_costs,
                "forgive_covered_protection_expenditures": forgive_covered_protection_expenditures,
                "forgive_line_6_3508_or_line_5_3508ez": forgive_line_6_3508_or_line_5_3508ez,
                "forgive_payroll_cost_60_percent_requirement": forgive_payroll_cost_60_percent_requirement,
            })

        # optional fields for all 3, S, EZ, Full
        if dba_name: params['dba_name'] = dba_name
        if demographics: params['demographics'] = demographics


        if not ez_form and not s_form:
            # mandatory fields for Full
            params.update({
                "no_reduction_in_employees": no_reduction_in_employees,
                "no_reduction_in_employees_and_covid_impact": no_reduction_in_employees_and_covid_impact,
                'forgive_modified_total': forgive_modified_total,
                'forgive_schedule_a_line_1': forgive_schedule_a_line_1,
                "forgive_schedule_a_line_2": forgive_schedule_a_line_2,
                "forgive_schedule_a_line_3_checkbox": forgive_schedule_a_line_3_checkbox,
                "forgive_schedule_a_line_3": forgive_schedule_a_line_3,
                "forgive_schedule_a_line_4": forgive_schedule_a_line_4,
                "forgive_schedule_a_line_5": forgive_schedule_a_line_5,
                "forgive_schedule_a_line_6": forgive_schedule_a_line_6,
                "forgive_schedule_a_line_7": forgive_schedule_a_line_7,
                "forgive_schedule_a_line_8": forgive_schedule_a_line_8,
                "forgive_schedule_a_line_9": forgive_schedule_a_line_9,
                "forgive_schedule_a_line_10": forgive_schedule_a_line_10,
                "forgive_schedule_a_line_10_checkbox": forgive_schedule_a_line_10_checkbox,
                "forgive_schedule_a_line_13": forgive_schedule_a_line_13,
            })

            # optional fields for Full
            if forgive_schedule_a_line_11: params['forgive_schedule_a_line_11'] = forgive_schedule_a_line_11
            if forgive_schedule_a_line_12: params['forgive_schedule_a_line_12'] = forgive_schedule_a_line_12

        headers = {'Content-Type': 'application/json'}
        response = self.execute(http_method=http_method,
                                headers=headers,
                                url=uri,
                                data=json.dumps(params))

        return {'status': response.status_code,
                'data': json.loads(response.text)}

    def create(self,
               entity_name,
               address1,
               address2,
               ein,
               naics_code,
               primary_name,
               primary_email,
               phone_number,
               ppp_loan_draw,
               sba_number,
               loan_number,
               bank_notional_amount,
               funding_date,
               forgive_covered_period_from,
               forgive_covered_period_to,
               forgive_fte_at_loan_application,
               forgive_fte_at_forgiveness_application,
               forgive_2_million,
               forgive_payroll,
               forgive_amount,
               dba_name=None,
               demographics=[],
               loan_increase=None,
               loan_increase_date=None):
        http_method = "POST"
        endpoint = "direct_forgiveness_submit/"
        uri = self.client.api_uri + endpoint

        params = {
            "entity_name": entity_name,
            "address1": address1,
            "address2": address2,
            "ein": ein,
            "naics_code": naics_code,
            "primary_name": primary_name,
            "primary_email": primary_email,
            "phone_number": phone_number,
            "ppp_loan_draw": ppp_loan_draw,
            "sba_number": sba_number,
            "loan_number": loan_number,
            "bank_notional_amount": bank_notional_amount,
            "funding_date": funding_date,
            "forgive_covered_period_from": forgive_covered_period_from,
            "forgive_covered_period_to": forgive_covered_period_to,
            "forgive_fte_at_loan_application": forgive_fte_at_loan_application,
            "forgive_fte_at_forgiveness_application": forgive_fte_at_forgiveness_application,
            "forgive_2_million": forgive_2_million,
            "forgive_payroll": forgive_payroll,
            "forgive_amount": forgive_amount,
        }

        # optional fields
        if dba_name: params['dba_name'] = dba_name
        if demographics: params['demographics'] = demographics
        if loan_increase: params['loan_increase'] = loan_increase
        if loan_increase_date: params['loan_increase_date'] = loan_increase_date

        headers = {'Content-Type': 'application/json'}
        response = self.execute(http_method=http_method,
                                headers=headers,
                                url=uri,
                                data=json.dumps(params))

        return {'status': response.status_code,
                'data': json.loads(response.text)}

    def delete(self, sba_number):
        http_method = "DELETE"
        endpoint = "direct_forgiveness_submit/{0}/".format(sba_number)

        uri = self.client.api_uri + endpoint
        response = self.execute(http_method=http_method,
                                url=uri)

        return {'status': response.status_code,
                'data': json.loads(response.text)}

    def create_document(self, name, etran_loan, document_type, document):
        http_method = "POST"
        endpoint = "direct_forgiveness_document/"
        uri = self.client.api_uri + endpoint
        params = {'name': name, 'document_type': document_type, 'etran_loan': etran_loan}
        files = {'document': open(document, 'rb')}
        response = self.execute(http_method=http_method,
                                url=uri,
                                data=params,
                                files=files)
        return {'status': response.status_code,
                'data': json.loads(response.text)}

    def list(self, sba_number = None, page = 1, status = 'pending'):
        http_method = "GET"
        endpoint = "direct_forgiveness_requests/"

        uri = self.client.api_uri + endpoint
        params = {"page": page}
        if sba_number: params["sba_number"] = sba_number
        if status: 
            assert status in ('pending', 'approved', 'rejected', 'borrower_correction', 'failed_validation', 'all',), 'status must be one of pending, approved, rejected, borrower_correction, failed_validation or all'
            params["status"] = status

        response = self.execute(http_method=http_method,
                                url=uri,
                                data=params)
        return {'status': response.status_code,
                'data': json.loads(response.text)}
