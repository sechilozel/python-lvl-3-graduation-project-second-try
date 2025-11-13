from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("/sbyname")
def sbyname():
    return render_template("namebutton.html")

@app.route("/sbysurname")
def sbysurname():
    return render_template("surnamebutton.html")

app.run(debug=True)