import os
from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

AI_BACKEND_URL = os.getenv("AI_BACKEND_URL","http://127.0.0.1:5001")
if not AI_BACKEND_URL:
    raise Exception


@app.route("/")
def home():
    return render_template("home.html")

@app.post("/detect")
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), 400
    file = request.files['image']
    files = {'image': file}
    response = requests.post(AI_BACKEND_URL+"/image/detect", files=files)
    
    if response.status_code == 200:
        result = response.json()
        return jsonify(result)
    else:
        return jsonify({"error": "Object detection failed"}), 500

@app.get("/check-ai-backend")
def test_ai_backend():
    res = requests.get(AI_BACKEND_URL)
    if res.status_code == 200:
        return "AI backend accessible from UI"
    else:
        return "AI backend not accessible from UI"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
