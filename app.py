import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        api_key = os.getenv('SERPAPI_KEY')
        url = 'https://serpapi.com/search.json'

        params = {
            'engine': 'google',
            'q': query,
            'google_domain': 'google.co.in',
            'gl': 'in',
            'hl': 'en',
            'api_key': api_key,
            'tbm': 'shop'
        }

        response = requests.get(url, params=params)
        data = response.json()

        for item in data.get('shopping_results', []):
            link = item.get('link')
            if link and link.startswith('http'):
                results.append({
                    'source': item.get('source', 'Unknown'),
                    'price': item.get('price', 'N/A'),
                    'title': item.get('title', 'No title'),
                    'link': link
                })

    return render_template('index.html', results=results)

