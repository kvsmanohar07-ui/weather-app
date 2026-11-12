import streamlit as st

st.title("Weather App")
st.write("Made by K.V.S. Manohar Reddy - Weather in your city!")

weather_data = {
    "Hyderabad": ("32°C, Sunny, Humidity 45%", "Wind: 10 km/h, Condition: Clear Sky"),
    "Tirupati": ("33°C, Sunny, Humidity 50%", "Wind: 12 km/h, Condition: Hot and Sunny"),
    "Chennai": ("31°C, Cloudy, Humidity 70%", "Wind: 15 km/h, Condition: Cloudy"),
    "Bangalore": ("26°C, Rainy, Humidity 80%", "Wind: 8 km/h, Condition: Light Rain"),
    "Delhi": ("28°C, Foggy, Humidity 60%", "Wind: 6 km/h, Condition: Foggy Morning"),
    "Mumbai": ("30°C, Humid, Humidity 75%", "Wind: 18 km/h, Condition: Humid"),
}

city = st.selectbox("Choose your city?", list(weather_data.keys()))

if st.button("Show Weather"):
    main, wind = weather_data[city]
    st.success(f"{city}: {main}")
    st.write(wind)
