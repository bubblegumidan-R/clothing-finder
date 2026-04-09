import streamlit as st
import subprocess
import sys

# --- EMERGENCY INSTALL SECTION ---
# This forces the computer to install the tool if it's missing
try:
    from serpapi import GoogleSearch
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-search-results"])
    from serpapi import GoogleSearch
# ---------------------------------

# Grab the key from the Secrets vault
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
    st.error("Missing Key! Go to Settings -> Secrets and add SERPAPI_KEY")
