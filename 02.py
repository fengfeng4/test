import requests
import pandas as pd

class OpenWeatherAPI:
    api_key =None
    row_data = None
    dataframe = None
    def __init__(self, api_key):
        self.api_key = api_key
    def fetch_weather_data(self, location):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            self.row_data = response.json()
            temp = []
            for entry in self.row_data["list"]:
                temp.append({
                    'Datetime': pd.to_datetime(entry['dt'], unit='s'),
                    'Temperature (C)': entry['main']['temp'] - 273.15,
                    'Humidity (%)': entry['main']['humidity'],
                    'Wind Speed (m/s)': entry['wind']['speed'],
                    'Weather': entry['weather'][0]['description']
                })
            self.dataframe = pd.DataFrame(temp)
            return self.dataframe
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
    def to_csv(self, path):
        self.dataframe.to_csv(path, index=False)

api = OpenWeatherAPI('2dd249caf078aec871ab451b46fee0a1')
data = api.fetch_weather_data('Shenzhen')
api.to_csv("data/data.csv")

def calculate_daily_stats(df_forecast):
    
    # Extract the date from the 'Datetime' column and create a new 'Date' column
    df_forecast['Date'] = df_forecast['Datetime'].dt.date

    # Group the data by the 'Date' column and calculate the min and max for each group
    daily_stats = df_forecast.groupby('Date').agg({
        'Temperature (C)': ['min', 'max'],
        'Humidity (%)': ['min', 'max'],
        'Wind Speed (m/s)': ['min', 'max']
    })

    # Flatten the MultiIndex columns
    daily_stats.columns = ['Min Temperature (C)', 'Max Temperature (C)', 
                           'Min Humidity (%)', 'Max Humidity (%)', 
                           'Min Wind Speed (m/s)', 'Max Wind Speed (m/s)']
    
    # Reset the index to turn the 'Date' back into a column
    daily_stats.reset_index(inplace=True)
    
    return daily_stats

# Calculate and save daily statistics to CSV
daily_stats = calculate_daily_stats(api.dataframe)
daily_stats.to_csv("data/data2.csv")
# print(daily_stats.head())
