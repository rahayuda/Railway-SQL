import mysql.connector

print("👋 Hello from Railway Python!")

# Koneksi ke Railway DB
conn = mysql.connector.connect(
    host="shuttle.proxy.rlwy.net",
    port=14810,
    user="root",
    password="uwJUEiosnJUeLOCkkhBgOgfZAqalBUGx",
    database="railway"
)

cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("📋 Isi tabel 'users':")
    if not rows:
        print("⚠️ Tabel kosong.")
    else:
        for row in rows:
            print(row)

except Exception as e:
    print(f"❌ Terjadi kesalahan saat SELECT: {e}")

finally:
    cursor.close()
    conn.close()
