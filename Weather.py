import requests
import json

class WeatherForecast:
    def __init__(self, location):
        self.location = location

    def get_weather(self):
        api_key = "YOUR_API_KEY"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.location}&appid={api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    def get_temperature(self):
        data = self.get_weather()
        temperature = data["main"]["temp"]
        temperature_celsius = round(temperature - 273.15, 2)
        return temperature_celsius

    def get_description(self):
        data = self.get_weather()
        description = data["weather"][0]["description"]
        return description

def main():
    location = "San Francisco"
    weather_forecast = WeatherForecast(location)
    temperature = weather_forecast.get_temperature()
    description = weather_forecast.get_description()
    print(f"The temperature in {location} is {temperature}°C and the weather is {description}.")

if __name__ == "__main__":
    main()
