import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('LRmodel.pkl', 'rb') as file:
    model = pickle.load(file)

df = pd.read_csv("C:\\Users\\HP\\Downloads\\quikr_car.csv")
cars_name = df["name"].str.split().str.slice(0,3).str.join(" ").unique()
company = df["company"].unique()

def predict_price(name, company, year, kms_driven, fuel_type):
    # Create a dataframe with input values
    input_df = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    # Use the model to predict the price
    prediction = model.predict(input_df)
    return prediction[0]



# Custom CSS to add a background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("https://stimg.cardekho.com/images/carexteriorimages/930x620/Maruti/FRONX/9243/1697697928533/front-left-side-47.jpg");
        background-size: cover;
    }}
    .title {{
        color: #FF6347; /* Tomato color */
        font-size: 3em;
    }}
    .footer {{
        margin-top: 20px;
        font-size: 0.8em;
        color: #666;
    }}
    .footer .connect-text {{
        color: #4B0082; /* Indigo color */
        font-weight: bold; /* Make text bold */
    }}
    .footer a {{
        color: #FF6347; /* Red color */
        text-decoration: none;
        margin-right: 10px;
        font-weight: bold; /* Make links bold */
        font-size: 1.2em; /* Increase font size */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Car Price Prediction</h1>", unsafe_allow_html=True)

# Input fields
name = st.selectbox("Car Name", cars_name)
company = st.selectbox("Company", company)
year = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, value=2020)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG"])

# Predict button
if st.button("Predict Price"):
    price = predict_price(name, company, year, kms_driven, fuel_type)
    st.success(f"The predicted price of the car is: ₹{price}")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Connect with me: "
            "<a href='https://www.linkedin.com/in/yogesh-singh-raghav-ab52b0255/' target='_blank'>LinkedIn</a> | "
            "<a href='https://www.instagram.com/y.s.raghav_/' target='_blank'>Instagram</a> | "
            "<a href='https://github.com/yogeshraghav667' target='_blank'>GitHub</a> | "
            "<a href='mailto:yogeshraghav667@gmail.com' target='_blank'>Email</a></div>",
            unsafe_allow_html=True)