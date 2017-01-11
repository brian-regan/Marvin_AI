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
* *"twitter" will read the twitter trends for Los Angeles
