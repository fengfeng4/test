import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

df = pd.read_csv("data/data2.csv")
df['Date'] = pd.to_datetime(df['Date'])
def determine_weather(row):
    if row['Max Temperature (C)'] > 25:
        return 'Sunny'
    elif row['Min Temperature (C)'] < 15 and row['Max Humidity (%)'] > 80:
        return 'Rainy'
    else:
        return 'Partly Cloudy'

# Add a 'Weather' column to the dataframe
df['Weather'] = df.apply(determine_weather, axis=1)
df.to_csv("data/data3.csv")

random_row = df.sample(n=1).iloc[0]
def create_forecast_card(ax, date, high_temp, low_temp, weather):
    # Background color based on weather
    if weather == 'Sunny':
        bg_color = 'gold'
    elif weather == 'Partly Cloudy':
        bg_color = 'lightgrey'
    elif weather == 'Rainy':
        bg_color = 'lightblue'
    
    # Create a rectangle patch for the background color
    rect = patches.Rectangle((0, 0), 1, 1, transform=ax.transAxes, color=bg_color, zorder=0)
    ax.add_patch(rect)

    ax.axis('off')  # Hide axes

    # Display date
    ax.text(0.5, 0.8, date.strftime('%Y-%m-%d'), fontsize=12, ha='center', va='center')

    # Display high temperature5
    ax.text(0.5, 0.6, f'High: {high_temp:.1f}C', fontsize=10, ha='center', va='center', color='red')

    # Display low temperature
    ax.text(0.5, 0.4, f'Low: {low_temp:.1f}C', fontsize=10, ha='center', va='center', color='blue')

    # Display weather condition
    ax.text(0.5, 0.2, weather, fontsize=10, ha='center', va='center')

fig, ax = plt.subplots(figsize=(3, 4))
create_forecast_card(ax, random_row['Date'], random_row['Max Temperature (C)'], random_row['Min Temperature (C)'], random_row['Weather'])

plt.tight_layout()
plt.show()
