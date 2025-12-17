from flask import Flask, render_template, request
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addStudent')
def add_student():
    return render_template('addStudent.html')

@app.route('/saveStudent', methods=['POST', 'GET'])
def save_student():
    if request.method == 'POST':
        try:
            name = request.form.get('studname')
            addr = request.form.get('studaddr')
            city = request.form.get('studcity')
            pin = request.form.get('studpin')
            with sqlite3.connect('mycollege.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)", (name, addr, city, pin))
                conn.commit()

                msg = "Record inserted successfully"
        except:
            conn.rollback()
            msg = "Could not insert Data"

    return render_template('success.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)