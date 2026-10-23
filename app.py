
import streamlit as st
import pandas as pd
import joblib

st.title("Company Employee Salary Prediction")

model = joblib.load("company_employee_model.pkl")

salary = st.number_input(
    "Basic Salary", min_value=0, value=52000
)
attendance = st.number_input(
    "Attendance Days", min_value=0, max_value=31, value=25
)
department = st.selectbox(
    "Department", ["IT", "HR", "Finance", "Marketing"]
)

if st.button("Predict Salary Category"):
    st.info(
        "To predict correctly, use the same feature preparation "
        "and columns used during model training."
    )
