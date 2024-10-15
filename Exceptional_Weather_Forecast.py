def fahrenheit_to_celsius(fahrenheit):
    try:
        # Attempt to convert the Fahrenheit temperature to Celsius
        celsius = (fahrenheit - 32) * 5 / 9
        return round(celsius, 2)
    except TypeError:
        # Handle the case where the input is not a number
        return "Invalid input. Please enter a numeric temperature."
    else:
        # Executed if there is no exception in the try block
        print(f"Converted temperature: {fahrenheit}°F to {round((fahrenheit - 32) * 5 / 9, 2)}°C")
    finally:
        # This block runs whether an exception occurs or not
        print("Temperature conversion process complete.")

def get_weather_forecast(city):
    # A simple mock forecast for demonstration purposes
    mock_forecasts = {
        "new york": {"temp_f": 72, "condition": "Sunny"},
        "london": {"temp_f": 65, "condition": "Cloudy"},
        "tokyo": {"temp_f": 78, "condition": "Clear"},
    }

    try:
        # Attempt to retrieve the forecast for the specified city
        forecast = mock_forecasts[city.lower()]
        temp_f = forecast['temp_f']
        temp_c = fahrenheit_to_celsius(temp_f)
        condition = forecast['condition']

        # Return the formatted weather forecast
        return f"Weather in {city.title()}: {temp_f}°F ({temp_c}°C), {condition}"
    
    except KeyError:
        # Handle the case where the city is not found
        return "Sorry, weather data for that city is not available."
    finally:
        # This block runs after every attempt, regardless of success
        print("Thank you for using the Weather Forecast App!")

def main():
    print("Welcome to the Weather Forecast App!")
    
    while True:
        city = input("Enter a city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get the weather forecast and print it
        forecast = get_weather_forecast(city)
        print(forecast)

# Run the program
if __name__ == "__main__":
    main()