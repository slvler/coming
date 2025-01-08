from api.api import APIEndpoint

class API(APIEndpoint):
    def __init__(self, api, endpoint="stats/"):
        super(API, self).__init__(api)
        self.endpoint = endpoint

    def total(self):
        return super(API, self).get("{}{}".format(self.endpoint, '/total'))

    def month(self):
        return super(API, self).get("{}{}".format(self.endpoint, '/month'))
