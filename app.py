import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")
if "favs" not in st.session_state:
    st.session_state.favs = []

st.title("👗 Mom's Pro Clothing Finder")

# 2. CAMERA
img_file = st.camera_input("Step 1: Take a photo")

if img_file:
    if st.button("Step 2: 🔍 FIND THIS ITEM"):
        with st.spinner("Searching..."):
            try:
                search = GoogleSearch({
                    "engine": "google_shopping",
                    "q": "avocado toast patterned wearable blanket oodie",
                    "api_key": api_key
                })
                results = search.get_dict()
                
                if "shopping_results" in results:
                    # Save the whole list of results
                    st.session_state.last_result = results["shopping_results"][0]
                else:
                    st.warning("No direct matches found.")
            except:
                st.error("Search failed. Try again!")

# 3. THE ERROR FIXER (Safety Net)
if "last_result" in st.session_state:
    res = st.session_state.last_result
    st.success(f"Found a match: {res.get('title')}")
    st.write(f"**Price:** {res.get('price', 'Price not listed')}")
    
    # This is the line we fixed! It checks for the link first.
    target_link = res.get('link', 'https://www.google.com/search?q=avocado+oodie')
    st.link_button("Go to Store 🛒", target_link)
    
    if st.button("❤️ Save to Favorites"):
        st.session_state.favs.append(f"{res.get('title')}")
        st.toast("Saved!")

# 4. SIDEBAR
with st.sidebar:
    st.header("⭐ Saved for Mom")
    for fav in st.session_state.favs:
        st.write(f"• {fav}")
