import mysql.connector

# Fungsi-fungsi CRUD
def create_user(name, email):
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        print("✅ Data user berhasil ditambahkan.")
    except Exception as e:
        print(f"❌ Gagal menambahkan data: {e}")

def read_users():
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\n📋 Isi tabel 'users':")
        if not rows:
            print("⚠️ Tabel kosong.")
        else:
            for row in rows:
                print(row)
    except Exception as e:
        print(f"❌ Gagal membaca data: {e}")

def update_user(user_id, new_name, new_email):
    try:
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (new_name, new_email, user_id))
        conn.commit()
        print("✅ Data user berhasil diupdate.")
    except Exception as e:
        print(f"❌ Gagal mengupdate data: {e}")

def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        print("✅ Data user berhasil dihapus.")
    except Exception as e:
        print(f"❌ Gagal menghapus data: {e}")

# Koneksi ke DB
conn = mysql.connector.connect(
    host="shuttle.proxy.rlwy.net",
    port=14810,
    user="root",
    password="uwJUEiosnJUeLOCkkhBgOgfZAqalBUGx",
    database="railway"
)
cursor = conn.cursor()

print("👋 Selamat datang di Aplikasi CRUD Railway!")

# Tampilkan semua data diawal
read_users()

while True:
    print("\nPilih menu:")
    print("1. Tambah User")
    print("2. Update User")
    print("3. Hapus User")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        name = input("Nama: ")
        email = input("Email: ")
        create_user(name, email)
        read_users()  # Tampilkan setelah create
    elif pilihan == "2":
        user_id = input("ID user yang ingin diupdate: ")
        new_name = input("Nama baru: ")
        new_email = input("Email baru: ")
        update_user(user_id, new_name, new_email)
        read_users()  # Tampilkan setelah update
    elif pilihan == "3":
        user_id = input("ID user yang ingin dihapus: ")
        delete_user(user_id)
        read_users()  # Tampilkan setelah delete
    elif pilihan == "4":
        print("👋 Keluar dari aplikasi.")
        break
    else:
        print("❌ Pilihan tidak valid. Silakan coba lagi.")

# Tutup koneksi
cursor.close()
conn.close()
