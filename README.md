# ai-service

## 1. UI (Flask based)
    - Handles image input from the user.
    - Store into the common storage
    - Call the AI backend to process the image
    - PORT: 5000
**Environment Variable**
```sh
AI_BACKEND_URL=http://ip-address:5001
```

## 2. AI Backend (Flask based)
    - Process Image from the UI backend
    - PORT: 5001


## Running through 

## Running through Docker-Compose
**Pre-requisit**
1. Docker

**Steps**
1. Pull the code from Repo
2. Run docker compose command ```docker compose up --build```
3. Access the UI at [http://127.0.0.1:5001](http://127.0.0.1:5001)










