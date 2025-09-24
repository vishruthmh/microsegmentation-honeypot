from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/query")
def query():
    conn = sqlite3.connect("/data/demo.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS demo (msg TEXT)")
    c.execute("INSERT INTO demo VALUES ('hello from SQLite')")
    conn.commit()
    c.execute("SELECT * FROM demo")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)
