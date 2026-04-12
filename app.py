import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")
if "favs" not in st.session_state:
    st.session_state.favs = []

st.title("👗 Mom's Pro Clothing Finder")

# 2. THE CAMERA
img_file = st.camera_input("Step 1: Take a photo")

if img_file:
    # 3. THE SEARCH BUTTON
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
                    item = results["shopping_results"][0]
                    # We store the result in 'session_state' so it doesn't disappear
                    st.session_state.last_result = item
                else:
                    st.warning("No direct matches found.")
            except:
                st.error("Search failed. Try again!")

# 4. SHOW THE RESULT (Outside the button logic to keep it stable)
if "last_result" in st.session_state:
    res = st.session_state.last_result
    st.success(f"Found a match: {res.get('title')}")
    st.write(f"**Price:** {res.get('price')}")
    st.link_button("Go to Store 🛒", res.get('link'))
    
    if st.button("❤️ Save to Favorites"):
        st.session_state.favs.append(f"{res.get('title')} ({res.get('price')})")
        st.toast("Saved to your list!")

# 5. SIDEBAR
with st.sidebar:
    st.header("⭐ Saved for Mom")
    for fav in st.session_state.favs:
        st.write(f"• {fav}")
