#frontend
from flask import Flask, render_template
import requests 

app = Flask(__name__)

##FASTAPI_URL = "https://genai-security-api.onrender.com/stats"
##FASTAPI_URL = "http://192.168.7.100:8000/stats"
##FASTAPI_URL = "http://host.docker.internal:8000/stats"
FASTAPI_URL= "http://genai-api:8000/stats"


@app.route('/')
def dashboard():
    try:
        response = requests.get(FASTAPI_URL)
        stats = response.json() 
    except:

        stats = {
            "total_requests": "שגיאה",
            "blocked_injections": "שגיאה",
            "data_leaks_prevented": "שגיאה",
            "status": "API Offline"
        }
        
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(port=5001, debug=True)