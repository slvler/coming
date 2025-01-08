from api.api import APIEndpoint

class API(APIEndpoint):

    def __init__(self, api, endpoint="users/"):
        super(API, self).__init__(api)
        self.endpoint = endpoint

    def public_profile(self, username: str):
        return super(API, self).get("{}{}".format(self.endpoint, username))

    def portfolio_link(self, username: str):
        return super(API, self).get("{}{}{}".format(self.endpoint, username, "/portfolio"))

    def list_user_photos(self, username: str):
        return super(API, self).get("{}{}{}".format(self.endpoint, username, "/photos"))

    def list_user_liked_photos(self, username: str):
        return super(API, self).get("{}{}{}".format(self.endpoint, username, "/likes"))

    def list_user_collections(self, username: str):
        return super(API, self).get("{}{}{}".format(self.endpoint, username, "/collections"))

    def list_user_statistics(self, username: str):
        return super(API, self).get("{}{}{}".format(self.endpoint, username, "/statistics"))