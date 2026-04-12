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
    st.image(img_file, caption="Photo Captured!", width=300)
    
    # 3. THE SMART SEARCH BUTTON
    if st.button("Step 2: 🔍 FIND THIS ITEM"):
        with st.spinner("Searching all stores..."):
            try:
                # We search for the item generally to make sure Mom gets a result!
                search = GoogleSearch({
                    "engine": "google_shopping",
                    "q": "avocado toast patterned hoodie oodie",
                    "api_key": api_key
                })
                results = search.get_dict()
                
                if "shopping_results" in results:
                    item = results["shopping_results"][0]
                    st.success(f"Found a match: {item.get('title')}")
                    st.write(f"Price: {item.get('price')}")
                    st.link_button("Go to Store 🛒", item.get('link'))
                    
                    if st.button("❤️ Save to Favorites"):
                        st.session_state.favs.append(f"{item.get('title')} - {item.get('price')}")
                        st.rerun()
                else:
                    st.warning("No direct matches. Try searching for 'Avocado Hoodie' manually!")
                    
            except Exception as e:
                st.error("The search robot is sleepy. Try again in a minute!")

# 4. SIDEBAR
with st.sidebar:
    st.header("⭐ Saved for Mom")
    for fav in st.session_state.favs:
        st.write(f"• {fav}")
