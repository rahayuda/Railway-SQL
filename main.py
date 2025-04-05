import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="shuttle.proxy.rlwy.net",
        port=14810,
        user="root",
        password="uwJUEiosnJUeLOCkkhBgOgfZAqalBUGx",
        database="railway"
    )

def create_user(name, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("✅ Data berhasil disisipkan.")
    cursor.close()
    conn.close()

def read_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("📋 Isi tabel 'users':")
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

def update_user(id, new_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s WHERE id = %s", (new_name, id))
    conn.commit()
    print(f"🔄 Data dengan ID {id} berhasil diupdate.")
    cursor.close()
    conn.close()

def delete_user(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    print(f"🗑️ Data dengan ID {id} berhasil dihapus.")
    cursor.close()
    conn.close()

print("👋 Hello from Railway Python with CRUD!")

create_user("Momotaros", "momotaros@example.com")
update_user(1, "Updated Name")
delete_user(2)
read_users()
