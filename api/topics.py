from api.api import APIEndpoint

class API(APIEndpoint):
    def __init__(self, api, endpoint="topics/"):
        super(API, self).__init__(api)
        self.endpoint = endpoint

    def all(self):
        return super(API, self).get(self.endpoint)

    def get_topics(self, id_or_slug: str|int):
        return super(API, self).get("{}{}".format(self.endpoint, id_or_slug))

    def get_topics_photos(self, id_or_slug: str|int):
        return super(API, self).get("{}{}{}".format(self.endpoint, id_or_slug, '/photos'))