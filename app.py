import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")

if "favs" not in st.session_state:
    st.session_state.favs = []

st.set_page_config(page_title="Mom's Pro Finder", page_icon="👗")
st.title("👗 Mom's Smart Scanner")

# 2. THE TEXT BOX (Tell the robot what the photo is!)
query = st.text_input("What are we looking for?", placeholder="e.g. Blue Nike Shoes")

# 3. THE CAMERA
img_file = st.camera_input("Step 1: Take the photo")

if img_file:
    # We show the photo so Mom knows it worked
    st.image(img_file, caption="Photo Ready!", width=300)
    
    # 4. THE SEARCH BUTTON
    if st.button("Step 2: 🔍 SEARCH NOW"):
        if not query or query == "":
            st.warning("Please type what the item is in the box above first!")
        else:
            with st.spinner(f"Finding {query}..."):
                try:
                    search = GoogleSearch({
                        "engine": "google_shopping",
                        "q": query,
                        "api_key": api_key
                    })
                    results = search.get_dict()
                    
                    if "shopping_results" in results:
                        st.session_state.last_result = results["shopping_results"][0]
                    else:
                        st.error("No matches found. Try a different name!")
                except:
                    st.error("The robot is sleepy. Check your API key!")

# 5. DISPLAY RESULTS
if "last_result" in st.session_state:
    res = st.session_state.last_result
    st.success(f"Found: {res.get('title')}")
    st.write(f"Price: {res.get('price')}")
    
    st.link_button("Go to Store 🛒", res.get('link', 'https://google.com'))
    
    if st.button("❤️ Save to Favorites"):
        st.session_state.favs.append(f"{res.get('title')} - {res.get('price')}")
        st.toast("Saved!")

# 6. SIDEBAR
with st.sidebar:
    st.header("⭐ Mom's List")
    for f in st.session_state.favs:
        st.write(f"• {f}")
