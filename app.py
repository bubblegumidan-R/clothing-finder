import streamlit as st
from serpapi import GoogleSearch

# We are skipping the .env file and going straight to the Secret Vault
if "SERPAPI_KEY" in st.secrets:
    api_key = st.secrets["SERPAPI_KEY"]
else:
    api_key = None

st.set_page_config(page_title="Clothing Finder")
st.title("👗 Clothing Finder")

if api_key:
    st.write("Hi Mom! Take a photo to find the brand and price.")
    picture = st.camera_input("Scan Clothing")
    
    if picture:
        st.info("Photo captured! Searching...")
        # The AI logic will go here once the camera works!
else:
    st.error("API Key not found! Go to Settings -> Secrets to add it.")
