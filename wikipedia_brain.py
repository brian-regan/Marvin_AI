import urllib as ur
import json


def search_wiki(term):
	url_term = ur.quote(term)
	url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={0}&format=json".format(url_term)
	response = ur.urlopen(url)
	data = json.loads(response.read())
	top_results = data["query"]["search"][0]
	
	title = ur.quote(top_results["title"])
	page_url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={0}".format(title)

	response = ur.urlopen(page_url)
	data = json.loads(response.read())

	pages = data['query']['pages']
	extract = pages[pages.keys()[0]]['extract']
	title = pages[pages.keys()[0]]['title']

	extract.replace("\n", "")

	d = {"title": title, "extract": extract}
	return d
