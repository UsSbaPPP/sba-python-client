import json
from .base_api import BaseApi, UnknownException


class LookupApi(BaseApi):
    def list(self, sba_number, page=1):
        """
        :param sba_number: str (optional)
        :param page: int (optional):
        :return:
        """
        assert (isinstance(page, int)), "page must be an integer"
        assert (isinstance(sba_number, str)), "sba_number must be a string"

        http_method = "GET"
        endpoint = "ppp_loan_validations/"

        uri = self.client.api_uri + endpoint

        params = {
            'page': page,
            'sba_number': str(sba_number)
        }

        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    query_params=params)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException
