import streamlit as st
import numpy as np
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Insurance Premium Estimator", page_icon="🏥")

st.title("🏥 Insurance Premium Estimator")
st.markdown("Fill in your details below to estimate your insurance premium.")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])

with col2:
    sex = st.selectbox("Sex", ["Female", "Male"])
    smoker = st.selectbox("Smoker?", ["No", "Yes"])
    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

sex_val = 0 if sex == "Female" else 1
smoker_val = 0 if smoker == "No" else 1
region_map = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
region_val = region_map[region]

if st.button("💰 Estimate Premium"):
    input_data = np.array([[age, sex_val, bmi, children, smoker_val, region_val]])
    prediction = model.predict(input_data)[0]
    
    st.success(f"### Estimated Annual Premium: **${prediction:,.2f}**")
    st.info("This is an estimate based on ML model trained on historical data.")
