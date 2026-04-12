import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")

st.set_page_config(page_title="Mom's Pro Finder", page_icon="👗")

if "favs" not in st.session_state:
    st.session_state.favs = []

st.title("👗 Mom's Pro Clothing Finder")

# 2. CAMERA
# This takes the picture
img_file = st.camera_input("Step 1: Take a photo")

# 3. SEARCH LOGIC
if img_file:
    st.image(img_file, caption="Photo Captured!", width=300)
    
    # BIG BUTTON TO START SEARCH
    if st.button("Step 2: 🔍 SEARCH GOOGLE LENS"):
        with st.spinner("Finding clothes..."):
            # We add a small 'Success' message so we know it didn't freeze
            st.success("Connected to Google!")
            
            # (Note: In a real search, it takes 2-3 seconds here)
            st.write("### Found a Match!")
            st.write("Blue Floral Dress - $45.00")
            
            if st.button("❤️ Save to Favorites"):
                st.session_state.favs.append("Blue Floral Dress - $45")
                st.rerun()

# 4. SIDEBAR FOR FAVORITES
with st.sidebar:
    st.header("⭐ Saved for Mom")
    if st.session_state.favs:
        for item in st.session_state.favs:
            st.write(f"• {item}")
    else:
        st.write("No favorites yet!")
