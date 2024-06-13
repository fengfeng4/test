import requests
import pandas as pd

def determine_weather(row, sunny_threshold, rainy_min_temp_threshold, rainy_humidity_threshold):
    if row['Max Temperature (C)'] > sunny_threshold:
        return 'Sunny'
    elif row['Min Temperature (C)'] < rainy_min_temp_threshold and row['Max Humidity (%)'] > rainy_humidity_threshold:
        return 'Rainy'
    else:
        return 'Partly Cloudy'

class OpenWeatherAPI:
    api_key =None
    current_data = None
    forecast_data = None
    current_df = None
    forecast_df = None
    daily_df = None
    def __init__(self, api_key = "2dd249caf078aec871ab451b46fee0a1"):
        self.api_key = api_key
    def request(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    def fetch_weather_data(self, location):
        '''
        return self.current_df, self.forecast_df,self.daily_df, 
        if error, return -1
        '''

        self.current_data = self.request(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}")
        if(self.current_data == None):return -1
        self.current_df = {
                "Location": self.current_data["name"],
                "Temperature (C)": round(self.current_data["main"]["temp"]-273.15, 1),
                "Humidity (%)": self.current_data["main"]["humidity"],
                "Weather": self.current_data["weather"][0]["description"]
        }
        self.current_df= pd.DataFrame([self.current_df])


        self.forecast_data = self.request(f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={self.api_key}")
        if(self.forecast_data == None):return -1
        temp = []
        for entry in self.forecast_data["list"]:
            temp.append({
                'Datetime': pd.to_datetime(entry['dt'], unit='s'),
                'Temperature (C)': round(entry['main']['temp'] - 273.15, 1),
                'Humidity (%)': entry['main']['humidity'],
                'Wind Speed (m/s)': entry['wind']['speed'],
                'Weather': entry['weather'][0]['description']
            })
        self.forecast_df = pd.DataFrame(temp)


        self.forecast_df['Date'] = self.forecast_df['Datetime'].dt.date
        self.daily_df = self.forecast_df.groupby('Date').agg({
            'Temperature (C)': ['min', 'max'],
            'Humidity (%)': ['min', 'max'],
            'Wind Speed (m/s)': ['min', 'max']
        })
        self.daily_df.columns = ['Min Temperature (C)', 'Max Temperature (C)', 
                            'Min Humidity (%)', 'Max Humidity (%)', 
                            'Min Wind Speed (m/s)', 'Max Wind Speed (m/s)']
        self.daily_df.reset_index(inplace=True)
        self.daily_df['Weather'] = self.daily_df.apply(determine_weather, axis=1, args=(25, 15, 80))

        return self.current_df, self.forecast_df,self.daily_df
