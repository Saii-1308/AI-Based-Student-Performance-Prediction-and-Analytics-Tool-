import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("C:\\Users\\jadha\\OneDrive\\Desktop\\PBL-project\\rf_model.pkl", "rb") as file:
    rf_model = pickle.load(file)

# Streamlit UI
st.title("🎓 Student Performance Prediction")

# User inputs
attendance = st.slider("Attendance (%)", 0, 100, 75)
behavior = st.selectbox("Behavior", ["Excellent", "Good", "Average", "Poor"])
extra_activities = st.selectbox("Extra Activities", ["Yes", "No"])
study_hours = st.slider("Study Hours per Day", 0, 10, 4)

# ✅ Convert categorical inputs to numerical values
behavior_mapping = {"Excellent": 3, "Good": 2, "Average": 1, "Poor": 0}
extra_activities_mapping = {"Yes": 1, "No": 0}

# Convert inputs to numerical format
input_data = np.array([[attendance, behavior_mapping[behavior], extra_activities_mapping[extra_activities], study_hours]])

# ✅ Make prediction
prediction = rf_model.predict(input_data)

# Display result
st.subheader(f"📌 Predicted Marks: {prediction[0]:.2f}")
