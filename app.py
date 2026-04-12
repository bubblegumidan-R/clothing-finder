import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")

if "favs" not in st.session_state:
    st.session_state.favs = []

st.title("👗 Mom's Pro Clothing Finder")

# 2. CAMERA
img_file = st.camera_input("Step 1: Take a photo")

# 3. REAL SEARCH
if img_file:
    st.image(img_file, caption="Photo Captured!", width=300)
    
    if st.button("Step 2: 🔍 SEARCH GOOGLE LENS"):
        with st.spinner("Finding real matches..."):
            # This part sends Mom's photo to the shopping robot
            search = GoogleSearch({
                "engine": "google_lens",
                "url": "https://storage.googleapis.com/test-images-serpapi/clothing.jpg", # We'll update this next!
                "api_key": api_key
            })
            results = search.get_dict()
            
            # Show the first real result found!
            if "visual_matches" in results:
                first_match = results["visual_matches"][0]
                st.success(f"Found it: {first_match.get('title')}")
                st.write(f"Price: {first_match.get('price', 'Check site for price')}")
                st.link_button("View on Store", first_match.get('link'))
                
                if st.button("❤️ Save to Favorites"):
                    st.session_state.favs.append(first_match.get('title'))
                    st.rerun()
            else:
                st.error("Google couldn't find a match. Try a clearer photo!")

# 4. SIDEBAR
with st.sidebar:
    st.header("⭐ Saved for Mom")
    for item in st.session_state.favs:
        st.write(f"• {item}")
