#This script is used to gather weather data from OpenWeatherMap API
# For using this script you need to have a CSV file with the following columns:
# latitude, longitude
#The data is then stored in a CSV file with the following columns:
# latitude, longitude, Temperature, Humidity, Pressure
import requests
import time
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Define a function to retrieve weather data for a given location
def get_weather_data(latitude, longitude, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        time.sleep(1.2)
        return temperature, humidity, pressure
    else:
        print(f'Error retrieving data for ({latitude}, {longitude}): {response.status_code}')


# Retrieve weather data for each location and create new columns in the DataFrame
api_key = 'YOUR_API_KEY_OF_OPENWEATHERMAP'
df[['Temperature', 'Humidity', 'Pressure']] = df.apply(lambda row: pd.Series(get_weather_data(row['latitude'], row['longitude'], api_key)), axis=1)
df.to_csv('data.csv', index=False)