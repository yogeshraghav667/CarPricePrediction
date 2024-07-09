import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('LRmodel.pkl', 'rb') as file:
    model = pickle.load(file)

df = pd.read_csv("dataset.csv")
cars_name = df["name"]
company = df["company"]

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

# Custom CSS to add a background image with reduced opacity and change label colors
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://stimg.cardekho.com/images/carexteriorimages/930x620/Maruti/FRONX/9243/1697697928533/front-left-side-47.jpg");
        background-size: cover;
    }
    .title {
        color: #FF6347; /* Tomato color */
        font-size: 3em;
    }
    .footer {
        margin-top: 20px;
        font-size: 0.8em;
        color: #666;
    }
    .footer .connect-text {
        color: #FFC300; /* Indigo color */
    }
    .footer a {
        color: #FDFEFE; /* White color */
        text-decoration: none;
        margin-right: 10px;
        font-size: 1.2em; /* Increase font size */
    }
    .connect-title {
        font-size: 1.3em;
        color: #FF6347; /* Change the color of Connect with me */
        font-weight: bold; /* Make the text bold */
    }
    label {
        color: #000000 !important; /* Change the color of input field labels */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h4 style='color: #FF6347;'>Created by Y.S.RAGHAV</h4>", unsafe_allow_html=True)
st.markdown("<h1 class='title'>Car Price Prediction</h1>", unsafe_allow_html=True)


# Input fields
name = st.selectbox("Car Name", cars_name)
company = st.selectbox("Company", company)
year = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, value=2020)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG", "CNG"])

# Predict button
if st.button("Predict Price"):
    price = predict_price(name, company, year, kms_driven, fuel_type)
    st.success(f"The predicted price of the car is: ₹{price}")

# Contact information
st.markdown("<div class='contact-box'>", unsafe_allow_html=True)
st.markdown("<div class='footer'><span class='connect-title'>Connect with me:</span> "
            "<a href='https://www.linkedin.com/in/yogesh-singh-raghav-ab52b0255/' target='_blank'>LinkedIn</a> | "
            "<a href='https://www.instagram.com/y.s.raghav_/' target='_blank'>Instagram</a> | "
            "<a href='https://github.com/yogeshraghav667' target='_blank'>GitHub</a> | "
            "<a href='mailto:yogeshraghav667@gmail.com' target='_blank'>Email</a></div>",
            unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
