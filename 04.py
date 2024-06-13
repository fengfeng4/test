import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/data.csv")
df['Datetime'] = pd.to_datetime(df['Datetime'])

x_ticks = df['Datetime'][::6]

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Line plot for Temperature over Time
axs[0, 0].plot(df['Datetime'], df['Temperature (C)'], marker='o')
axs[0, 0].set_title('Temperature over Time')
axs[0, 0].set_xlabel('Datetime')
axs[0, 0].set_ylabel('Temperature (C)')
axs[0, 0].set_xticks(x_ticks)
axs[0, 0].tick_params(axis='x', rotation=45)
max_temp = df['Temperature (C)'].max()
max_temp_time = df.loc[df['Temperature (C)'] == max_temp, 'Datetime'].iloc[0]
axs[0, 0].annotate(f'Max Temp: {max_temp:.2f}C', xy=(max_temp_time, max_temp), 
             xytext=(max_temp_time, max_temp+2), 
             arrowprops=dict(facecolor='black', shrink=0.05))
axs[0, 0].grid(True, linestyle='--', linewidth=0.5)

# # Add line of best fit for Temperature over Time
s = np.polyfit(df['Datetime'].astype(np.int64) // 10**9, df['Temperature (C)'], 1)
p = np.poly1d(s)
axs[0, 0].plot(df['Datetime'], p(df['Datetime'].astype(np.int64) // 10**9), "r--")

# # Plot 2: Bar plot for Humidity over Time
axs[0, 1].bar(df['Datetime'], df['Humidity (%)'], color='skyblue')
axs[0, 1].set_title('Humidity over Time')
axs[0, 1].set_xlabel('Datetime')
axs[0, 1].set_ylabel('Humidity (%)')
axs[0, 1].set_xticks(x_ticks)
axs[0, 1].tick_params(axis='x', rotation=45)

# # Plot 3: Pie chart for Weather Description
weather_counts = df['Weather'].value_counts()
axs[1, 0].pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title('Weather Description Distribution')
axs[1, 0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# # Plot 4: Scatter plot for Temperature vs. Wind Speed
axs[1, 1].scatter(df['Temperature (C)'], df['Wind Speed (m/s)'], c='g', marker='o')
axs[1, 1].set_title('Temperature vs. Wind Speed')
axs[1, 1].set_xlabel('Temperature (C)')
axs[1, 1].set_ylabel('Wind Speed (m/s)')
axs[1, 1].grid(True)

# # Add line of best fit for Temperature vs. Wind Speed
s = np.polyfit(df['Temperature (C)'], df['Wind Speed (m/s)'], 1)
p = np.poly1d(s)
axs[1, 1].plot(df['Temperature (C)'], p(df['Temperature (C)']), "r--")

# # Adjust layout
plt.tight_layout()
plt.show()