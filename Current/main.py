import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("WEATHER_APP_KEY")

user_city = input("Enter your city: ")

weather_request = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&units=metric&appid={api_key}")

weather_data = weather_request.json()['weather'][0]['main']
weather_temp = weather_request.json()['main']['temp']

# turns "clouds" into "Cloudy" for better readability
if weather_data == "Clouds":
    weather_data = "Cloudy"

print(f"The weather in {user_city} is {weather_data} with a temperature of {weather_temp}C")