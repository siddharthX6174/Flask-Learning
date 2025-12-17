from flask import Flask
import sqlite3

app = Flask("__main__")


conn = sqlite3.connect('mycollege.db')
cur = conn.cursor()
cur.execute("select count(*) from sqlite_master where type='table' and name='students'")
if cur.fetchone()[0]==1:
    print("Table already exists")
else:
    conn.execute('CREATE TABLE if not exists students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    print("Table created successfully")
conn.close()

if __name__ == "__main__":
    app.run(debug=True)