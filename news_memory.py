#python 3
#import urllib.request as ur, json

#python 2
import urllib as ur, json

# Get list of possible news sources

def main():
	url = "https://newsapi.org/v1/sources?language=en"
	response = ur.urlopen(url)
	data = json.loads(response.read())


	outlets = dict()

	for source in data['sources']:
		outlets[source['name']] = source['id']

	return outlets

