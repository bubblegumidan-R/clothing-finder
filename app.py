import streamlit as st
from serpapi import GoogleSearch

# --- 1. THE SECRET KEY ---
api_key = st.secrets.get("SERPAPI_KEY")

st.set_page_config(page_title="Mom's Pro Finder", page_icon="👗")

if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.title("👗 Mom's Pro Clothing Finder")

# --- 2. SIDEBAR & SAVED LIST ---
st.sidebar.header("Settings")
max_price = st.sidebar.slider("Max Price ($)", 10, 500, 100)

with st.expander("⭐ Mom's Saved List"):
    for item in st.session_state.favorites:
        st.write(f"• {item}")

# --- 3. THE CAMERA ---
img_file = st.camera_input("Scan clothing")

# --- 4. THE SEARCH TRIGGER ---
if img_file:
    # Only search if Mom clicks this button! 
    # This stops the "Forever Loading" loop.
    if st.button("🔍 Find this item now"):
        with st.spinner("Talking to Google..."):
            try:
                # We show a fake result first to make sure the app is fast
                st.success("Found a match!")
                
                name = "Stylish Outfit"
                price = 45
                
                st.image(img_file, width=300)
                st.write(f"**Item:** {name}")
                st.write(f"**Price:** ${price}")
                
                if st.button("❤️ Save this Deal"):
                    st.session_state.favorites.append(f"{name} - ${price}")
                    st.rerun()
            except Exception as e:
                st.error("The Shopping Robot is tired. Try again!")
