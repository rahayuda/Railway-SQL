from flask import Flask, render_template_string, request, redirect
import mysql.connector

app = Flask(__name__)

# Koneksi ke MySQL Railway
conn = mysql.connector.connect(
    host="shuttle.proxy.rlwy.net",
    port=14810,
    user="root",
    password="uwJUEiosnJUeLOCkkhBgOgfZAqalBUGx",
    database="railway"
)
cursor = conn.cursor()

# Template HTML
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CRUD Railway</title>
</head>
<body>
    <h1>📋 Daftar Users</h1>
    <ul>
        {% for user in users %}
            <li>{{ user[0] }}. {{ user[1] }} ({{ user[2] }}) 
                <a href="/delete/{{ user[0] }}">Hapus</a>
            </li>
        {% endfor %}
    </ul>
    <h2>➕ Tambah User</h2>
    <form method="post" action="/add">
        Nama: <input type="text" name="name"><br>
        Email: <input type="text" name="email"><br>
        <input type="submit" value="Tambah">
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template_string(TEMPLATE, users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    return redirect('/')

@app.route('/delete/<int:user_id>')
def delete(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
