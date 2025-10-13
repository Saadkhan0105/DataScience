from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Nadeem": 95,
        "Masroor Jahan": 95,
        "Saad": 84,
        "Umaima": 73,
        "Humaira": 68,
        "Abuzar": 59,
        "Zaid": 49
    }
    return render_template("index.html" , marks=marks)

app.run(debug=True)