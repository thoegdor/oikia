import requests
from pprint import pprint
import datetime
from helper import D


API_key = D['weather_API_key']
base_url = "https://api.openweathermap.org/data/2.5/forecast?"

city_zip = D['weather_zip']
 
final_url = base_url + "appid=" + API_key + "&zip=" + city_zip + ",us"

weather_data = requests.get(final_url).json()

# need to parse that bad boy
# first eight entries correspond to current date
# just going to make a decent ascii table for printing to command line for now

# cols: time, humidity, temp(f), desc

# need a kelvin converter

def kelvin_to_fahr(temp_in_k):
    f = ((temp_in_k - 273.15) * 9)/5 + 32
    return round(f,2)

weather_list = weather_data['list']
container_list = [['datetime','humidity','temp(f)','desc']]

for h in range(0,9):
    # get vals, then stuff
    dtime = weather_list[h]['dt_txt']
    humidity = weather_list[h]['main']['humidity']
    temp = kelvin_to_fahr(weather_list[h]['main']['temp'])
    desc = weather_list[h]['weather'][0]['description']
    row = [dtime,humidity,temp,desc]
    container_list.append(row)
    
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

pprint(container_list)


