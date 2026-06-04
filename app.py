from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def hent_database():
    return mysql.connector.connect(
        host="localhost",
        user="aisha_monitor",
        password="PASSORD123",
        database="exsamen_cpuram"
    )

@app.route("/")
def hovedside():
    conn = hent_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM system_cpu ORDER BY created_at DESC LIMIT 1")
    siste_data = cursor.fetchone()

    conn.close()

    return render_template("hovedside.html", data=siste_data)

@app.route("/arbeidere")
def arbeidere():
    conn = hent_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM arbeidere")
    ansatte = cursor.fetchall()

    conn.close()

    return render_template("arbeidere.html", ansatte=ansatte)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
