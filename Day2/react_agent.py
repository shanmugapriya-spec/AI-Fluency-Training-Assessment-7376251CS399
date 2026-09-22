from tools import get_weather


def react_agent():
    print("=== ReACT AGENT ===")

    question = "What is the current weather in Coimbatore?"

    print("Question:", question)

    # Thought
    print("\nThought:")
    print("I need current weather information, so I should use a weather tool.")

    # Action
    print("\nAction:")
    print("Calling get_weather('Coimbatore')...")

    weather = get_weather("Coimbatore")

    # Observation
    print("\nObservation:")

    if "error" in weather:
        print("Unable to get weather information.")
        print("Error:", weather["error"])
        return

    print("City:", weather["city"])
    print("Temperature:", weather["temperature"], "°C")
    print("Humidity:", weather["humidity"], "%")
    print("Weather code:", weather["weather_code"])

    # Final answer
    print("\nFinal Answer:")
    print(
        f"The current temperature in {weather['city']} is "
        f"{weather['temperature']} °C with "
        f"{weather['humidity']}% humidity."
    )


if __name__ == "__main__":
    react_agent()