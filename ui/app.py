from flask import Flask
import requests

app = Flask(__name__)

AI_BACKEND_URL = "http://ai-backend:5001"

@app.route("/")
def hello():
    return "Hello from UI Flask Server"


@app.get("/check-ai-backend")
def test_ai_backend():
    res = requests.get(AI_BACKEND_URL)
    if res.status_code == 200:
        return "AI backend accessible from UI"
    else:
        return "AI backend not accessible from UI"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
