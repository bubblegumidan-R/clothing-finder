import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load your secret key
load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    # This shows your HTML file
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    # Get the image from the website
    image_file = request.files['clothing_image']
    
    # Logic for SerpApi (Google Lens)
    # Note: SerpApi usually needs a public URL, but for testing
    # we can search for the "text" you describe or upload it.
    params = {
        "engine": "google_lens",
        "api_key": api_key,
        "url": "https://example.com/image.jpg" # This will be the photo Mom takes
    }
    
    # search = GoogleSearch(params)
    # results = search.get_dict()
    
    return "Scanning logic connected! Ready to find prices."

if __name__ == '__main__':
    app.run(debug=True)
