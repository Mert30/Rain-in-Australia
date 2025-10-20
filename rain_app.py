import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Modeli yükle
model = joblib.load("notebook/models/best_model.joblib")
feature_columns = joblib.load("notebook/features/feature_columns.joblib")

st.set_page_config(
    page_title="Rain Prediction in Australia ☔", page_icon="🌦️", layout="centered"
)
st.title("🌦️ Rain Prediction in Australia")
st.write("This app predicts whether it will rain tomorrow in Australia.")

col1, col2 = st.columns(2)

with col1:
    min_temp = st.number_input("Minimum Temperature (°C)")
    max_temp = st.number_input("Maximum Temperature (°C)")
    rainfall = st.number_input("Rainfall (mm)")
    evaporation = st.number_input("Evaporation (mm)")
    sunshine = st.number_input("Sunshine (hours)")
    wind_gust_speed = st.number_input("Wind Gust Speed (km/h)")
    wind_speed_9am = st.number_input("Wind Speed 9am (km/h)")
    wind_speed_3pm = st.number_input("Wind Speed 3pm (km/h)")
    humidity_9am = st.number_input("Humidity 9am (%)")
    humidity_3pm = st.number_input("Humidity 3pm (%)")
    pressure_9am = st.number_input("Pressure 9am (hPa)")

with col2:
    location = st.text_input("Location")
    wind_gust_dir = st.selectbox(
        "Wind Gust Direction", ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    )
    wind_dir_9am = st.selectbox(
        "Wind Direction 9am", ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    )
    wind_dir_3pm = st.selectbox(
        "Wind Direction 3pm", ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    )
    rain_today = st.selectbox("Rain Today?", ["Yes", "No"])
    pressure_3pm = st.number_input("Pressure 3pm (hPa)")
    cloud_9am = st.number_input("Cloud 9am (oktas)")
    cloud_3pm = st.number_input("Cloud 3pm (oktas)")
    temp_9am = st.number_input("Temperature 9am (°C)")
    temp_3pm = st.number_input("Temperature 3pm (°C)")
    year = st.number_input("Year", min_value=2000, max_value=2030, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, step=1)
    day = st.number_input("Day", min_value=1, max_value=30, step=1)

if st.button("🌧️ Predict"):
    rain_today_val = 1 if rain_today == "Yes" else 0

    input_data = pd.DataFrame(
        [
            [
                location,
                min_temp,
                max_temp,
                rainfall,
                evaporation,
                sunshine,
                wind_gust_dir,
                wind_gust_speed,
                wind_dir_9am,
                wind_dir_3pm,
                wind_speed_9am,
                wind_speed_3pm,
                humidity_9am,
                humidity_3pm,
                pressure_9am,
                pressure_3pm,
                cloud_9am,
                cloud_3pm,
                temp_9am,
                temp_3pm,
                rain_today_val,
                year,
                month,
                day,
            ]
        ],
        columns=[
            "Location",
            "MinTemp",
            "MaxTemp",
            "Rainfall",
            "Evaporation",
            "Sunshine",
            "WindGustDir",
            "WindGustSpeed",
            "WindDir9am",
            "WindDir3pm",
            "WindSpeed9am",
            "WindSpeed3pm",
            "Humidity9am",
            "Humidity3pm",
            "Pressure9am",
            "Pressure3pm",
            "Cloud9am",
            "Cloud3pm",
            "Temp9am",
            "Temp3pm",
            "RainToday",
            "Year",
            "Month",
            "Day",
        ],
    )

    input_data = pd.get_dummies(input_data)

    input_data = input_data.reindex(columns=feature_columns, fill_value=0)

    input_data = input_data.astype(
        {col: "int8" for col in input_data.select_dtypes("bool").columns}
    )

    scaler = StandardScaler()
    scaled_input = scaler.fit_transform(input_data)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🌧️ Tomorrow **rain is expected!** Don't forget to take your umbrella.")
    else:
        st.success("☀️ Tomorrow **rain is NOT expected.** A beautiful day awaits you!")
