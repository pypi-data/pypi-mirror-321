import requests

from camalis.exceptions import CamalisApiException


class BaseCamalisClient:
    token = None
    base_url = ''
    element_id = None

    def __init__(self, api_url, token, element_id):
        self.base_url = api_url
        self.token = token
        self.element_id = element_id

    def _check_status(self, response):
        if response.status_code in [200, 201]:
            if response.headers.get('Content-Type', None) == 'application/octet-stream':
                return response.content
            if response.text:
                return response.json()
            return None

        if response.status_code == 400:
            raise CamalisApiException(response.json()['message'])

        if response.status_code == 401:
            raise CamalisApiException('Token is invalid')

        if response.status_code == 404:
            raise CamalisApiException('Not found')

        raise CamalisApiException(f'Error, status code: {response.status_code}')

    def request_post(self, url, json):
        response = requests.post(f'{self.base_url}{url}', json=json, headers={
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'X-Origem': 'integracao'
        }, verify=False)

        return self._check_status(response)

    def request_get(self, url, content_type='application/json'):
        response = requests.get(f'{self.base_url}{url}', headers={
            'Authorization': f'Bearer {self.token}',
            'Content-Type': content_type,
            'X-Origem': 'integracao'
        }, verify=False)
        return self._check_status(response)
