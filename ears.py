import speech_recognition as sr
from time import sleep

import news_reader
import news_memory
from print_speek import *
from news_cleaner import *
import calendar_speaker
import forcast_brain
import google_gmail
import movie_search
import twitter_brain
import wikipedia_brain
#import youtube_brain (in development)

outlets = news_memory.main()

launch_phrase = "hello marvin"

def listen():
	global woken

	r = sr.Recognizer()
	m = sr.Microphone()
	speech = ""
	with m as source:
		if woken == False:
			print("Calibrating for background noise...")
	    		r.adjust_for_ambient_noise(source)

	with m as source:
	    print("Listening...")
	    audio = r.listen(source)
	
	try:
	    # recognize speech using Google Speech Recognition
	    speech = r.recognize_google(audio)
	    print("You said {}".format(speech))
	    if woken == False:
	    	awaken(speech.lower())
	    else:
	    	respond(speech.lower())
	except sr.UnknownValueError:
	    print("Oops! Didn't catch that")
	except sr.RequestError as e:
	    print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
	    return speech

def awaken(message):
	if launch_phrase in message:
		global woken
		woken =  True
		speak_text("Hello sir, how can I help?")

def respond(instruction):
	global woken
	if "news" in instruction:
		source = instruction.replace("news ", "", 1)
		

		cleaned_source = news_cleaner(source)
		print("source:" + cleaned_source['name'])
		speech = news_reader.reader(cleaned_source['idn'])
		speak_text(u"News from {0}".format(cleaned_source['name']))
		for sentance in speech:
			speak_text(sentance)

	
	elif "calendar" in instruction:
		calendar_speaker.main()

	elif "weather" in instruction:
		say = forcast_brain.get_weather()
		speak_text(say)
	elif "email" in instruction:
		speechs = google_gmail.Say_Messages()
		for say in speechs:
			speak_text(say)
	elif "movie" in instruction:
		query = instruction.split("movie ")[1]
		say = movie_search.omdb(query)
		speak_text(say)

	elif "wiki" in instruction:
		query = instruction.split("wiki ")[1]
		wiki_out = wikipedia_brain.search_wiki(query)
		say = u"Wikipedia results for {0}: {1}".format(wiki_out['title'], wiki_out['extract'])
		speak_text(say)

	elif "twitter" in instruction:
		trends = twitter_brain.trends(34.0522, -118.2437)
		say = movie_search.read_list(trends)
		speak_text("Currently Trending: " + say)

	# music in development
	# elif "music" in instruction:
	# 	query = instruction.split("music ")[1]
	# 	youtube_brain.play(query)

	woken = False




woken = False
while True:
	listen()

