from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello from AI Backend Flask Server"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)