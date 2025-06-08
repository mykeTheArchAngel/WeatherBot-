Step-by-Step Explanation:

    API Setup:

        We use OpenWeatherMap's free API (sign up at openweathermap.org to get an API key)

        BASE_URL is the endpoint for current weather data

        units=metric converts temperatures to Celsius

    User Input:

        The bot asks for a city name through standard input

    API Request:

        Constructs the complete request URL with city and API key

        Uses requests library to send HTTP GET request

    Response Handling:

        Checks if response is successful (status code 200)

        Converts JSON response to Python dictionary

        Extracts temperature, weather description, and humidity

    Error Handling:

        Catches network errors with try/except

        Handles invalid city names through status code checking

    Output:

        Formats and displays the weather information in readable format

To Use This Bot:

    Install Python if not already installed

    Install requests library: pip install requests

    Get free API key from OpenWeatherMap

    Replace "YOUR_API_KEY" with your actual key

    Run the script
