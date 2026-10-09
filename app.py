import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Page title
st.title("Student Performance Predictor")
st.write("Enter the student details below to predict the expected exam marks.")

# Input fields
study_hours = st.slider("Study Hours per Day", min_value=1, max_value=12, value=5)
attendance = st.slider("Attendance Percentage", min_value=0, max_value=100, value=75)
previous_marks = st.slider("Previous Exam Marks", min_value=0, max_value=100, value=60)

# Predict button
if st.button("Predict Marks"):
    input_data = np.array([[study_hours, attendance, previous_marks]])
    prediction = model.predict(input_data)[0]
    # Clamp prediction between 0 and 100
    prediction = max(0, min(100, round(prediction, 1)))
    st.success(f"Predicted Exam Marks: **{prediction} / 100**")
