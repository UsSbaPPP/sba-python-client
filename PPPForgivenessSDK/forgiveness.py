import json
from .base_api import BaseApi, UnknownException



class ForgivenessRequestApi(BaseApi):

    def delete(self, slug):
        """

        :param slug:
        :return:
        """

        http_method = "DELETE"
        endpoint = "ppp_loan_forgiveness_requests/{0}/".format(slug)

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

    def get(self, slug, sbanumber=None):
        """

        :param slug:
        :return:
        """

        http_method = "GET"
        if sbanumber is None:
            endpoint = "ppp_loan_forgiveness_requests/{0}/".format(slug)
        else:
            endpoint = "ppp_loan_forgiveness_requests/?sba_number={0}".format(sbanumber)

        uri = self.client.api_uri + endpoint

        try:
            response = self.execute(http_method=http_method,
                                    url=uri)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def create(self,
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
            forgive_lender_confirmation,
            forgive_lender_decision,
            forgive_2_million=None,
            forgive_payroll=None,
            forgive_rent=None,
            forgive_utilities=None,
            forgive_mortgage=None,
            forgive_line_6_3508_or_line_5_3508ez=None,
            forgive_payroll_cost_60_percent_requirement=None,
            forgive_payroll_schedule=None,
            no_reduction_in_employees=None,
            no_reduction_in_employees_and_covid_impact=None,
            forgive_covered_period_from=None,
            forgive_covered_period_to=None,
            demographics=[],
            forgive_eidl_amount=None,
            forgive_eidl_application_number=None,
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
            forgive_alternate_covered_period_from=None,
            forgive_alternate_covered_period_to=None,
            s_form=False,
        ):
        """
        :param bank_notional_amount:
        :param sba_number:
        :param loan_number:
        :param entity_name:
        :param ein:
        :param funding_date:
        :param forgive_eidl_amount:
        :param forgive_eidl_application_number:
        :param forgive_payroll:
        :param forgive_rent:
        :param forgive_utilities:
        :param forgive_mortgage:
        :param address1:
        :param address2:
        :param dba_name:
        :param phone_number:
        :param forgive_fte_at_loan_application:
        :param demographics:
        :param forgive_line_6_3508_or_line_5_3508ez:
        :param forgive_modified_total:
        :param forgive_payroll_cost_60_percent_requirement:
        :param forgive_amount:
        :param forgive_fte_at_forgiveness_application:
        :param forgive_schedule_a_line_1:
        :param forgive_schedule_a_line_2:
        :param forgive_schedule_a_line_3_checkbox:
        :param forgive_schedule_a_line_3:
        :param forgive_schedule_a_line_4:
        :param forgive_schedule_a_line_5:
        :param forgive_schedule_a_line_6:
        :param forgive_schedule_a_line_7:
        :param forgive_schedule_a_line_8:
        :param forgive_schedule_a_line_9:
        :param forgive_schedule_a_line_10:
        :param forgive_schedule_a_line_10_checkbox:
        :param forgive_schedule_a_line_11:
        :param forgive_schedule_a_line_12:
        :param forgive_schedule_a_line_13:
        :param forgive_covered_period_from:
        :param forgive_covered_period_to:
        :param forgive_alternate_covered_period_from:
        :param forgive_alternate_covered_period_to:
        :param forgive_2_million:
        :param forgive_payroll_schedule:
        :param primary_email:
        :param primary_name:
        :param ez_form:
        :param s_form:
        :param no_reduction_in_employees:
        :param no_reduction_in_employees_and_covid_impact:
        :param forgive_lender_confirmation;
        :param forgive_lender_decision;
        :return:
        """
        http_method = "POST"
        endpoint = "ppp_loan_forgiveness_requests/"

        uri = self.client.api_uri + endpoint

        if not s_form:
            # enforce fields not previously allowed as None for 3508/3508EZ
            assert (forgive_payroll is not None), "forgive_payroll cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_utilities is not None), "forgive_utilities cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_mortgage is not None), "forgive_mortgage cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_rent is not None), "forgive_rent cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_line_6_3508_or_line_5_3508ez is not None), "forgive_line_6_3508_or_line_5_3508ez cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_payroll_cost_60_percent_requirement is not None), "forgive_payroll_cost_60_percent_requirement cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_payroll_schedule is not None), "forgive_payroll_schedule cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_period_to is not None), "forgive_covered_period_to cannot be None when 3508 or 3508EZ is selected"
            assert (forgive_covered_period_from is not None), "forgive_covered_period_from cannot be None when 3508 or 3508EZ is selected"

        if not s_form and not ez_form:
            assert (no_reduction_in_employees is not None), "no_reduction_in_employees cannot be None when 3508 or 3508EZ is selected"
            assert (no_reduction_in_employees_and_covid_impact is not None), "no_reduction_in_employees_and_covid_impact cannot be None when 3508 or 3508EZ is selected"

        # mandatory fields for all forms, Full, EZ, S
        params = {
            'etran_loan': {
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
            }
        }

        if not s_form:
            # mandatory fields for EZ, Full
            params['etran_loan'].update({
                "forgive_covered_period_from": forgive_covered_period_from,
                "forgive_covered_period_to": forgive_covered_period_to,
                "forgive_2_million": forgive_2_million,
                "forgive_payroll": forgive_payroll,
                "forgive_rent": forgive_rent,
                "forgive_utilities": forgive_utilities,
                "forgive_mortgage": forgive_mortgage,
                "forgive_line_6_3508_or_line_5_3508ez": forgive_line_6_3508_or_line_5_3508ez,
                "forgive_payroll_cost_60_percent_requirement": forgive_payroll_cost_60_percent_requirement,
                "forgive_payroll_schedule": forgive_payroll_schedule,
            })
            # optional fields for EZ, Full
            if forgive_alternate_covered_period_from: params['etran_loan']['forgive_alternate_covered_period_from'] = forgive_alternate_covered_period_from
            if forgive_alternate_covered_period_to: params['etran_loan']['forgive_alternate_covered_period_to'] = forgive_alternate_covered_period_to

        # optional fields for all 3, S, EZ, Full
        if forgive_eidl_amount: params['etran_loan']['forgive_eidl_amount'] = forgive_eidl_amount
        if forgive_eidl_application_number: params['etran_loan']['forgive_eidl_application_number'] = forgive_eidl_application_number
        if dba_name: params['etran_loan']['dba_name'] = dba_name
        if demographics: params['etran_loan']['demographics'] = demographics


        if not ez_form and not s_form:
            # mandatory fields for Full
            params['etran_loan'].update({
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
            if forgive_schedule_a_line_11: params['etran_loan']['forgive_schedule_a_line_11'] = forgive_schedule_a_line_11
            if forgive_schedule_a_line_12: params['etran_loan']['forgive_schedule_a_line_12'] = forgive_schedule_a_line_12

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
