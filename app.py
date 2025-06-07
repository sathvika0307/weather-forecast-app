import streamlit as st
import requests

st.title("🌦️ Weather Forecast App")

city = st.text_input("Enter a city name:")

if city:
    api_key = "your_openweather_api_key_here"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['main']
        desc = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        st.write(f"**Temperature**: {temp} °C")
        st.write(f"**Weather**: {weather} - {desc}")
    else:
        st.error("City not found. Please try again.")
