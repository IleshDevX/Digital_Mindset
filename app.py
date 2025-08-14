import streamlit as st
import pandas as pd
import joblib
import json
import pickle

# Load model and selected features
model = joblib.load("model.pkl")
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Digital Mindset Prediction App')

# User input form
st.write("Enter input values for prediction:")
user_input = {}
for feature in selected_features:
    user_input[feature] = st.number_input(f"{feature}", value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([user_input])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted value: {prediction[0]:.2f}")
