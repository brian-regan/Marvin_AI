import speech_recognition as sr
from time import sleep
import os
#from gtts import gTTS
#import pyglet
from get_creds import *
import pyvona


def speak_text(text):
	data = get_creds()['ivona']

	v = pyvona.create_voice(data['acc_key'], data['sec_key'])
	v.voice_name = "Brian"
	v.speak(text)


# not used
# def speak_text_old(text):
# 	tts = gTTS(text = text, lang = 'en')

# 	tts.save("speak.mp3")

# 	sound = pyglet.media.load('speak.mp3', streaming=False)
# 	sound.play()

# 	def exit_callback(dt):
# 	    pyglet.app.exit()

# 	pyglet.clock.schedule_once(exit_callback , sound.duration)

# 	pyglet.app.run()

# 	os.remove("speak.mp3")
