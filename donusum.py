import sqlite3
import pandas as pd

csv_file = "characters excel.xlsx"  # Dosya adını kendi dosyanla değiştir
df = pd.read_excel(csv_file)

conn = sqlite3.connect("characters.db") # Aynı dosya adını .db uzantılı şekilde yaz

df.to_sql("characters", conn, if_exists="replace", index=False) #tablo_adi kısmı değiştirilebilir

conn.close()
