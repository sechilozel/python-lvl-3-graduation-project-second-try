from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from logic import DB_Manager
from config import DATABASE

manager = DB_Manager(DATABASE)
app = Flask(__name__)

@app.route("/")
def mainpage():
    # conn = sqlite3.connect('characters.db')
    # cursor = conn.cursor()
    # cursor.execute("SELECT name, surname, family, nation, race, lineage, magicrate FROM characters")
    # characters = cursor.fetchall()
    # conn.close()
    return render_template('index.html')     # , characters=characters)


@app.route("/sbyname", methods=["GET", "POST"])
def sbyname():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    if request.method == 'POST':
        name_query = request.form['name']
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            WHERE name LIKE ?
        """, ('%' + name_query + '%',))
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
        """)

    characters = cur.fetchall()
    conn.close()
    return render_template('namebutton.html', characters=characters)


@app.route("/sbysurname", methods=["GET", "POST"])
def sbysurname():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    if request.method == 'POST':
        surname_query = request.form['surname']
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            WHERE surname LIKE ?
        """, ('%' + surname_query + '%',))
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
        """)

    characters = cur.fetchall()
    conn.close()
    return render_template('surnamebutton.html', characters=characters)

@app.route("/sbyfamily", methods=["GET", "POST"])
def sbyfamily():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    if request.method == 'POST':
        family_query = request.form['family']
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            WHERE family LIKE ?
        """, ('%' + family_query + '%',))
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
        """)

    characters = cur.fetchall()
    conn.close()
    return render_template('familybutton.html', characters=characters)

@app.route("/sbynation", methods=["GET", "POST"])
def sbynation():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    if request.method == 'POST':
        nation_query = request.form['nation']
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            WHERE nation LIKE ?
        """, ('%' + nation_query + '%',))
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
        """)

    characters = cur.fetchall()
    conn.close()
    return render_template('nationbutton.html', characters=characters)

@app.route("/sbyrace", methods=["GET", "POST"])
def sbyrace():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    if request.method == 'POST':
        race_query = request.form['race']
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            WHERE race = ?
        """, (race_query,))
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
        """)

    characters = cur.fetchall()
    conn.close()
    return render_template('racebutton.html', characters=characters)

@app.route("/sbylineage", methods=["GET", "POST"])
def sbylineage():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    if request.method == 'POST':
        lineage_query = request.form['lineage']
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            WHERE lineage LIKE ?
        """, ('%' + lineage_query + '%',))
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
        """)

    characters = cur.fetchall()
    conn.close()
    return render_template('lineagebutton.html', characters=characters)

@app.route("/addcharacter", methods=["GET", "POST"])
def addcharacter():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        family = request.form['family']
        nation = request.form['nation']
        race = request.form['race']
        lineage = request.form['lineage']
        magicrate = request.form['magicrate']
        conn = sqlite3.connect('characters.db')
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO characters (name, surname, family, nation, race, lineage, magicrate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, surname, family, nation, race, lineage, magicrate))
        conn.commit()
        conn.close()
        return redirect(url_for('mainpage'))
    
    return render_template('addbutton.html')

app.run(debug=True)