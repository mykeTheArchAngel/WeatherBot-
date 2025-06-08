import requests

API_KEY = "YOUR_API_KEY"  # Replace with your actual key

def get_emoji(condition_id):
    """Return appropriate emoji based on weather condition ID"""
    # Thunderstorm
    if 200 <= condition_id < 300:
        return '⛈️'
    # Drizzle
    elif 300 <= condition_id < 500:
        return '🌧️'
    # Rain
    elif 500 <= condition_id < 600:
        return '🌧️'
    # Snow
    elif 600 <= condition_id < 700:
        return '❄️'
    # Atmosphere (Fog, Mist, etc)
    elif 700 <= condition_id < 800:
        return '🌫️'
    # Clear
    elif condition_id == 800:
        return '☀️'
    # Clouds
    elif 801 <= condition_id <= 804:
        if condition_id == 801:
            return '🌤️'  # Few clouds
        elif condition_id == 802:
            return '⛅'   # Scattered clouds
        else:
            return '☁️'   # Broken or overcast clouds
    # Extreme conditions
    elif condition_id >= 900:
        return '⚠️'
    # Default
    return '🌍'

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        condition_id = data['weather'][0]['id']
        
        return {
            'city': data['name'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'].title(),
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'emoji': get_emoji(condition_id)
        }
        
    except requests.exceptions.RequestException as e:
        print(f"🚫 Error: {str(e)}")
        return None

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    
    if weather:
        print(f"\n{weather['emoji']} Weather in {weather['city']}:")
        print(f"  Temperature: {weather['temp']}°C")
        print(f"  Feels like: {weather['feels_like']}°C")
        print(f"  Conditions: {weather['description']}")
        print(f"  Humidity: {weather['humidity']}%")
        print(f"  Wind: {weather['wind']} m/s")

if __name__ == "__main__":
    main()
