import json
from .base_api import BaseApi, UnknownException


class EIDLLookupApi(BaseApi):
    def list(self, eidl_loan_number, page=1):
        """
        :param eidl_loan_number: str (optional)
        :param page: int (optional):
        :return:
        """
        assert (isinstance(page, int)), "page must be an integer"
        assert (isinstance(eidl_loan_number, str)), "eidl_loan_number must be a string"

        http_method = "GET"
        endpoint = "etran_eidl_loan_validation/"

        uri = self.client.api_uri + endpoint

        params = {
            'page': page,
            'eidl_loan_number': str(eidl_loan_number)
        }

        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    query_params=params)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException
