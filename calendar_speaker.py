from print_speek import *
import google_calendar

def main():
	list = google_calendar.main()
	for item in list:
		speak_text(item)