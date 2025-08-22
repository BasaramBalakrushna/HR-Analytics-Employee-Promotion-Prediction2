import streamlit as st
import joblib
import pandas as pd
import os

import joblib
import pandas as pd
import os
import streamlit as st

# # Correct full path to the model
# model_path = r"C:\Users\ADMIN\Desktop\Hr_Promotion_Project\HR PROJECT(29072025) (2)\xgb_model.pkl"

# # Check if model exists
# if not os.path.exists(model_path):
#     st.error(f"❌ Model file not found at: {model_path}")
#     st.stop()

# # Load XGBoost model
# model = joblib.load(model_path)


#1
# Load model relative to app.py
# model_path = "xgb_model.pkl"

# if not os.path.exists(model_path):
#     st.error(f"❌ Model file not found at: {model_path}")
#     st.stop()

# model = joblib.load(model_path)

#2
import os, joblib

model_path = os.path.join(os.path.dirname(__file__), "xgb_model.pkl")
model = joblib.load(model_path)








# Try to get feature names from the model
if hasattr(model, "feature_names_in_"):
    features = list(model.feature_names_in_)
else:
    features = [
        'no_of_trainings', 'age', 'previous_year_rating', 'length_of_service', 'avg_training_score',
        'education', 'gender', 'kpis_above_80', 'awards_won',
        'department_Analytics', 'department_Finance', 'department_HR', 'department_Legal',
        'department_Operations', 'department_Procurement', 'department_R&D', 'department_Sales & Marketing', 'department_Technology',
        'recruitment_channel_other', 'recruitment_channel_referred', 'recruitment_channel_sourcing',
    ] + [f'region_region_{i}' for i in range(1, 35)]  # ✅ UPDATED to include all 34 regions

st.title("Employee Promotion Prediction (XGBoost)")

# Inputs
department = st.selectbox("Department", [
    'Analytics', 'Finance', 'HR', 'Legal', 'Operations',
    'Procurement', 'R&D', 'Sales & Marketing', 'Technology'
])

# ✅ UPDATED: Full region list (34 regions)
region = st.selectbox("Region", [f'region_{i}' for i in range(1, 35)])

education = st.selectbox("Education", [
    'Below Secondary', "Bachelor's", "Master's"
])

gender = st.selectbox("Gender", ['Male', 'Female'])

recruitment = st.selectbox("Recruitment Channel", [
    'other', 'referred', 'sourcing'
])

trainings = st.slider("No. of Trainings", 1, 10, 1)
age = st.slider("Age", 20, 60, 30)
rating = st.slider("Previous Year Rating", 0.0, 5.0, 3.0, step=0.5)
service = st.slider("Length of Service", 1, 35, 5)
score = st.slider("Average Training Score", 0, 100, 60)

kpi = st.radio("KPIs > 80%", ['Yes', 'No'])
award = st.radio("Awards Won?", ['Yes', 'No'])

if st.button("Predict"):
    edu_map = {"Below Secondary": 0, "Bachelor's": 1, "Master's": 2}
    gender_map = {'Male': 0, 'Female': 1}
    bin_map = {'Yes': 1, 'No': 0}

    row = {
        'no_of_trainings': trainings,
        'age': age,
        'previous_year_rating': rating,
        'length_of_service': service,
        'avg_training_score': score,
        'education': edu_map[education],
        'gender': gender_map[gender],
        'kpis_above_80': bin_map[kpi],
        'awards_won': bin_map[award],
        'department_Analytics': 1 if department == 'Analytics' else 0,
        'department_Finance': 1 if department == 'Finance' else 0,
        'department_HR': 1 if department == 'HR' else 0,
        'department_Legal': 1 if department == 'Legal' else 0,
        'department_Operations': 1 if department == 'Operations' else 0,
        'department_Procurement': 1 if department == 'Procurement' else 0,
        'department_R&D': 1 if department == 'R&D' else 0,
        'department_Sales & Marketing': 1 if department == 'Sales & Marketing' else 0,
        'department_Technology': 1 if department == 'Technology' else 0,
        'recruitment_channel_other': 1 if recruitment == 'other' else 0,
        'recruitment_channel_referred': 1 if recruitment == 'referred' else 0,
        'recruitment_channel_sourcing': 1 if recruitment == 'sourcing' else 0,
    }

    # One-hot encode selected region
    for i in range(1, 35):  # ✅ Handles all regions from region_1 to region_34
        row[f'region_region_{i}'] = 1 if region == f'region_{i}' else 0

    # Ensure all required features are present
    for col in features:
        if col not in row:
            row[col] = 0

    df = pd.DataFrame([row])[features]

    pred = model.predict(df)[0]

    if pred == 1:
        st.success("✅ Likely to be PROMOTED")
    else:
        st.error("❌ Not likely to be promoted")
