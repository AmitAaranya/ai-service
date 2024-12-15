import json
import os
from flask import Flask, jsonify, request
import torch
import numpy as np
from PIL import Image
from img_ops import create_bounding_box

app = Flask(__name__)

model = torch.hub.load("ultralytics/yolov5", "yolov5s")
DATA_PATH = os.getenv("DATA_PATH",os.path.join("..","data"))

@app.route("/", methods=["GET"])
def hello():
    return "Hello from AI Backend Flask Server"

@app.route('/image/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({"error": "No image file found"}), 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    img_np = np.array(img)
    results = model(img_np)
    
    boxes = results.xywh[0].tolist() 
    labels = results.names  # Object labels
    
    detected_objects = []
    for box in boxes:
        detected_objects.append({
            'label': labels[int(box[5])], 
            'confidence': box[4],
            'coordinates': {
                'x': box[0],
                'y': box[1],
                'width': box[2],
                'height': box[3]
            }
        })
    output_image_path = os.path.join(DATA_PATH,f"out_{file.filename}")
    output_img_np = create_bounding_box(detected_objects,np.array(img),output_image_path)
    res = {
        'detections': detected_objects,
        'path': output_image_path
    }
    json.dump(res,open(os.path.join(DATA_PATH,f"{file.filename}.json"),"w"),indent=4)
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5001)
