import requests
import os
from dotenv import load_dotenv

load_dotenv()

##ip api
## url link to api https://ip-api.com/docs/api:json
def call_ip_api():
    ## grab source
    source = f'http://ip-api.com/json/'

    response = requests.get(source)
    curr_user_data = {}
    if response.status_code == 200:
        data = response.json()

        if "country" in data:
            curr_user_data['country'] = data['country']
        if 'city' in data:
            curr_user_data['city'] = data['city']
        if 'zip' in data:
            curr_user_data['zip'] = data['zip']
        if 'query' in data:
            curr_user_data['ip_adress'] = data['query']
        if 'countryCode' in data:
            curr_user_data['countryCode'] = data['countryCode']
        if 'lat' in data:
            curr_user_data['lat'] = data['lat']
        if 'lon' in data:
            curr_user_data['lon'] = data['lon']
    else:
        requests.status_codes == 404

    return curr_user_data

## openweather

def call_openweather_api():
    weather_data = {}
    userData = call_ip_api()
    lat = userData['lat']
    lon = userData['lon']
    openWeather_api_key = os.getenv('OPEN_WEATHER_API_KEY')

    openWeather_api_source = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openWeather_api_key}'

    response = requests.get(openWeather_api_source)
    if response.status_code == 200:
        data = response.json()

        for data in data['weather']:
            if 'main' in data:
                weather_data['main'] = data['main']
            if 'description' in data:
                weather_data['description'] = data['description']
            if 'icon' in data:
                weather_data['icon'] = data['icon']
    else:
        return "Weather API call failed"

    return weather_data
        
call_openweather_api()
