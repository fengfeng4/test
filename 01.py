import requests
import pandas as pd

global api_key
global location

def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
    

api_key = '2dd249caf078aec871ab451b46fee0a1'
location = 'Shenzhen'
data = fetch_weather_data()
print(data)