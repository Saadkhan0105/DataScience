from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Saad": 54,
        "Umaima": 93,
        "Humaira": 78,
        "Abuzar": 89,
        "Nadeem": 95,
    }
    return render_template("index.html" , marks=marks)

app.run(debug=True)