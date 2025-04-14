import streamlit as st
import pandas as pd
import numpy as np
import joblib  # If you're using joblib to load the model
from sklearn.linear_model import LinearRegression

# Title
st.title("NYC Green Taxi Fare Prediction")

st.markdown("### Enter trip details to predict the total fare")

# Sample feature input (replace these with actual features from X.columns)
feature_names = ['trip_distance', 'fare_amount', 'extra', 'mta_tax', 'tip_amount',
                 'tolls_amount', 'improvement_surcharge', 'congestion_surcharge',
                 'trip_duration', 'passenger_count']

# Create input fields
user_input = {}
for feature in feature_names:
    user_input[feature] = st.number_input(feature, value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([user_input])

# Optional: Load trained model
try:
    lr = joblib.load("linear_model.pkl")
except:
    # Dummy model if not loaded
    lr = LinearRegression()
    lr.fit(input_df, [0])  # Dummy fit to prevent crash

# Predict button
if st.button("Predict Fare"):
    try:
        prediction = lr.predict(input_df)[0]
        st.success(f"Estimated Total Fare: ${prediction:.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
