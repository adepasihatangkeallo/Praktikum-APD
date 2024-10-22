import os

# Variabel Global
users = {
    "ade": {"password": "109", "role": "admin", "playlist": {}}
}
global_role = ""
current_username = ""

# FUNGSI UNTUK MENAMPILKAN MENU UTAMA
def tampilkan_menu_utama():
    print("==========================================================")
    print("| Selamat datang di aplikasi Playlist Lagu saya           |")
    print("| 1. Admin               ----                             |")
    print("| 2. Pengguna           --  --                            |")
    print("| 3. Exit                 --                              |")
    print("==========================================================")

# Fungsi untuk mengecek kredensial pengguna
def cek_kredensial(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False

# Fungsi untuk menampilkan daftar pengguna
def tampilkan_pengguna():
    print("\nDaftar Pengguna:")
    for username, data in users.items():
        print(f"Username: {username}, Role: {data['role']}")

# Fungsi rekursif untuk login admin
def login_admin():
    global current_username
    username = input("Username: ")
    password = input("Password: ")
    if cek_kredensial(username, password) and users[username]["role"] == "admin":
        current_username = username
        print("Login admin berhasil!")
        return True
    else:
        print("Login gagal. Username atau password salah. Coba lagi.")
        return login_admin()  # Memanggil dirinya sendiri

# Prosedur untuk menambahkan pengguna baru
def tambah_pengguna():
    global users
    username = input("Username baru: ")
    password = input("Password baru: ")
    if username in users:
        print("Nama sudah terpakai. Coba lagi!")
    else:
        users[username] = {"password": password, "role": "user", "playlist": {}}
        print(f"Selamat, akun Anda berhasil terdaftar dengan username: {username}")

# Prosedur untuk menghapus pengguna
def hapus_pengguna():
    username = input("Masukkan username yang ingin dihapus: ")
    if username in users and username != "ade":
        del users[username]
        print(f"Pengguna {username} berhasil dihapus.")
    else:
        print("Username tidak ditemukan atau tidak bisa dihapus.")

# Program Utama
while True:
    tampilkan_menu_utama()
    try:
        role = input("Pilih peran Anda (1/2/3): ")
        if role not in ["1", "2", "3"]:
            raise ValueError("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

        if role == "1":  # Admin
            print("Silahkan login sebagai admin")
            if login_admin():
                while True:
                    print("\n===== MENU ADMIN =====")
                    print("1. Lihat semua pengguna")
                    print("2. Hapus pengguna")
                    print("3. Lihat playlist semua pengguna")
                    print("4. Kembali ke menu utama")
                    pilihan = input("Pilih opsi: ")

                    if pilihan == "1":
                        tampilkan_pengguna()
                    elif pilihan == "2":
                        hapus_pengguna()
                    elif pilihan == "3":
                        print("\nPlaylist Semua Pengguna:")
                        for username, data in users.items():
                            print(f"\nPlaylist milik {username}:")
                            if data['playlist']:
                                for index, (judul, artis) in enumerate(data['playlist'].items(), 1):
                                    print(f"{index}. {judul} - {artis}")
                            else:
                                print("Playlist kosong")
                    elif pilihan == "4":
                        break
                    else:
                        print("Pilihan tidak valid.")

        elif role == "2":  # Pengguna
            print("==========================================================")
            print("| 1. Daftar Akun Dulu Dong                                |")
            print("| 2. Login                                                |")
            print("==========================================================")
            opsi = input("Pilih opsi: ")

            if opsi == "1":
                tambah_pengguna()

            elif opsi == "2":
                print("Hi, Silahkan login dulu ya!")
                username = input("Username: ")
                password = input("Password: ")
                if cek_kredensial(username, password) and users[username]["role"] == "user":
                    current_username = username
                    while True:
                        print(f"\nSelamat datang, {username}!")
                        print("1. Tambah lagu baru ke playlist")
                        print("2. Lihat playlist")
                        print("3. Edit lagu di playlist")
                        print("4. Hapus lagu dari playlist")
                        print("5. Logout")
                        status = input("Pilih opsi: ")

                        if status == "1":
                            judul_lagu = input("Judul lagu: ")
                            artis = input("Nama artis: ")
                            users[username]["playlist"][judul_lagu] = artis
                            print("Lagu baru ditambahkan ke playlist!\n")

                        elif status == "2":
                            if not users[username]["playlist"]:
                                print("Playlist kamu masih kosong. Tambahkan lagu dulu!\n")
                            else:
                                print("Playlist kamu:")
                                for index, (judul, artis) in enumerate(users[username]["playlist"].items(), 1):
                                    print(f"{index}. {judul} - {artis}")
                                print()

                        elif status == "3":
                            if not users[username]["playlist"]:
                                print("Tidak ada lagu yang bisa diedit.")
                            else:
                                print("Playlist kamu:")
                                for index, (judul, artis) in enumerate(users[username]["playlist"].items(), 1):
                                    print(f"{index}. {judul} - {artis}")
                                edit = int(input("Lagu nomor berapa yang ingin kamu edit: ")) - 1
                                if 0 <= edit < len(users[username]["playlist"]):
                                    judul_lama = list(users[username]["playlist"].keys())[edit]
                                    judul_baru = input("Masukkan judul lagu yang baru: ")
                                    artis_baru = input("Masukkan nama artis yang baru: ")
                                    print("Apa kamu yakin ingin mengedit lagu ini?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_edit = input("Pilih: ")
                                    if memastikan_edit == "1":
                                        del users[username]["playlist"][judul_lama]
                                        users[username]["playlist"][judul_baru] = artis_baru
                                        print("Lagu berhasil diedit!\n")
                                    else:
                                        print("Aksi untuk mengedit lagu dibatalkan")
                                else:
                                    print("Nomor lagu tidak valid.\n")

                        elif status == "4":
                            if not users[username]["playlist"]:
                                print("Tidak ada lagu yang bisa dihapus.")
                            else:
                                print("Playlist kamu:")
                                for index, (judul, artis) in enumerate(users[username]["playlist"].items(), 1):
                                    print(f"{index}. {judul} - {artis}")
                                hapus = int(input("Lagu nomor berapa yang ingin dihapus: ")) - 1
                                if 0 <= hapus < len(users[username]["playlist"]):
                                    judul_hapus = list(users[username]["playlist"].keys())[hapus]
                                    print("Apa kamu yakin ingin menghapus lagu ini?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_hapus = input("Pilih: ")
                                    if memastikan_hapus == "1":
                                        del users[username]["playlist"][judul_hapus]
                                        print("Lagu berhasil dihapus dari playlist!\n")
                                    else:
                                        print("Aksi untuk menghapus dibatalkan")
                                else:
                                    print("Nomor lagu tidak valid.\n")

                        elif status == "5":
                            print("Logout berhasil.\n")
                            break

                        else:
                            print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")

                else:
                    print("USERNAME DAN PASSWORD SALAH. MASUKKAN YANG BENAR!\n")

            else:
                print("Input tidak valid, silahkan pilih 1 atau 2")

        elif role == "3":
            print("Yakin ingin keluar dari aplikasi ini?")
            confirm_exit = input("1. Ya\n2. Tidak\nPilih: ")
            if confirm_exit == "1":
                print("Terima kasih!   YAAA!")
                break
            elif confirm_exit == "2":
                print("Kembali ke menu utama.")
            else:
                print("Pilihan tidak valid.")

    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
