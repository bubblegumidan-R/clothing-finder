import streamlit as st
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load your secret key
load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

# Set up the page title
st.set_page_config(page_title="Clothing Finder")
st.title("👗 Clothing Finder")
st.write("Hi Mom! Snap a photo of any clothing to find its price.")

# The Camera Tool
picture = st.camera_input("Take a photo")

if picture and api_key:
    st.write("🔍 Searching the internet for you...")
    
    # In a real app, we would upload 'picture' to get a URL here.
    # For now, let's just make sure the connection works!
    st.success("Camera connected! Next, we will link the search results.")
    
elif not api_key:
    st.error("Wait! You forgot to add your API Key to the .env file.")
