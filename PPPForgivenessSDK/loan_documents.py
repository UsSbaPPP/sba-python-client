import json

from .base_api import BaseApi, UnknownException


class LoanDocumentsApi(BaseApi):
    def create(self, name, document_type, etran_loan, document):
        """
        :param name:
        :param document_type:
        :param etran_loan:
        :param document:
        :return:
        """
        http_method = "POST"
        endpoint = "ppp_loan_documents/"
        uri = self.client.api_uri + endpoint
        params = {'name': name, 'document_type': document_type, 'etran_loan': etran_loan}
        files = {'document': open(document, 'rb')}
        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    data=params,
                                    files=files)
            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def list(self, sba_number, page=1):
        """
        :param sba_number: str:
        :param page: int (optional):
        :return:
        """
        assert (isinstance(page, int)), "page must be an integer"
        assert (isinstance(sba_number, str)), "sba_number must be a string"

        http_method = "GET"
        endpoint = "ppp_loan_documents/"

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

    def get(self, slug):
        """
        :param slug: str:
        :return:
        """
        assert (isinstance(slug, str)), "sba_number must be a string"

        http_method = "GET"
        endpoint = "ppp_loan_documents/{0}/".format(slug)

        uri = self.client.api_uri + endpoint

        params = {
            'slug': str(slug)
        }

        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    query_params=params)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException
