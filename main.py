from client import Unsplash


api_key = 'unntZPEoj9kxhfHS4R-Iv0594jQk9EdqeJEhKt7RNPM'
secret_key = 'Qjup2n0MogMW36eb_TylUjasHD1iYQ2C6ZrbaZWbTd8'

unsplash = Unsplash(api_key, secret_key)


#print(unsplash.photos.all())
#print(unsplash.photos.show("S9HcGJmsmyc"))
#print(unsplash.photos.random())
#print(unsplash.photos.statistics("LF8gK8-HGSg"))
#print(unsplash.photos.photo_download("LF8gK8-HGSg"))
#print(unsplash.photos.update("S9HcGJmsmyc"))
#print(unsplash.photos.like_photo("LF8gK8-HGSg"))
#print(unsplash.photos.delete_like("LF8gK8-HGSg"))

# print(unsplash.users.public_profile("john"))
# print(unsplash.users.portfolio_link("john"))
# print(unsplash.users.list_user_photos("john"))
# print(unsplash.users.list_user_liked_photos("john"))
# print(unsplash.users.list_user_collections("john"))
# print(unsplash.users.list_user_statistics("john"))
# print(unsplash.collection.all())
# print(unsplash.collection.get_collection(2))
# print(unsplash.collection.get_collection_photos(2))
# print(unsplash.collection.get_related_collections(2))
print(unsplash.collection.create_collections())