import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")

if "favs" not in st.session_state:
    st.session_state.favs = []

st.set_page_config(page_title="Smart Scanner", page_icon="🔍")
st.title("🔍 Smart Clothing Scanner")

# 2. INPUTS
st.write("### Step 1: Name the item")
query = st.text_input("What are we scanning?", placeholder="e.g. HP Laptop")

st.write("### Step 2: Take the photo")
img_file = st.camera_input("Smile!")

if img_file:
    if st.button("Step 3: 🔍 START SMART SEARCH"):
        if not query:
            st.warning("Please type a name first!")
        else:
            with st.spinner(f"Searching for '{query}'..."):
                try:
                    search = GoogleSearch({
                        "engine": "google_shopping",
                        "q": query,
                        "api_key": api_key
                    })
                    results = search.get_dict()
                    
                    if "shopping_results" in results:
                        st.session_state.last_result = results["shopping_results"][0]
                        st.success("Found a match!")
                    else:
                        st.error("No matches found. Try a different name!")
                except:
                    st.error("Search failed. Check your API key!")

# 3. THE SMART LINK LOGIC (Your Idea!)
if "last_result" in st.session_state:
    res = st.session_state.last_result
    title = res.get('title')
    
    st.divider()
    st.write(f"### {title}")
    st.write(f"**Price:** {res.get('price')}")
    
    # YOUR IDEA: If the direct link is missing, create a Google Search link!
    direct_link = res.get('link')
    
    if direct_link:
        st.link_button("🛒 Buy Now", direct_link)
    else:
        # This creates a link to Google.com with the item name already typed in!
        google_search_url = f"https://www.google.com/search?q={title.replace(' ', '+')}"
        st.link_button("🔎 Search for this on Google", google_search_url)

    if st.button("❤️ Save to Favorites"):
        st.session_state.favs.append(f"{title}")
        st.toast("Saved!")

# 4. SIDEBAR
with st.sidebar:
    st.header("⭐ Saved in favrots")
    for f in st.session_state.favs:
        st.write(f"• {f}")
