from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Fungsi untuk koneksi ke database Railway
def get_db_connection():
    return mysql.connector.connect(
        host="shuttle.proxy.rlwy.net",
        port=14810,  # Sesuaikan dengan Railway
        user="root",
        password="uwJUEiosnJUeLOCkkhBgOgfZAqalBUGx",
        database="railway"
    )

@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", users=users)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    email = request.form["email"]
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
