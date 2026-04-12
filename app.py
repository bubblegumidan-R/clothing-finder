import streamlit as st
from serpapi import GoogleSearch

# 1. SETUP
api_key = st.secrets.get("SERPAPI_KEY")

if "favs" not in st.session_state:
    st.session_state.favs = []

st.set_page_config(page_title="Mom's Smart Scanner", page_icon="🔍")
st.title("🔍 Mom's AI Smart Scanner")

# 2. INPUTS (No more placeholder!)
st.write("### Step 1: Name the item")
query = st.text_input("What are we scanning?", value="", placeholder="Type the name here...")

# 3. THE CAMERA
st.write("### Step 2: Take the photo")
img_file = st.camera_input("Smile!")

if img_file:
    if st.button("Step 3: 🔍 START SMART SEARCH"):
        if not query:
            st.warning("Whoops! Please type the name of the item first so the AI knows what to look for.")
        else:
            with st.spinner(f"AI is analyzing '{query}'..."):
                try:
                    search = GoogleSearch({
                        "engine": "google_shopping",
                        "q": query,
                        "api_key": api_key
                    })
                    results = search.get_dict()
                    
                    if "shopping_results" in results:
                        st.session_state.last_result = results["shopping_results"][0]
                        st.success("Match Found!")
                    else:
                        st.error("The AI couldn't find that exact item. Try a simpler name!")
                except:
                    st.error("The robot is sleepy. Check your API key!")

# 4. THE AI ASSISTANT (Insights & Rating)
if "last_result" in st.session_state:
    res = st.session_state.last_result
    title = res.get('title')
    price = res.get('price', 'Price hidden')
    store = res.get('source', 'Unknown Store')
    
    st.divider()
    st.write(f"### {title}")
    
    # AI ASSISTANT BOX
    with st.expander("✨ AI Expert Analysis", expanded=True):
        st.write(f"**The Verdict:** This looks like a solid find from **{store}**.")
        st.write(f"**Price Check:** It's listed at **{price}**. Make sure to check if shipping is included!")
        st.info("💡 **AI Tip:** If you're buying this as a gift, check the return policy just in case!")

    # 5. BUTTONS
    direct_link = res.get('link')
    if direct_link:
        st.link_button(f"🛒 Buy from {store}", direct_link)
    else:
        google_search_url = f"https://www.google.com/search?q={title.replace(' ', '+')}"
        st.link_button("🔎 See more prices on Google", google_search_url)

    if st.button("❤️ Save to Mom's List"):
        st.session_state.favs.append(f"{title} ({price})")
        st.toast("Saved!")

# 6. SIDEBAR
with st.sidebar:
    st.header("⭐ Mom's Favorites")
    if not st.session_state.favs:
        st.write("No items saved yet.")
    for f in st.session_state.favs:
        st.write(f"• {f}")                
