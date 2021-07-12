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
