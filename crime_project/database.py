import sqlite3
import pandas as pd

DB="crime.db"

def connect():
    return sqlite3.connect(DB,check_same_thread=False)

def insert(data):
    conn=connect()
    cur=conn.cursor()
    cur.execute("""
    INSERT INTO crimes(date,crime_type,latitude,longitude,location)
    VALUES(?,?,?,?,?)
    """,data)
    conn.commit()
    conn.close()

def fetch_df():
    conn=connect()
    df=pd.read_sql("SELECT * FROM crimes",conn)
    conn.close()
    return df

def delete(id):
    conn=connect()
    cur=conn.cursor()
    cur.execute("DELETE FROM crimes WHERE id=?",(id,))
    conn.commit()
    conn.close()
