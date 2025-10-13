from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if(request.method == "POST"):
        #Handle form submission here
        with open("file.txt", "w") as f:
            f.write(f"The name is {request.form['name']} and email is {request.form['email']} ")
        return render_template("contact.html")
        pass
    else:
        return render_template("contact.html")

app.run(debug=True)