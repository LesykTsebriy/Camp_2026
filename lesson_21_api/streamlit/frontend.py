import requests
import streamlit as st

st.title("Streamlit Greeting App")
st.write("This frontend talks directly to the FastAPI backend engine.")

# 1. UI Components Layout
name = st.text_input("Name", value="World")
intensity = st.slider("Intensity", min_value=1, max_value=10, value=5)

# 2. Trigger Action on Button Click
if st.button("Greet"):
    payload = {"name": name, "intensity": intensity}
    try:
        # Send a network request to the FastAPI server
        response = requests.get("http://127.0.0.1:8000/api/greet", params=payload)
        
        if response.status_code == 200:
            result_text = response.json()["result"]
            st.success(result_text)
        else:
            st.error(f"Backend API returned an error code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI. Is backend.py running on port 8000?")
