import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
    
    #FILTER BY NAME
    def get_namechars(self, name):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE name = ?", (name,))
            return cur.fetchall()
    
    #FILTER BY SURNAME
    def get_surnamechars(self, surname):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE surname = ?", (surname,))
            return cur.fetchall()
    
    #FILTER BY FAMILY
    def get_familychars(self, family):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE family = ?", (family,))
            return cur.fetchall()
    
    #FILTER BY NATION
    def get_nationchars(self, nation):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE nation = ?", (nation,))
            return cur.fetchall()
    
    #FILTER BY RACE
    def get_racechars(self, race):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE race = ?", (race,))
            return cur.fetchall()
    
    #FILTER BY LINEAGE
    def get_lineagechars(self, lineage):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE lineage = ?", (lineage,))
            return cur.fetchall()
    
    #FILTER BY MAGIC RATE (minimum)
    def get_magicratechars(self, magicrate):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE magicrate >= ?", (magicrate,))
            return cur.fetchall()
    #FILTER BY MAGIC RATE (maximum)
    def get_magicratechars(self, magicrate):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM characters WHERE magicrate <= ?", (magicrate,))
            return cur.fetchall()