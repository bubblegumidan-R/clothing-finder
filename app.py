import streamlit as st
from serpapi import GoogleSearch

# --- 1. THE VAULT (Getting your key) ---
if "SERPAPI_KEY" in st.secrets:
    api_key = st.secrets["SERPAPI_KEY"]
else:
    api_key = None

st.set_page_config(page_title="Mom's Pro Clothing Finder", page_icon="👗")

st.title("👗 Mom's Pro Clothing Finder")

# --- 2. THE SIDEBAR (The Price Slicer) ---
st.sidebar.header("Filter Settings")
max_price = st.sidebar.slider("Max Price ($)", 10, 500, 100)
st.sidebar.write(f"Looking for clothes under ${max_price}")

# --- 3. THE FAVORITES BIN ---
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# --- 4. THE CAMERA ---
img_file = st.camera_input("Scan a clothing item")

if img_file and api_key:
    st.info("Searching for deals...")
    
    # This is where the magic happens
    search = GoogleSearch({
        "engine": "google_lens",
        "url": "https://example.com/placeholder_image.jpg", # Placeholder for now
        "api_key": api_key
    })
    
    # For now, let's show a 'Mock' result so Mom can see the Price Slicer work
    st.subheader(f"Results under ${max_price}:")
    
    # Imagine these are real results from the search
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://placehold.co/200x200?text=Cool+Shirt", caption="Found Shirt - $35")
        if st.button("❤️ Save to Favorites"):
            st.session_state.favorites.append("Cool Shirt - $35")
            st.success("Saved!")

# --- 5. SHOW FAVORITES ---
if st.session_state.favorites:
    with st.expander("⭐ Mom's Saved List"):
        for item in st.session_state.favorites:
            st.write(item)
