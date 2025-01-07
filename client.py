import urllib3
from api import photos
from api import users

DEFAULT_URL = 'https://api.unsplash.com/'

class UnsplashClient:
    def __init__(self, api_key, secret_key, host=DEFAULT_URL):
        self.api_key = api_key
        self.secret_key = secret_key
        if host.endswith('/'):
            self.host = host
        else:
            self.host = host + '/'

    def execute(self, method, path):
        url = "{}{}".format(self.host, path)
        response = urllib3.request(
            method,
            url,
            fields={'client_id': self.api_key}
        )
        return response

class Unsplash:
    def __init__(self, api_key, secret_key, client=UnsplashClient):
        self.client = client(api_key, secret_key)
        self.photos = photos.API(self.client)
        self.users = users.API(self.client)

