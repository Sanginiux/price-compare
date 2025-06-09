from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("SERPAPI_KEY")  # Set your SerpAPI key in env

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/compare")
def compare():
    product = request.args.get("product", "")
    if not product:
        return jsonify(prices=[], error="Product name required"), 400
    url = f"https://serpapi.com/search.json?engine=google_shopping&q={product}&api_key={API_KEY}"
    data = requests.get(url).json()
    prices = [
        {
            "title": item.get("title"),
            "price": item.get("extracted_price"),
            "store": item.get("source"),
            "link": item.get("link")
        }
        for item in data.get("shopping_results", [])
    ]
    return jsonify(prices=prices)

if __name__ == "__main__":
    app.run(debug=True)
