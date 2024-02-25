import json
from .base_api import BaseApi


class LookupApi(BaseApi):
    def list(self, sba_number=None, page=1, first_draw_lookup=False, tin=None):
        """
        :param sba_number: str (optional)
        :param page: int (optional):
        :return:
        """
        assert (isinstance(page, int)), "page must be an integer"
        if tin is None:
            assert (isinstance(sba_number, str)), "sba_number must be a string"
        else:
            assert (isinstance(tin, str)), "tin must be a string"


        http_method = "GET"
        if not first_draw_lookup:
            endpoint = "ppp_loan_validations/"
        else:
            endpoint = "etran_ppp_validation/"

        uri = self.client.api_uri + endpoint

        params = {
            'page': page,
        }

        if tin:
            params['tin'] = tin
        else:
            params['sba_number'] = str(sba_number)

        response = self.execute(http_method=http_method,
                                url=uri,
                                query_params=params)

        return {'status': response.status_code,
                'data': json.loads(response.text)}
