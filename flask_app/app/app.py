from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is a simple Web App!</h1>"


@app.route("/boredAPI/<int:participants>")
def boredAPI(participants):
    response = requests.get("http://www.boredapi.com/api/activity?participants=" + str(participants)).text
    response_info = json.loads(response)
    return "An activity suitable for  " + str(response_info["participants"]) + " participants would be " + response_info["activity"] + " which is of type " + response_info["type"] + "."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
