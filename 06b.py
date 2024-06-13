import tkinter as tk
from tkinter import ttk
import pandas as pd
from openWeatherAPI import OpenWeatherAPI

def create_window():
    window = tk.Tk()
    window.title("WeatherVista Dashboard")
    window.geometry("600x400")
    
    # Add a label
    label = ttk.Label(window, text="WeatherVista Dashboard", font=("Arial", 16))
    label.pack(pady=20)
    
    # Add entry field for location
    location_label = ttk.Label(window, text="Enter Location:")
    location_label.pack(pady=5)
    location_entry = ttk.Entry(window)
    location_entry.pack(pady=5)

    # Add a button to fetch weather data
    def fecth_data():
        api = OpenWeatherAPI()
        if(api.fetch_weather_data(location_entry.get()) == -1):
            weather_data_label.config(text="error location name")
            return
        weather_data = api.current_df
        weather_info = f"Location: {weather_data['Location'].iloc[0]}\n"
        weather_info += f"Temperature: {weather_data['Temperature (C)'].iloc[0]:.1f} C\n"
        weather_info += f"Humidity: {weather_data['Humidity (%)'].iloc[0]}%\n"
        weather_info += f"Weather: {weather_data['Weather'].iloc[0]}"
        weather_data_label.config(text=weather_info)

    fetch_button = ttk.Button(window, text="Fetch Weather", command=fecth_data)
    fetch_button.pack(pady=10)

    # Add a label to display weather data
    weather_data_label = ttk.Label(window, text="", font=("Arial", 12))
    weather_data_label.pack(pady=20)
    
    window.mainloop()

create_window()