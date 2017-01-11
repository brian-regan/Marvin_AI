# Marvin_AI

![Logo](https://raw.githubusercontent.com/brian-regan/Marvin_AI/master/marvin_logo.png)

The beginnings of a basic home AI system for tasks such as email and calendar reading, movie information, wikipedia searching, weather reports and more.

## Features and API's
Voice activated commands and text to speech responses with the following features:

* Weather Reporting with [Dark Sky](https://darksky.net/dev/)
* Google Calendar and Gmail Summaries
* Twitter trends.
* News headlines from [News API](https://newsapi.org/)
* Film information from [OMDb API](https://www.omdbapi.com/)

## Triggers
After running ears.py the speech *"Hello Marvin"* will activate the system to listen for other commands. Note that these commands only work after *"Hello Marvin"* was woken the system.

* *"News [source]"* will read news headlines from the given source.
* *"calendar"* will read upcoming Google calendar events.
* *"weather"* will read the weeks weather forecast for the locations specified in creds.json.
* *"email"* will read the sender and subject line of unread, important emails from your gmail inbox.
* *"movie [movie name]"* will read some information about the genre, cast, crew and ratings of the movie.
* *"wiki [query]"* will read the intro of the wikipedia page of your query.
* *"twitter"* will read the twitter trends for Los Angeles

## Setup

Clone the repo. Included are two json files *creds* and *client_secret*. *creds* stores API Keys for Dark Sky, Youtube, Twitter and Ivona which can been gotten at:

* [Dark Sky](https://darksky.net/dev/)
* [Youtube](https://console.developers.google.com/)
* [Twitter](https://dev.twitter.com/rest/public)
* [Ivona](https://www.ivona.com/)

*client_secret* contains API keys for google services (youtube not included) and can be gotten [here](https://console.developers.google.com/
).

When these files are populated with the relevant keys navigate to the relevant directory and run *ears.py*. 

## Library Dependencies

The following libraries will need to be installed before running Marvin:

* SpeechRecognition
* pyvona
* forecastio
* tweepy
* google-api-python-client

## Note
Marvin currently runs on Python 2.7. However, with some changes to urllib imports, can easily be made to run with Python3.
