import os
from getgauge.python import Messages
import requests


class API(object):
    BASE_API_URL = os.getenv('API_BASE_URL')

    # Constructor
    def __init__(self):
        self.method = None
        self.url = None
        self.params = None
        self.json = None
        self.headers = None

    # Method for get the headers
    def get_headers(self):
        self.headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
        return self.headers

    # Method for api request for all CRUD operations
    def api_request(self, method, endpoint, json_object=None,):
        base_url = self.BASE_API_URL
        url = base_url + endpoint
        headers = self.get_headers()
        request = requests.Request(
            method=method, url=url, params=None,
            json=json_object, headers=headers
        )
        request_prepared = request.prepare()
        self.log_request(request_prepared)
        request_session = requests.Session()
        response = request_session.send(request_prepared, verify=False)
        self._log_response(response)
        return response

    # Method for display the API request body, headers in Report file
    def log_request(self, req):
        Messages.write_message('\n<b>{} {}</b>'.format(req.method, req.url))
        Messages.write_message('\n<i>Request Headers:</i>')
        Messages.write_message('\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()))
        Messages.write_message('\n<i>Request Body:</i>')
        Messages.write_message('{}'.format(req.body))

    # Method for display the API request response in Report file
    def _log_response(self, res):
        Messages.write_message('\n---Response---')
        Messages.write_message('<i>Status code:</i> <b>{}</b>'.format(res.status_code))
        Messages.write_message('\n<i>Response Headers:</i>')
        Messages.write_message('\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()))
        if res.status_code != requests.codes.no_content:
            Messages.write_message('\n<i>Response Body:</i>')
            Messages.write_message('{}'.format(res.json()))
