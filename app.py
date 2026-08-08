#frontend
from flask import Flask, render_template
import requests 

app = Flask(__name__)

#FASTAPI_URL = "https://genai-security-api.onrender.com/stats" - not relevant 
#FASTAPI_URL = "http://192.168.7.100:8000/stats" - for college testing, not relevant
#FASTAPI_URL = "http://host.docker.internal:8000/stats" - just for testing on windows, not relevant
FASTAPI_URL= "http://genai-api:8000/stats" 
#FASTAPI_URL = "http://genai-api-container:8000/stats" - not relevant
#FASTAPI_URL = "http://172.17.0.1:8000/stats"


@app.route('/')
def dashboard():
    try:
        response = requests.get(FASTAPI_URL)
        stats = response.json() 
    except:

        stats = {
            "total_requests": "error",
            "blocked_injections": "error",
            "data_leaks_prevented": "error",
            "status": "API Offline"
        }
        
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)