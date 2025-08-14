import streamlit as st
import pandas as pd
import joblib
import json
import pickle

st.title('Digital Mindset Prediction App')

# Load model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please ensure model.pkl exists in the same directory.")
    st.stop()

# Define the features we know are important based on our analysis
selected_features = [
    'age', 'years_in_role', 'growth_mindset_score', 
    'limiting_beliefs_score', 'training_hours_last_year',
    'leadership_score', 'team_openness_score',
    'recent_failed_initiatives', 'positive_feedback_percent'
]

# User input form
st.write("Enter input values for prediction:")
user_input = {}

# Create input fields for each feature
for feature in selected_features:
    # Add appropriate min/max values and step size for each feature
    if feature == 'age':
        user_input[feature] = st.number_input(f"{feature}", min_value=18, max_value=100, value=30)
    elif feature == 'years_in_role':
        user_input[feature] = st.number_input(f"{feature}", min_value=0, max_value=50, value=5)
    elif feature in ['growth_mindset_score', 'leadership_score', 'team_openness_score']:
        user_input[feature] = st.number_input(f"{feature}", min_value=0.0, max_value=10.0, value=5.0)
    elif feature == 'limiting_beliefs_score':
        user_input[feature] = st.number_input(f"{feature}", min_value=0.0, max_value=10.0, value=3.0)
    elif feature == 'training_hours_last_year':
        user_input[feature] = st.number_input(f"{feature}", min_value=0, max_value=500, value=40)
    elif feature == 'recent_failed_initiatives':
        user_input[feature] = st.number_input(f"{feature}", min_value=0, max_value=20, value=2)
    elif feature == 'positive_feedback_percent':
        user_input[feature] = st.number_input(f"{feature}", min_value=0.0, max_value=100.0, value=75.0)
    else:
        user_input[feature] = st.number_input(f"{feature}", value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([user_input])

# Predict button
if st.button("Predict Digital Mindset Score"):
    try:
        prediction = model.predict(input_df)
        st.success(f"Predicted Digital Mindset Score: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
