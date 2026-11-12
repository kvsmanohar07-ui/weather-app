import streamlit as st
import requests

st.title("🌦️ Weather App - Live")
st.write("Made by K.V.S. Manohar Reddy - Live weather in your city!")

# City -> lat, lon for Open-Meteo API
cities = {
    "Tirupati": (13.6288, 79.4192),
    "Hyderabad": (17.3850, 78.4867),
    "Chennai": (13.0827, 80.2707),
    "Bangalore": (12.9716, 77.5946),
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777),
}

city = st.selectbox("Choose your city?", list(cities.keys()))

if st.button("Show Live Weather"):
    lat, lon = cities[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m"
    
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        curr = data["current"]

        temp = curr["temperature_2m"]
        humidity = curr["relative_humidity_2m"]
        feels = curr["apparent_temperature"]
        wind = curr["wind_speed_10m"]
        code = curr["weather_code"]

        # Simple weather code to text
        if code == 0:
            condition = "☀️ Clear Sky"
        elif code in [1, 2, 3]:
            condition = "⛅ Cloudy"
        elif code in [45, 48]:
            condition = "🌫️ Foggy"
        elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
            condition = "🌧️ Rainy"
        elif code in [71, 73, 75, 77, 85, 86]:
            condition = "❄️ Snowy"
        elif code in [95, 96, 99]:
            condition = "⛈️ Thunderstorm"
        else:
            condition = "🌤️ Partly Cloudy"

        st.success(f"{city}: {temp}°C, {condition}")
        st.write(f"Feels like: {feels}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Wind: {wind} km/h")

    except Exception as e:
        st.error("Could not fetch live weather. Check internet and try again.")
