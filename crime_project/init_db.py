import sqlite3

conn = sqlite3.connect("crime.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS crimes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
crime_type TEXT,
latitude REAL,
longitude REAL,
location TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
