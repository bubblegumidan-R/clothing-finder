import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")

if "favs" not in st.session_state:
    st.session_state.favs = []

st.set_page_config(page_title="Mom's Pro Finder", page_icon="👗")
st.title("👗 Mom's Universal Scanner")

# 2. THE FIX: SEARCH BOX
# Now Mom can type "Red Dress" or "Nikes" here
query = st.text_input("What are we scanning?", "Avocado Hoodie")

# 3. THE CAMERA
img_file = st.camera_input("Step 1: Take a photo")

if img_file:
    # 4. THE BUTTON
    if st.button("Step 2: 🔍 SEARCH FOR " + query.upper()):
        with st.spinner(f"Looking for {query}..."):
            try:
                search = GoogleSearch({
                    "engine": "google_shopping",
                    "q": query, # This uses the text you typed!
                    "api_key": api_key
                })
                results = search.get_dict()
                
                if "shopping_results" in results:
                    item = results["shopping_results"][0]
                    st.session_state.last_result = item
                else:
                    st.warning("No matches found for that name.")
            except:
                st.error("The robot is sleepy. Check your API key!")

# 5. DISPLAY RESULTS
if "last_result" in st.session_state:
    res = st.session_state.last_result
    st.success(f"Found: {res.get('title')}")
    st.write(f"Price: {res.get('price')}")
    
    # Safety link check
    link = res.get('link', 'https://www.google.com/search?q=' + query)
    st.link_button("Go to Store 🛒", link)
    
    if st.button("❤️ Save to Favorites"):
        st.session_state.favs.append(f"{res.get('title')} - {res.get('price')}")
        st.toast("Saved!")

# 6. SIDEBAR
with st.sidebar:
    st.header("⭐ Mom's List")
    for f in st.session_state.favs:
        st.write(f"• {f}")
