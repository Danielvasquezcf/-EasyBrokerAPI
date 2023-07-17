import requests

class EasyBrokerAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.stagingeb.com/v1/'

    def _make_request(self, method, endpoint, params=None):
        headers = {'X-Authorization': self.api_key}
        url = self.base_url + endpoint

        response = requests.request(method, url, headers=headers, params=params)
        response.raise_for_status()

        return response.json()

    def get_contact_requests(self, page=1, limit=20):
        endpoint = 'contact_requests'
        params = {'page': page, 'limit': limit}

        return self._make_request('GET', endpoint, params)

    def print_contact_request_titles(self, page=1, limit=20):
        contact_requests = self.get_contact_requests(page, limit)

        for request in contact_requests['content']:
            for key, value in request.items():
                print(f"{key}: {value}")
        print()


api_key = "l7u502p8v46ba3ppgvj5y2aad50lb9"
api = EasyBrokerAPI(api_key)
api.print_contact_request_titles()
