from api.api import APIEndpoint

class API(APIEndpoint):

    def __init__(self, api, endpoint="collections/"):
        super(API, self).__init__(api)
        self.endpoint = endpoint

    def all(self):
        return super(API, self).get("{}".format(self.endpoint))

    def get_collection(self, id: int):
        return super(API, self).get("{}{}".format(self.endpoint, id))

    def get_collection_photos(self, id: int):
        return super(API, self).get("{}{}{}".format(self.endpoint, id, '/photos'))

    def get_related_collections(self, id: int):
        return super(API, self).get("{}{}{}".format(self.endpoint, id, '/related'))
    def create_collections(self):
        return super(API, self).post("{}".format(self.endpoint))

    def update_collections(self, id: int):
        return super(API, self).put("{}{}".format(self.endpoint, id))

    def delete_collections(self, id: int):
        return super(API, self).delete("{}{}".format(self.endpoint, id))

    def collection_add_photo(self, collection_id: int):
        return super(API, self).post("{}{}{}".format(self.endpoint, collection_id, '/add'))

    def collection_remove_photo(self, collection_id: int):
        return super(API, self).delete("{}{}{}".format(self.endpoint, collection_id, '/remove'))