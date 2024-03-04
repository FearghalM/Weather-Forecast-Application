import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("WEATHER_APP_KEY")

user_city = input("Enter your city: ")

weather_request = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&units=metric&appid={api_key}")

weather_data = weather_request.json()['weather'][0]['main']
weather_temp = weather_request.json()['main']['temp']


#replace s with y to make it more readable
if weather_data[-1] == "s":
    weather_data = weather_data[:-1] + "y"

print(f"The weather in {user_city} is {weather_data} with a temperature of {weather_temp}C")