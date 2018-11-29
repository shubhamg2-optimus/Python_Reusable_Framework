import requests

import logging
import json
from requests.adapters import HTTPAdapter
from requests_toolbelt.multipart.encoder import MultipartEncoder


class RequestHelper:
    """
    Class to help with HTTP requests using the requests library
    """

    def __init__(self, session=False, proxy=None):
        self.logger = logging.getLogger("api_common")
        self.url = None

        if session is not None:
            self.request_session = requests.Session()
        else:
            self.request_session = None
        if proxy is not None:
            self.proxydict = {
                "https": proxy,
                "http": proxy
            }
        else:
            self.proxydict = None

    def set_url(self, url):
        self.url = url

    def get_call(self, call_object):
        """
        Custom Get HTTP call
        :return:
        """

        api_endpoint = call_object.method
        if self.request_session is None:
            s = requests.Session()
            s.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = s.get(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                      params=call_object.parameters, verify=call_object.verify, stream=call_object.stream)
        else:
            self.request_session.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = self.request_session.get(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                                         params=call_object.parameters, verify=call_object.verify,
                                         stream=call_object.stream)

        self.logger.info('Response Code: %s' % r.status_code)
        return r

    def post_call(self, call_object):

        api_endpoint = self.url + call_object.method

        if call_object.stream:
            encoder = MultipartEncoder(fields=call_object.files)
            call_object.headers.update({'Content-type': encoder.content_type})
            call_object.data = encoder
            call_object.files = None

        if self.request_session is None:
            s = requests.Session()
            s.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = s.post(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                       params=call_object.parameters, verify=call_object.verify, stream=call_object.stream)
        else:
            self.request_session.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = self.request_session.post(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                                          params=call_object.parameters, verify=call_object.verify,
                                          stream=call_object.stream)

        self.logger.info('Response Code: %s' % r.status_code)
        return r

    def delete_call(self, call_object):
        """
        Custom Delete HTTP call
        :return:
        """
        api_endpoint = call_object.method
        if self.request_session is None:
            s = requests.Session()
            s.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = s.delete(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                         params=call_object.parameters, verify=call_object.verify, stream=call_object.stream)
        else:
            self.request_session.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = self.request_session.delete(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                                            params=call_object.parameters, verify=call_object.verify,
                                            stream=call_object.stream)

        self.logger.info('Response Code: %s' % r.status_code)
        return r

    def patch_call(self, call_object):
        """
        Custom Patch HTTP call
        :return:
        """
        api_endpoint = self.url + call_object.method
        if self.request_session is None:
            s = requests.Session()
            s.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = s.patch(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                        params=call_object.parameters, verify=call_object.verify, stream=call_object.stream)
        else:
            self.request_session.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = self.request_session.patch(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                                           params=call_object.parameters, verify=call_object.verify,
                                           stream=call_object.stream)

        self.logger.info('Response Code: %s' % r.status_code)
        return r

    def put_call(self, call_object):
        """
        Custom Put HTTP call
        :return:
        """
        api_endpoint = call_object.method

        if call_object.stream:
            encoder = MultipartEncoder(fields=call_object.files)
            call_object.headers.update({'Content-type': encoder.content_type})
            call_object.data = encoder
            call_object.files = None

        if self.request_session is None:
            s = requests.Session()
            s.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = s.put(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                      params=call_object.parameters, verify=call_object.verify, stream=call_object.stream)
        else:
            self.request_session.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = self.request_session.put(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                                         params=call_object.parameters, verify=call_object.verify,
                                         stream=call_object.stream)

        self.logger.info('Response Code: %s' % r.status_code)
        return r

    def options_call(self, call_object):
        """
        Custom Options HTTP call
        :return:
        """
        api_endpoint = self.url + call_object.method
        if self.request_session is None:
            s = requests.Session()
            s.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = s.options(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                          params=call_object.parameters, verify=call_object.verify, stream=call_object.stream)
        else:
            self.request_session.mount(api_endpoint, HTTPAdapter(max_retries=5))
            r = self.request_session.options(url=api_endpoint, headers=call_object.headers, data=call_object.data,
                                             params=call_object.parameters, verify=call_object.verify,
                                             stream=call_object.stream)

        self.logger.info('Response Code: %s' % r.status_code)
        return r


class CallObject(object):
    """
    Class structure with required pieces for making a request call
    """

    def __init__(self, method, parameters=None, headers=None, data=None, files=None, clean_data=True,
                 json_serialize=False, clean_parm=True, stream=None, verify=False):
        self.method = method

        if parameters is not None:
            if clean_parm and isinstance(parameters, dict):
                self.parameters = clean_dict(parameters)
            else:
                self.parameters = parameters
        else:
            self.parameters = parameters

        if headers is not None:
            self.headers = headers
        else:
            self.headers = {}

        if clean_data and data is not None and isinstance(data, dict):
            self.data = clean_dict(data)
        else:
            self.data = data
        if json_serialize:
            self.data = json.dumps(self.data)
        self.files = files
        self.stream = stream
        self.verify = verify


def clean_dict(params):
    result = {}
    result.update((k, v) for k, v in params.items() if v is not None and v != "" and v != [None] and v != [])
    if "self" in result.keys():
        del result['self']
    if 'params' in result.keys():
        del result['params']
    if result == {}:
        result = None
    return result
