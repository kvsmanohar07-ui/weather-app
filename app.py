import streamlit as st
import requests

st.title("🌦️ Weather App - Live")
st.write("Made by K.V.S. Manohar Reddy | OASIS INFOBYTE - Task 4")
# User city type cheyali - 【entity-OASIS¦canonical_name=OASIS】 rule
city = st.text_input("Enter city name:", "Tirupati")

if st.button("Get Weather"):
    # 1. Empty validation
    if not city.strip():
        st.error("Please enter a city name!")
    else:
        try:
            # 2. City name -> lat, lon (Geocoding API - Free)
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
            geo_res = requests.get(geo_url, timeout=10).json()

            if "results" not in geo_res:
                st.error(f"City not found: {city}. Please check spelling!")
            else:
                lat = geo_res["results"][0]["latitude"]
                lon = geo_res["results"][0]["longitude"]
                real_name = geo_res["results"][0]["name"]

                # 3. Live Weather API
                url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m"
                data = requests.get(url, timeout=10).json()
                curr = data["current"]

                temp_c = curr["temperature_2m"]
                temp_f = (temp_c * 9/5) + 32
                humidity = curr["relative_humidity_2m"]
                feels = curr["apparent_temperature"]
                wind = curr["wind_speed_10m"]
                code = curr["weather_code"]

                if code == 0:
                    condition = "☀️ Clear Sky"
                elif code in [1, 2, 3]:
                    condition = "⛅ Cloudy"
                elif code in [45, 48]:
                    condition = "🌫️ Foggy"
                elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
                    condition = "🌧️ Rainy"
                elif code in [95, 96, 99]:
                    condition = "⛈️ Thunderstorm"
                else:
                    condition = "🌤️ Partly Cloudy"

                st.success(f"{real_name}: {temp_c}°C / {temp_f:.1f}°F, {condition}")
                st.write(f"Feels like: {feels}°C")
                st.write(f"Humidity: {humidity}%")
                st.write(f"Wind Speed: {wind} km/h")

        except Exception:
            st.error("Network error! Please check internet and try again.")
