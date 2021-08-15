import requests

class Connect():
    def __init__(self, endpoint, **fields):
        self.endpoint = 'https://api.mangadex.org/{}'.format(endpoint)
        self.fields = fields

    def get_data(self):
        data = requests.get(self.endpoint, params=self.fields)
        return data.json()