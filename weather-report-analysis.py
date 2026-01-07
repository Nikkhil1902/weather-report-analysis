import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather-1.csv")

print(df.head())
print(df.info())

df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

print(df.isnull().sum())

avg_temp_state = df.groupby('State/UT')['Temperature (°C)'].mean()
avg_temp_state = avg_temp_state.sort_values(ascending=False)
print(avg_temp_state)

plt.figure()
avg_temp_state.head(10).plot(kind='bar')
plt.xlabel("State")
plt.ylabel("Average Temperature (°C)")
plt.title("Top 10 States by Average Temperature")
plt.show()

condition_count = df['Condition'].value_counts()
print(condition_count)

plt.figure()
condition_count.plot(kind='bar')
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.title("Weather Conditions Distribution")
plt.show()

avg_humidity = df.groupby('State/UT')['Humidity (%)'].mean()
avg_humidity = avg_humidity.sort_values(ascending=False)
print(avg_humidity)

plt.figure()
avg_humidity.head(10).plot(kind='bar')
plt.xlabel("State")
plt.ylabel("Average Humidity (%)")
plt.title("Top 10 States by Humidity")
plt.show()

avg_wind = df.groupby('State/UT')['Wind Speed (km/h)'].mean()
avg_wind = avg_wind.sort_values(ascending=False)
print(avg_wind)

plt.figure()
avg_wind.head(10).plot(kind='bar')
plt.xlabel("State")
plt.ylabel("Average Wind Speed (km/h)")
plt.title("Top 10 States by Wind Speed")
plt.show()

hottest_place = df.loc[df['Temperature (°C)'].idxmax()]
coldest_place = df.loc[df['Temperature (°C)'].idxmin()]

print(hottest_place)
print(coldest_place)
