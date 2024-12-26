from api.api import APIEndpoint
class API(APIEndpoint):
    def __init__(self, api, endpoint="photos/"):
        super(API, self).__init__(api)
        self.endpoint = endpoint

    def all(self):
        return super(API, self).get(self.endpoint)

    def show(self, id):
        return super(API, self).get(self.endpoint + id)

    def random(self):
        return super(API, self).get(self.endpoint + "random")

    def statistics(self, id):
        return super(API, self).get(self.endpoint + id + "/statistics")

    def photo_download(self, id):
        return super(API, self).get(self.endpoint + id + "/download")

    def update(self, id):
        return super(API, self).put(self.endpoint + id)

    def like_photo(self, id):
        return super(API, self).post(self.endpoint + id + "/like")

    def delete_like(self, id):
        return super(API, self).delete(self.endpoint + id + "/like")