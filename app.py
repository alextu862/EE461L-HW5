# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # so React (localhost or Heroku) can call these routes

@app.route("/checkin/<projectId>/<qty>")
def checkIn_hardware(projectId, qty):
    return jsonify({"message": f"{qty} hardware checked in", "projectId": projectId})

@app.route("/checkout/<projectId>/<qty>")
def checkOut_hardware(projectId, qty):
    return jsonify({"message": f"{qty} hardware checked out", "projectId": projectId})

@app.route("/join/<projectId>")
def joinProject(projectId):
    return jsonify({"message": f"Joined {projectId}"})

@app.route("/leave/<projectId>")
def leaveProject(projectId):
    return jsonify({"message": f"Left {projectId}"})

if __name__ == "__main__":
    app.run()
