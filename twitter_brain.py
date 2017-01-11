# pulls various info from twitter API using tweepy

import tweepy
from get_creds import *


def trends(lat, lon):
	data = get_creds()['twitter']

	auth = tweepy.OAuthHandler(data["consumer_key"], data["consumer_secret"])
	auth.set_access_token(data["acc_token"], data["acc_token_secret"])

	api = tweepy.API(auth)

	place = api.trends_closest(lat, lon)

	pull = api.trends_place(place[0]["woeid"])
	trends = []
	for item in pull[0]['trends'][0:6]:
		trends.append(item["name"])

	return trends

