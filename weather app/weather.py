import requests

API_KEY = "5fd1f170ea6e39e174f4da4a2c56b85b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" # Change to "imperial" for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city}:")
        print(f"Condition: {weather.capitalize()}")
        print(f"Temperature: {temp}^C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not Found! Please enter a valid city name.")

def main():
    print("Welcome to the Weather App!")
    while True:
        city = input("Enter city name (or type 'quit' to exit): ").strip()
        if city.lower() == "quit":
            print("Exiting... Stay Safe!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()                    