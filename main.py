import tkinter as tk
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")

def get_weather(city):
    try:
        # URL and Request
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        weather = json.loads(response.text)
        
        # Parse Result
        location = weather['name']
        temp = weather['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        weather_desc = weather['weather'][0]['description']
        
        # Result String
        result = f"Location: {location}\nTemperature: {temp:.2f}°C\nWeather: {weather_desc}"
    
    except:
        result = "There was a problem retrieving the weather information."
    
    return result

def query_weather():
    city = city_entry.get()
    weather_result = get_weather(city)
    result_label.config(text=weather_result)


root = tk.Tk()

city_entry = tk.Entry(root, text="Enter city name", width=50)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weahter", command=query_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
