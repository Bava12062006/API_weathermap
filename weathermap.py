import requests
import matplotlib.pyplot as plt

# Step 1: Set up OpenWeatherMap API
API_KEY = "a330de032c998e78ab830a78197a86da"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Step 2: Get city name from user
city_name = input("Enter the city name: ")

try:
    # Fetch weather data from API
    params = {
        "q": f"{city_name},IN",  # Add country code for better accuracy
        "appid": API_KEY,
        "units": "metric",  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise exception for HTTP errors
    weather_data = response.json()

    # Extract weather data
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]
    weather_condition = weather_data["weather"][0]["description"]
    city_name = weather_data["name"]

    # Step 3: Plot the weather data using Matplotlib
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [temperature, humidity, pressure]

    # Create a bar chart
    plt.bar(labels, values, color=['blue', 'green', 'orange'])

    # Add title and labels
    plt.title(f"Weather in {city_name}")
    plt.xlabel("Weather Parameters")
    plt.ylabel("Values")
    
    # Show the plot
    plt.show()

    # Display the weather details
    print(f"Weather in {city_name}:")
    print(f"Condition: {weather_condition.capitalize()}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")

except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except KeyError:
    print(f"City '{city_name}' not found. Please check the city name and try again.")
