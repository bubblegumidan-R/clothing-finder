import streamlit as st
from serpapi import GoogleSearch

# --- 1. THE VAULT ---
api_key = st.secrets.get("SERPAPI_KEY")

st.set_page_config(page_title="Mom's Pro Clothing Finder", page_icon="👗")

# --- 2. THE FAVORITES STORAGE ---
# This makes sure the "List" exists as soon as the app starts
if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.title("👗 Mom's Pro Clothing Finder")

# --- 3. THE SIDEBAR (Price Slicer) ---
st.sidebar.header("Filter Settings")
max_price = st.sidebar.slider("Max Price ($)", 10, 500, 100)
st.sidebar.write(f"Filtering for items under **${max_price}**")

# --- 4. FAVORITES DISPLAY (Always Visible) ---
with st.expander("⭐ Mom's Saved List", expanded=True):
    if st.session_state.favorites:
        for index, item in enumerate(st.session_state.favorites):
            st.write(f"{index + 1}. {item}")
    else:
        st.write("Your list is empty. Heart an item to save it!")

# --- 5. THE CAMERA ---
st.subheader("1. Scan Clothing")
img_file = st.camera_input("Take a photo of the item")

# --- 6. SEARCH RESULTS ---
st.subheader("2. Search Results")

# This part now shows "Demo" results so you can test the buttons right now!
col1, col2 = st.columns(2)

with col1:
    st.image("https://placehold.co/200x200?text=Sample+Outfit", caption="Sample Deal - $35")
    # THE BUTTON
    if st.button("❤️ Save to Favorites"):
        st.session_state.favorites.append(f"Sample Outfit - $35")
        st.rerun() # This refreshes the page so the list updates instantly

with col2:
    if img_file:
        st.success("Photo captured! Searching Google Lens...")
        # (Real search logic goes here)
    else:
        st.info("Waiting for a photo to start real search...")
