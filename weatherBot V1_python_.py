import requests

def weather_bot():
    # Get API key from OpenWeatherMap (free tier)
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    # Get city input from user
    city = input("Enter city name: ")
    
    # Create request URL
    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    try:
        # Send request to weather API
        response = requests.get(request_url)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant weather information
            temperature = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            
            # Display results
            print(f"\nCurrent weather in {city}:")
            print(f"- Temperature: {temperature}°C")
            print(f"- Conditions: {weather_desc.capitalize()}")
            print(f"- Humidity: {humidity}%")
            
        else:
            print("City not found. Please try again.")
    
    except requests.exceptions.RequestException:
        print("Error connecting to weather service. Check your internet connection.")

# Run the bot
weather_bot()