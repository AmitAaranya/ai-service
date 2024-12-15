from flask import Flask, jsonify, request
import torch
import cv2
from PIL import Image
import numpy as np

app = Flask(__name__)

model = torch.hub.load("ultralytics/yolov5", "yolov5s")

@app.route("/", methods=["GET"])
def hello():
    return "Hello from AI Backend Flask Server"

@app.route('/image/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({"error": "No image file found"}), 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    
    # Convert image to format compatible with YOLO
    img_np = np.array(img)
    results = model(img_np)
    
    # Extract bounding boxes and labels from the results
    boxes = results.xywh[0].tolist()  # Box coordinates and confidence score
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
    
    # Generate the output image with bounding boxes drawn
    output_img = np.array(img)
    for obj in detected_objects:
        x1, y1, w, h = obj['coordinates'].values()
        cv2.rectangle(output_img, (int(x1), int(y1)), (int(x1 + w), int(y1 + h)), (255, 0, 0), 2)
    
    # output_image_path = '/output/result.jpg'
    # cv2.imwrite(output_image_path, output_img)
    
    # Return the result as JSON
    return jsonify({
        'detections': detected_objects
        # 'output_image': output_image_path
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
