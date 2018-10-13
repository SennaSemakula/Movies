from imdb import IMDb
ia = IMDb()

"""This function will return a list of movies that satifies the wildcard"""
def search_movie(title):
	movie = ia.search_movie(title)

	return movie

predator_options = search_movie('predator')
# print("Movies that were listed were ")
# print(predator_options)
retrive_movie()
