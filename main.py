import mysql.connector

try:
    conn = mysql.connector.connect(
        host="shuttle.proxy.rlwy.net",
        port=14810,
        user="root",
        password="uwJUEiosnJUeLOCkkhBgOgfZAqalBUGx",
        database="railway"
    )
    print("✅ Koneksi ke MySQL Railway berhasil!")

    cursor = conn.cursor()

    # Buat tabel
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    print("📦 Tabel 'users' dibuat atau sudah ada.")

    # Insert data
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Rahayu", "rahayu@example.com"))
    conn.commit()
    print("✅ Data berhasil disisipkan.")

    # Select data
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    print("📋 Isi tabel 'users':")
    for user in users:
        print(user)

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
