from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
    marks = {
    "Nadeem": 95,
    "Masroor Jahan": 95,
    "Saad": 84,
    "Umaima": 73,
    "Humaira": 68,
    "Abuzar": 70,
    "Zaid": 49
}
    values = [1, marks, 67]
    return jsonify(values)

app.run(debug=True)