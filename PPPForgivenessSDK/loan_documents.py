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