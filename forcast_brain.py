# forcast puller 
import forecastio
from print_speek import *
from get_creds import *

def get_weather():

	data = get_creds()['forecastio']
	
	api_key = data['key']
	lat = data['lat']
	lng = data['lng']

	forecast = forecastio.load_forecast(api_key, lat, lng)
	daily = forecast.daily()
	weather = daily.summary

	speech = "In university the weather will be " + weather
	return(speech)
