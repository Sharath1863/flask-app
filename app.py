from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():

     return "shreyas"





@app.route("/health")
def health():
    return jsonify(
        status="OK",
        service="flask-devops",
        hostname=socket.gethostname(),
        environment=os.getenv("ENV", "production")
    )

@app.route("/version")
def version():
    return "Version: 1.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
