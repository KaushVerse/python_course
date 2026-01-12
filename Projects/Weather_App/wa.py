# 🌦️ Weather App
# By Kaushik 🚀

import requests

# 🏷️ OpenWeatherMap API Key (Get free key from https://openweathermap.org/api)
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        print(f"\n🌤️ Weather in {city_name}, {country}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌥️ Condition: {weather_desc}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s\n")
    else:
        print("⚠️ City not found or API error!")

def main():
    print("🌦️ Welcome to Python Weather App!")
    while True:
        city = input("🏙️ Enter city name (or 'q' to quit): ")
        if city.lower() == 'q':
            print("👋 Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
