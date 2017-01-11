#youtube_brain.py

#!/usr/bin/python

from apiclient.discovery import build

import pafy
import vlc


import logging
from get_creds import *

#logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.


def youtube_search(query):

  data = get_creds()['youtube']

  DEVELOPER_KEY = data['key']
  YOUTUBE_API_SERVICE_NAME = "youtube"
  YOUTUBE_API_VERSION = "v3"

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY,cache_discovery=False)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q= query,
    part="id,snippet",
    maxResults= 1
  ).execute()

  videos = []

  

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result["id"]["videoId"])

  url = "https://www.youtube.com/watch?v={0}".format(videos[0])
  print(url)
  return(url)


def streamer(url):
	vid = pafy.new(url)
	stream = vid.getbestaudio()
	global p
	p = vlc.MediaPlayer(stream.url)
	p.play()


def play(query):

  url = youtube_search(query)
  streamer(url)
  while True:
    pass