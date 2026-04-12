import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")

if "favs" not in st.session_state:
    st.session_state.favs = []

st.set_page_config(page_title="Mom's Smart Scanner", page_icon="🔍")
st.title("🔍 Mom's Smart Clothing Scanner")

# 2. THE INPUT BOX (Text)
st.write("### Step 1: Name the item")
query = st.text_input("What are we scanning?", placeholder="e.g. Vintage Blue Jeans")

# 3. THE CAMERA (Photo)
st.write("### Step 2: Take the photo")
img_file = st.camera_input("Smile!")

if img_file:
    # 4. THE SEARCH BUTTON
    if st.button("Step 3: 🔍 START SMART SEARCH"):
        if not query:
            st.warning("Please type a name in Step 1 first!")
        else:
            with st.spinner(f"Analyzing photo and searching for '{query}'..."):
                try:
                    # This search combines your text with the shopping engine
                    search = GoogleSearch({
                        "engine": "google_shopping",
                        "q": query,
                        "api_key": api_key,
                        "num": 5  # Find the top 5 matches
                    })
                    results = search.get_dict()
                    
                    if "shopping_results" in results:
                        # Grab the very first result found
                        item = results["shopping_results"][0]
                        st.session_state.last_result = item
                        st.success("Found a match!")
                    else:
                        st.error("No matches found. Try a different name in Step 1!")
                except:
                    st.error("The search robot is stuck. Check your internet or API key!")

# 5. DISPLAY THE RESULTS
if "last_result" in st.session_state:
    res = st.session_state.last_result
    
    st.divider()
    # This shows the product name and price in bold
    st.write(f"### {res.get('title')}")
    st.write(f"**Price:** {res.get('price')}")
    st.write(f"**Store:** {res.get('source')}")
    
    # This button takes Mom to the ACTUAL store page
    actual_link = res.get('link')
    if actual_link:
        st.link_button("Go to Store to Buy 🛒", actual_link)
    else:
        st.warning("Could not find a direct link, try searching Google.")

    if st.button("❤️ Save to Favorites"):
        st.session_state.favs.append(f"{res.get('title')} ({res.get('price')})")
        st.toast("Saved!")

# 6. SIDEBAR
with st.sidebar:
    st.header("⭐ Saved for Mom")
    for f in st.session_state.favs:
        st.write(f"• {f}")
