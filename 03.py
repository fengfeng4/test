import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/data.csv")
df["Datetime"] = pd.to_datetime(df["Datetime"])
x_ticks = df['Datetime'][::6]

# weather_counts = df['Weather'].value_counts()
# plt.figure(figsize=(8, 8))
# plt.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%')
# plt.title('Weather Description Distribution')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.scatter(df['Temperature (C)'], df['Wind Speed (m/s)'], c='g', marker='o')
# plt.title('Temperature vs. Wind Speed')
# plt.xlabel('Temperature (C)')
# plt.ylabel('Wind Speed (m/s)')
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(df['Datetime'], df['Temperature (C)'], marker='o', linestyle='--', color='b')
# plt.bar(df['Datetime'], df['Temperature (C)'], color='skyblue')
# plt.title('Temperature over Time')
# plt.xlabel('Datetime')
# plt.ylabel('Temperature (C)')
# plt.xticks(ticks=x_ticks, rotation=45)
# plt.grid(True)

# # Annotate the highest temperature
# max_temp = df['Temperature (C)'].max()
# max_temp_time = df.loc[df['Temperature (C)'] == max_temp, 'Datetime'].iloc[0]
# plt.annotate(f'Max Temp: {max_temp:.2f}C', xy=(max_temp_time, max_temp), 
#              xytext=(max_temp_time, max_temp+2), 
#              arrowprops=dict(facecolor='black', shrink=0.05))

# plt.show()