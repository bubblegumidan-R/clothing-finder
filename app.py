import streamlit as st
from serpapi import GoogleSearch

# Pulling the key from the Secrets vault
if "SERPAPI_KEY" in st.secrets:
    api_key = st.secrets["SERPAPI_KEY"]
else:
    api_key = None

st.title("👗 Clothing Finder")

if api_key:
    st.write("Ready for Mom to scan clothes!")
    picture = st.camera_input("Take a photo")
    if picture:
        st.success("Photo received! AI is ready.")
else:
    st.error("Missing Key! Add 'SERPAPI_KEY' to your Streamlit Secrets.")
