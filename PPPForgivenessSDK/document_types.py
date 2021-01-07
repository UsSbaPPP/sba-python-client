import json

from .base_api import BaseApi, UnknownException



class DocumentTypeApi(BaseApi):

    def list(self, name=None, description=None, page=1):

        """

        :param name:
        :param description:
        :param page:
        :return:
        """
        assert (isinstance(page, int)), "page must be an integer"

        http_method = "GET"
        endpoint = "ppp_loan_document_types/"

        uri = self.client.api_uri + endpoint

        params = {'page': page}
        if name:
            params['name'] = str(name)
        if description:
            params['description'] = str(description)

        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    query_params=params)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException



    def get(self, id):
        """

        :param id:
        :return:
        """
        assert (isinstance(id, int)), "id must be an integer"

        http_method = "GET"
        endpoint = "ppp_loan_document_types/{0}/".format(str(id))

        uri = self.client.api_uri + endpoint
        print (uri)
        try:
            response = self.execute(http_method=http_method,
                                    url=uri)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException
