import datetime

#python 3
#import urllib.request as ur, json

#python 2
import urllib as ur, json


def read_list(lst):
	if len(lst) > 1:

		first_part = ', '.join(lst[0:len(lst) -1 ])
		second_part = str(lst[len(lst) - 1])

		sentance = first_part + " and " + second_part
	else:
		sentance = lst[0]
	return sentance


def omdb(title):
	title_correct = title.replace(" ", "+")
	url = "http://www.omdbapi.com/?t={0}&plot=short&tomatoes=True&r=json".format(title_correct)
	response = ur.urlopen(url)
	data = json.loads(response.read())

	title = data['Title']
	director = data['Director']
	cast_clean = read_list(data['Actors'].split(','))
	genres_clean = read_list(data['Genre'].split(','))
	awards = data['Awards']
	imdb = data['imdbRating']
	tomatoMeter = data['tomatoMeter']
	tomatoesUserMeter = data['tomatoUserMeter']
	consesus = data['tomatoConsensus']

	year = data['Year']

	speech = u"{0} is a {1} {2} film directed by {3}, starring {4}. It has an IMDb rating of {5}, a Rotten Tomatoes critic score of {6} and user score of {7}. The critic consesus was that {8}".format(title, 
		year, genres_clean, director, cast_clean, imdb, tomatoMeter, tomatoesUserMeter, consesus)

	return speech



