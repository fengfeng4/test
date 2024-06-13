import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from openWeatherAPI import OpenWeatherAPI
import weather_plots as wp 

def update_weather():
    api = OpenWeatherAPI()
    result = api.fetch_weather_data(city_var.get())
    if(result == -1):
        return
    current_df, hourly_df, daily_df  = result

    for widget in plot_frame.winfo_children():
        widget.destroy()
    
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    fig.tight_layout(pad=5.0)

    # Generate plots
    wp.create_forecast_card(axs[0], daily_df.iloc[0]['Date'], daily_df.iloc[0]['Max Temperature (C)'], daily_df.iloc[0]['Min Temperature (C)'], daily_df.iloc[0]['Weather'])
    wp.plot_scatter(hourly_df, 'Temperature (C)', 'Wind Speed (m/s)', axs[1], title="Wind Speed vs Temperature")
    wp.plot_min_max(daily_df, 'Date', 'Min Temperature (C)', 'Max Temperature (C)', axs[2], title="Daily Min/Max Temperature")

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Dashboard")

# Create a frame for the controls
control_frame = ttk.Frame(root, padding="10")
control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Create a frame for the plots
plot_frame = ttk.Frame(root, padding="10")
plot_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Dropdown for city selection
city_var = tk.StringVar(value='Sydney')
city_dropdown = ttk.Combobox(control_frame, textvariable=city_var, values=['Sydney', 'New York', 'London', 'Beijing'])
city_dropdown.grid(row=0, column=0, padx=5, pady=5)

# Button to fetch and update weather data
update_button = ttk.Button(control_frame, text="Update Weather", command=update_weather)
update_button.grid(row=0, column=1, padx=5, pady=5)

# Configure row and column weights
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
plot_frame.grid_rowconfigure(0, weight=1)
plot_frame.grid_columnconfigure(0, weight=1)

# Initialize the weather data
update_weather()

# Start the Tkinter event loop
root.mainloop()