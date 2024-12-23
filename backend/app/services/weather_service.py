import requests

def get_weather_data(location: str) -> dict:
    api_key = "your_api_key"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    return response.json()
