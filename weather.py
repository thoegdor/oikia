import requests
from pprint import pprint
from helper import D

API_key = D['weather_API_key']
base_url = "https://api.openweathermap.org/data/2.5/forecast?"

city_zip = "06511"
 
final_url = base_url + "appid=" + API_key + "&zip=" + city_zip + ",us"

weather_data = requests.get(final_url).json()

pprint(weather_data)