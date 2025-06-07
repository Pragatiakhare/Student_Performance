import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("C://Users//praga//Downloads//Stud_perform", "rb"))

st.title("🎓 Student Performance Predictor")

# Input fields
hours = st.number_input("📚 Number of Hours Studied", min_value=0, step=1)
score = st.number_input("📝 Previous Exam Score", min_value=0, max_value=100)
activity = st.selectbox("🏅 Participated in Extracurricular Activities?", ["Yes", "No"])
sleep = st.number_input("😴 Sleep Hours per Day", min_value=0, step=1)
papers = st.number_input("📄 Sample Question Papers Practiced", min_value=0, step=1)

# Convert 'Yes'/'No' to 1/0
activity_val = 1 if activity == "Yes" else 0

# Predict button
if st.button("🎯 Predict Performance"):
    input_df = pd.DataFrame([[hours, score, activity_val, sleep, papers]],
                            columns=['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 
                                     'Sleep Hours', 'Sample Question Papers Practiced'])
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Predicted Performance Index: {round(prediction, 2)}")
