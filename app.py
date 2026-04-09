import streamlit as st
from serpapi import GoogleSearch

# Get the key from the Streamlit Secret Vault
if "SERPAPI_KEY" in st.secrets:
    api_key = st.secrets["SERPAPI_KEY"]
else:
    api_key = None

st.title("👗 Clothing Finder")

if api_key:
    st.write("Ready to help Mom scan some clothes!")
    picture = st.camera_input("Take a photo")
    
    if picture:
        st.success("Got the photo! Ready to search.")
else:
    st.error("Key missing! Go to Settings -> Secrets and add SERPAPI_KEY")
