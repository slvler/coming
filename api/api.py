class APIEndpoint(object):
    def __init__(self, api):
        self.api = api

    def request(self, method, url):
        response = self.api.execute(method, url)
        return response.json()

    def get(self, url):
        print(url)
        return self.request("GET", url)

    def put(self, url):
        return self.request("PUT", url)

    def post(self, url):
        return self.request("POST", url)

    def delete(self, url):
        return self.request("DELETE", url)