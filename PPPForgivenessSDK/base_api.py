import json
from requests import Response, session
from requests.adapters import HTTPAdapter
from urllib3 import Retry
import os


class UnknownException(Exception): pass
class InvalidTypeException(Exception): pass

class BaseApi(object):
    def __init__(self, client, verify=True):
        self.client = client

        self.timeout = self.client.timeout
        self.session = session()

        retries = Retry(total=self.client.max_retries, backoff_factor=self.client.backoff_factor)
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

        self.session.verify = verify

        #if 'Authorization' not in self.session.headers:
        #    self.authorize()

        self.session.headers['Authorization'] = 'Token ' + self.client.access_token
        if self.client.vendor_key:
            self.session.headers['Vendor-Key'] = self.client.vendor_key

 #   def execute(self, http_method: str, url: str, headers: dict = {}, query_params: dict = {}, data: dict = {},
 #               files: dict = {}) -> Response:
    def execute(self, http_method, url, headers={}, query_params={}, data={}, files={}):
        """Connect to the given url to get a response back

            :param http_method: method for the request.
            :param url: URL to connect to
            :param headers: (optional) Dictionary of extra HTTP headers to pass to the request
            :param query_params: (optional) Dictionary of bytes to be sent in the query string
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                            object to send in the body of the request
            :param files: (optional) Dictionary of ``'filename': file-like-objects``
                            for multipart encoding upload.

            :return: Response: The response of the request.
        """
        if self.client.extra_headers:
            headers.update(self.client.extra_headers)

        response = self.session.request(
            http_method,
            url,
            headers=headers,
            params=query_params,
            data=data,
            files=files,
            timeout=self.timeout
        )

        return response
