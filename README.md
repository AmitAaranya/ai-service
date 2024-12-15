# AI Service Microservice

This project contains two main components:
1. **UI Backend**: A Flask-based service that handles image input from the user, stores the image, and interacts with the AI backend for object detection.
2. **AI Backend**: A Flask-based service that processes the image using a lightweight object detection model (e.g., YOLOv5).

The UI communicates with the AI backend to perform object detection on images and returns results in a structured JSON format.

## Prerequisites
Before running this solution, ensure you have the following tools installed:

- **Python** (Flask or FastAPI): For building the backend services.
- **Docker**: For containerizing the application (optional).
- **Lightweight Object Detection Model**: An open-source model such as YOLOv5 or MobileNet SSD (we recommend [YOLOv5](https://github.com/ultralytics/yolov5) for object detection).
- **Python Libraries**:
  - `Flask`: For Python based backend server.
  - `requests`: For HTTP communication between the UI and AI backend.
  - `Pillow`: For reading the PIL image
  - `torch`: For accessing YOLOv5 model from Hub
  - `opencv-python`: For drawing bounding box into output image

## Architecture Overview

The system consists of two services:

1. **UI Backend**:  
    - Accepts image input from users.  
    - Stores the image and calls the AI backend to process it.  
    - Serves the processed image with bounding boxes and detection results in JSON format.  
    - **Port**: `5000`

2. **AI Backend**:  
    - Accepts image input from the UI backend.  
    - Uses an object detection model (e.g., YOLOv5) to process the image.  
    - Returns the bounding boxes and detected objects in a structured JSON format.  
    - **Port**: `5001`

## Environment Variables

In the UI service, ensure the following environment variable is set to point to the AI backend:
```sh
AI_BACKEND_URL=http://ip-address:5001
```

# Running the Services
## 1. Running Without Docker

**UI Backend**
- Navigate to the `ui` directory.
- Install the necessary dependencies:
```sh
pip install -r requirements.txt
```
- Run the UI backend:
```sh
python app.py
```
- The UI should be accessible at http://127.0.0.1:5000.

**AI Backend**
- Navigate to the `ai-backend` directory.
- Install the necessary dependencies:
```sh
pip install -r requirements.txt
```
- Run the AI backend:
```sh
python app.py
```
- The AI backend should be accessible at http://127.0.0.1:5001.

## 2. Running with Docker and Docker Compose
**Prerequisites**
- Ensure Docker is installed on your machine.
- Ensure Docker Compose is installed.
**Steps**
- Clone the repository to your local machine:
```sh
git clone https://github.com/AmitAaranya/ai-service.git
```
- Navigate to the root directory of the project:
- Build and run the services using Docker Compose:
```sh
docker-compose up --build
```
- The UI should be accessible at http://127.0.0.1:5000.
- The AI backend will be running at http://127.0.0.1:5001.

# Interacting with the Services
**Upload an Image:**
- Access the UI via the browser at http://127.0.0.1:5000.
- Upload an image for processing.

**Processing by AI:**
- The UI backend sends the image to the AI backend for object detection.
- The AI backend processes the image, applies the object detection model, and returns the results.

**Output:**
- The UI backend returns the processed image with bounding boxes and a structured JSON response containing the detected objects.
```json
{
    "detections": [
        {
            "confidence": 0.889124870300293,
            "coordinates": {
                "height": 255.1783905029297,
                "width": 137.53494262695312,
                "x": 172.6475830078125,
                "y": 298.4649963378906
            },
            "label": "dog"
        },
        {
            "confidence": 0.6902128458023071,
            "coordinates": {
                "height": 77.86497497558594,
                "width": 169.74417114257812,
                "x": 453.25555419921875,
                "y": 96.6738052368164
            },
            "label": "car"
        }
    ]
}
```


# References
- [Loading pre-trained YOLOv5 model via PyTorch Hub](https://docs.ultralytics.com/yolov5/tutorials/pytorch_hub_model_loading/#before-you-start)
- [Getting start with Docker](https://docs.docker.com/get-started/)
- [Docker Compose documentation](https://docs.docker.com/compose/gettingstarted/)
- [Python Flask documentation](https://flask.palletsprojects.com/en/stable/)