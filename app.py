import streamlit as st

st.title("Weather App")
st.write("Made by K.V.S. Manohar Reddy - Weather in your city!")

city = st.selectbox("Choose your city?", ["Hyderabad", "Tirupati", "Chennai", "Bangalore", "Delhi", "Mumbai"])

if st.button("Show Weather"):
    if city == "Hyderabad":
        st.success("Hyderabad: 32°C, Sunny, Humidity 45%")
        st.write("Wind: 10 km/h, Condition: Clear Sky")
    elif city == "Tirupati":
        st.success("Tirupati: 33°C, Sunny, Humidity 50%")
        st.write("Wind: 12 km/h, Condition: Hot and Sunny")
    elif city == "Chennai":
        st.success("Chennai: 31°C, Cloudy, Humidity 70%")
        st.write("Wind: 15 km/h, Condition: Cloudy")
    elif city == "Bangalore":
        st.success("Bangalore: 26°C, Rainy, Humidity 80%")
        st.write("Wind: 8 km/h, Condition: Light Rain")
    elif city == "Delhi":
        st.success("Delhi: 28°C, Foggy, Humidity 60%")
        st.write("Wind: 6 km/h, Condition: Foggy Morning")
    else:
        st.success("Mumbai: 30°C, Humid, Humidity 75%")
        st.write("Wind: 18 km/h, Condition: Humid")
