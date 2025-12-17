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


@app.route('/listStudent')
def list_student():
    conn = sqlite3.connect('mycollege.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return render_template('view.html', rows=rows)


@app.route('/deleteInput')
def delete_input():
    return render_template('deleteInput.html')

@app.route('/deleteStudent', methods=['POST'])
def delete_student():
    if request.method == 'POST':
        try:
            name = request.form.get('studname')
            with sqlite3.connect('mycollege.db') as conn:
                cur = conn.cursor()
                # my_query = "SELECT * FROM students WHERE name = ?"
                # cur.execute(my_query, (name,))
                cur.execute("DELETE FROM students WHERE name = ?", (name,))
                conn.commit()
                msg = "Total rows deleted: " + str(conn.total_changes)
        except:
            conn.rollback()
            msg = "Could not delete Data"
        finally:
            conn.close()

    return render_template('success.html', msg=msg)


@app.route('/updateInput')
def update_input():
    return render_template('updateInput.html')

@app.route('/updateStudent', methods=['POST'])
def update_student():
    if request.method == 'POST':
        try:
            name = request.form.get('studname')
            # addr = request.form.get('studaddr')
            city = request.form.get('studcity')
            # pin = request.form.get('studpin')
            with sqlite3.connect('mycollege.db') as conn:
                cur = conn.cursor()
                cur.execute("UPDATE students SET city = ? WHERE name = ?", (city, name))
                conn.commit()
                msg = "Total rows updated: " + str(conn.total_changes)
        except:
            conn.rollback()
            msg = "Could not update Data"
        finally:
            conn.close()

    return render_template('success.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True)