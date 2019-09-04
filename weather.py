import requests
from pprint import pprint
import datetime
from helper import D

def weather_reporter(D):

    API_key = D['weather_API_key']
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    city_zip = D['weather_zip']
    final_url = base_url + "appid=" + API_key + "&zip=" + city_zip + ",us"
    weather_data = requests.get(final_url).json()

    # need to parse that bad boy
    # print cols: time, humidity, temp(f), desc + emoji
    
    def kelvin_to_fahr(temp_in_k):
        f = ((temp_in_k - 273.15) * 9)/5 + 32
        return round(f,2)
    
    #desc_emoji_dict = {
    #    "moderate rain":u'\U0001F327',
    #    "light rain":u'\U0001F327',
    #    "clear sky":u'\U0001F31D',
    #    "broken clouds":u'U0001F324',
    #    "overcast clouds":u'U0001F325'
    #}

    weather_list = weather_data['list']
    container_list = [['datetime','humidity','temp(f)','desc']]

    for h in range(0,9): # 24 hours of entries
        # get vals, then stuff
        dtime = weather_list[h]['dt_txt']
        humidity = weather_list[h]['main']['humidity']
        temp = kelvin_to_fahr(weather_list[h]['main']['temp'])
        desc = weather_list[h]['weather'][0]['description']
        #emoji = desc_emoji_dict[desc]
        row = [dtime,humidity,temp,desc]
        container_list.append(row)
    
    return(container_list) # add zip in here somewhere

#pprint(weather_reporter(D))
