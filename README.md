# price-compare

Real-time product price comparison using SerpAPI and Flask.

## Setup

1. Create virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your SerpAPI API key in environment variable `SERPAPI_KEY`:

```bash
# Windows
set SERPAPI_KEY=your_api_key_here
# Mac/Linux
export SERPAPI_KEY=your_api_key_here
```

4. Run the Flask app:

```bash
python app.py
```

5. Open http://localhost:5000 in your browser and try it out!
