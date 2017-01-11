# get json fle from newsapi.org

from print_speek import *
#python 3
#import urllib.request as ur, json

#python 2
import urllib as ur, json

def reader(source):
	url = "https://newsapi.org/v1/articles?source={0}&sortBy=top&apiKey=19d1e60dad134c9e91a675a9016a7801".format(source)


	response = ur.urlopen(url)
	data = json.loads(response.read())

	speech = []
	for item in data['articles']:
		author = item['author']
		title = item['title']

		if author == None:
			author = "Reporter"

		news = u"{0} writes; {1}".format(author, title)
		speech.append(news)

		
	return(speech)
