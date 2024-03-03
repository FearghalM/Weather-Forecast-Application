import os
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap
from dotenv import load_dotenv

load_dotenv()


# Function to get the weather information using the OpenWeatherMap API
def get_weather(user_city):
    api_key = os.getenv("WEATHER_APP_KEY")
    weather_request = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&units=metric&appid={api_key}")

    # If the city is not found
    if weather_request.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    #parse the json response
    weather_data = weather_request.json()
    icon_id = weather_data['weather'][0]['icon']
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    city_name = weather_data['name']
    country_name = weather_data['sys']['country']

    # get the weather icon URL and return the weather information
    icon_url = f"http://openweathermap.org/img/w/{icon_id}.png"
    return (icon_url, temperature, description, city_name, country_name)

# Function to search for the weather information
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # if the city is found, update the labels with the weather information
    icon_url, temperature, description, city_name, country_name = result
    location_label.configure(text=f"{city_name}, {country_name}")

    # get the weather icon from the URL
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # update the temperature and description labels
    temp_label.configure(text=f"{temperature:.2f}°C")
    desc_label.configure(text=f"Description: {description}")


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

# Entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Arial 14")
city_entry.pack(pady=10)

# Button widget -> to search for the weather information
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# label widget -> to display the city/country name
location_label = tk.Label(root, font="Arial 20")
location_label.pack(pady=20)

# Label widget -> to display the weather icon
icon_label = tk.Label(root, font="Arial 14")
icon_label.pack()

# Label widget -> to display the temperature
temp_label = tk.Label(root, font="Arial 18")
temp_label.pack()

# Label widget -> to display the weather description
desc_label = tk.Label(root,font="Arial 14")
desc_label.pack()

root.mainloop()