from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def mainpage():
    conn = sqlite3.connect('characters.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, surname, family, nation, race, lineage, magicrate FROM characters")
    characters = cursor.fetchall()
    conn.close()
    return render_template('index.html', characters=characters)


@app.route("/sbyname")
def sbyname():
    return render_template("namebutton.html")

@app.route("/sbysurname")
def sbysurname():
    return render_template("surnamebutton.html")

@app.route("/sbyfamily")
def sbyfamily():
    return render_template("familybutton.html")

@app.route("/sbynation")
def sbynation():
    return render_template("nationbutton.html")

@app.route("/sbyrace")
def sbyrace():
    return render_template("racebutton.html")

@app.route("/sbylineage")
def sbylineage():
    return render_template("lineagebutton.html")

app.run(debug=True)