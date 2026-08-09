#frontend
from flask import Flask, render_template
import requests 

app = Flask(__name__)

# Active endpoint for the backend API running within the Docker network
FASTAPI_URL = "http://genai-api-container:8000/stats"

@app.route('/')
def dashboard():
    """
    Renders the main security dashboard.
    Fetches real-time statistics from the backend API,
    and falls back to an offline state if the service is unreachable.
    """
    try:
        response = requests.get(FASTAPI_URL)
        stats = response.json() 
    except:
        # Fallback dictionary for degraded/offline state presentation
        stats = {
            "total_requests": "error",
            "blocked_injections": "error",
            "data_leaks_prevented": "error",
            "status": "API Offline"
        }
        
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)