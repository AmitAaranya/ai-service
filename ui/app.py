import mimetypes
import os
from flask import Flask, jsonify, render_template, request, send_file
import requests

app = Flask(__name__)

AI_BACKEND_URL = os.getenv("AI_BACKEND_URL","http://127.0.0.1:5001")
if not AI_BACKEND_URL:
    raise Exception
DATA_PATH = os.getenv("DATA_PATH",os.path.join("..","data"))


@app.route("/")
def home():
    return render_template("home.html")

@app.post("/detect")
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), 400
    file = request.files['image']
    file_path = os.path.join(DATA_PATH,file.filename)
    file.save(file_path)
    with open(file_path, 'rb') as f:
        files = {'image': (file.filename, f, 'image/jpeg')} 
        response = requests.post(AI_BACKEND_URL+"/image/detect", files=files)
    
    if response.status_code == 200:
        result = response.json()
        return jsonify(result)
    else:
        return jsonify({"error": "Object detection failed"}), 500



@app.get("/image/<filename>")
def show_image(filename):
    # Check if the file exists
    if not os.path.exists(os.path.join(DATA_PATH,filename)):
        return jsonify({"error": "Image path does not exist"}), 404

    # Get the MIME type of the file based on its extension
    mime_type, _ = mimetypes.guess_type(os.path.join(DATA_PATH,filename))
    if not mime_type:
        mime_type = 'application/octet-stream'  # Default MIME type if unable to guess
    
    # Send the file with the correct MIME type
    return send_file(os.path.join(DATA_PATH,filename), mimetype=mime_type)


@app.get("/check-ai-backend")
def test_ai_backend():
    res = requests.get(AI_BACKEND_URL)
    if res.status_code == 200:
        return "AI backend accessible from UI"
    else:
        return "AI backend not accessible from UI"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
