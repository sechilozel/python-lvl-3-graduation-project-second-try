from flask import Flask, render_template, request, redirect, url_for
import sqlite3

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
            ORDER BY name ASC
        """, ('%' + name_query + '%',))
        if name_query not in [row[0] for row in cur.fetchall()]:
            return render_template('error.html')
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            ORDER BY name ASC
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
            ORDER BY surname ASC
        """, ('%' + surname_query + '%',))
        if surname_query not in [row[1] for row in cur.fetchall()]:
            return render_template('error.html')
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            ORDER BY surname ASC
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
            ORDER BY family ASC
        """, ('%' + family_query + '%',))
        if family_query not in [row[2] for row in cur.fetchall()]:
            return render_template('error.html')
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            ORDER BY family ASC
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
            ORDER BY nation ASC
        """, ('%' + nation_query + '%',))
        if nation_query not in [row[3] for row in cur.fetchall()]:
            return render_template('error.html')
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            ORDER BY nation ASC
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
            ORDER BY race ASC
        """, (race_query,))
        if race_query not in [row[4] for row in cur.fetchall()]:
            return render_template('error.html')
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            ORDER BY race ASC
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
            ORDER BY lineage ASC
        """, ('%' + lineage_query + '%',))
        if lineage_query not in [row[5] for row in cur.fetchall()]:
            return render_template('error.html')
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            ORDER BY lineage ASC
        """)

    characters = cur.fetchall()
    conn.close()
    return render_template('lineagebutton.html', characters=characters)

@app.route("/sbymagicrate", methods=["GET", "POST"])
def sbymagicrate():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    if request.method == 'POST':
        magicratemax_query = request.form.get('magicratemax')
        magicratemin_query = request.form.get('magicratemin')

        if magicratemin_query == '':
            magicratemin_query = 0.0
        if magicratemax_query == '':
            magicratemax_query = 5.0

        if magicratemin_query > magicratemax_query:
            magicratemax_query, magicratemin_query = magicratemin_query, magicratemax_query
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            WHERE magicrate <= ? AND magicrate >= ?
            ORDER BY magicrate DESC
        """, (magicratemax_query, magicratemin_query))
    else:
        cur.execute("""
            SELECT name, surname, family, nation, race, lineage, magicrate
            FROM characters
            ORDER BY magicrate DESC
        """)
    characters = cur.fetchall()
    conn.close()
    return render_template('magicbutton.html', characters=characters)

@app.route("/seethelist")
def seethelist():
    conn = sqlite3.connect('characters.db')
    cur = conn.cursor()
    cur.execute("""
        SELECT name, surname, family, nation, race, lineage, magicrate
        FROM characters
        ORDER BY race ASC
    """)
    characters = cur.fetchall()
    conn.close()
    return render_template('charlist.html', characters=characters)

LINEAGE_OPTIONS = {
    "Anormal": ["Angel", "Demon", "Fairy", "Magician","Royal"],
    "Noramal": ["Kinoto", "Wizard"],
    "Normal": ["Human"]
}

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

    # selected_race = None
    # lineage_choices = []

    # if request.method == 'POST':
    #     selected_race = request.form.get('race')
    #     lineage_choices = LINEAGE_OPTIONS.get(selected_race, [])

    #     if request.form.get('lineage'):
    #         name = request.form['name']
    #         surname = request.form['surname']
    #         family = request.form['family']
    #         nation = request.form['nation']
    #         race = request.form['race']
    #         lineage = request.form['lineage']
    #         magicrate = request.form['magicrate']
    #         conn = sqlite3.connect('characters.db')
    #         cur = conn.cursor()
    #         cur.execute("""
    #             INSERT INTO characters (name, surname, family, nation, race, lineage, magicrate)
    #             VALUES (?, ?, ?, ?, ?, ?, ?)
    #         """, (name, surname, family, nation, race, lineage, magicrate))
    #         conn.commit()
    #         conn.close()
    #         return redirect(url_for('mainpage'))
    
    # return render_template('addbutton.html',
    #                        races=LINEAGE_OPTIONS.keys(),
    #                        selected_race=selected_race,
    #                        lineage_choices=lineage_choices)

app.run(debug=True)