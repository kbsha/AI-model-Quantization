import streamlit as st
import requests

st.title("AI Cyber Threat Detector")

text = st.text_input("Enter URL or message")

if st.button("Analyze"):

    response = requests.post(
        "http://127.0.0.1:8001/predict",
        json={"text": text}
    )

    result = response.json()

    st.success(result["prediction"])
    st.write("Confidence:", result["confidence"])