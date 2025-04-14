"""
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Taxi Fare Prediction - Linear Regression")

# Example input form
user_input = {}
for col in X.columns:
    user_input[col] = st.number_input(col, value=0.0)

input_df = pd.DataFrame([user_input])

# Prediction
prediction = lr.predict(input_df)[0]
st.write(f"Predicted Total Amount: ${prediction:.2f}")
"""