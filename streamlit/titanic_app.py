import streamlit as st
import requests

st.title("Titanic Survival Prediction")

# User inputs
pclass = st.selectbox("Passenger Class", [1,2,3])
sex = st.selectbox("Sex", ["male","female"])
age = st.number_input("Age", min_value=0.0, max_value=100.0, value=30.0)
fare = st.number_input("Fare", min_value=0.0, value=32.0)
embarked = st.selectbox("Port of Embarkation", ["C","Q","S"])

if st.button("Predict Survival"):
    data = {
        "pclass": pclass,
        "sex": sex,
        "age": age,
        "fare": fare,
        "embarked": embarked
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Survived: {result['survived']} (Probability: {result['survival_prob']*100:.2f}%)")
    else:
        st.error("API call failed")
