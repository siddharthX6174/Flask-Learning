from flask import Flask, request
import requests

app = Flask("__main__")

@app.route("/makeJson")
def make_json():
    person = {
        "name": "Siddharth",
        "language": ["Python", "C++", "Go"],
        "framework": ["Flask", "FastAPI", "Gin"]
    }
    response = requests.post("http://127.0.0.1:5000/processJson", json=person)  # requests (external library) 👉 used to send HTTP requests
    return response.text

@app.route("/processJson", methods=["POST"])
def process_json():
    if request.is_json:
        return request.json.get('name')
    else:
        return "No JSON data found"

if __name__ == "__main__":
    app.run(debug=True)