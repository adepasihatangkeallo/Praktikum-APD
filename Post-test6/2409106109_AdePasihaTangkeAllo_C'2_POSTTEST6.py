import os

users = {
    "ade": {"password": "109", "role": "admin", "playlist": {}}
}

while True:
    print("==========================================================")
    print("| Selamat datang di aplikasi Playlist Lagu saya           |")
    print("| 1. Admin               ----                             |")
    print("| 2. Pengguna           --  --                            |")
    print("| 3. Exit                 --                              |")
    print("==========================================================")
    role = input("Pilih peran Anda (1/2/3): ")

    if role == "1":# INI UNTUK ADMIN
        print("Silahkan login sebagai admin")
        username = input("Username: ")
        password = input("Password: ")
        if username == "ade" and users["ade"]["password"] == password:
            print("Login admin berhasil!")
            while True:
                print("\n===== MENU ADMIN =====")
                print("1. Lihat semua pengguna")
                print("2. Hapus pengguna")
                print("3. Lihat playlist semua pengguna")
                print("4. Kembali ke menu utama")
                pilihan = input("Pilih opsi: ")

                if pilihan == "1":
                    print("\nDaftar Pengguna:")
                    for username, data in users.items():
                        print(f"Username: {username}, Role: {data['role']}")
                elif pilihan == "2":
                    username = input("Masukkan username yang ingin dihapus: ")
                    if username in users and username != "ade":
                        del users[username]
                        print(f"Pengguna {username} berhasil dihapus.")
                    else:
                        print("Username tidak ditemukan atau tidak bisa dihapus.")
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

    elif role == "2":# INI UNTUK PENGGUNA
        print("==========================================================")
        print("| 1. Daftar Akun Dulu Dong                                |")
        print("| 2. Login                                                |")
        print("==========================================================")
        opsi = input("Pilih opsi: ")

        if opsi == "1":
            print("HALO CANTIK DAN GANTENG! Ayo buat akun dulu YAAA")
            username = input("Username: ")
            password = input("Password: ")
            if username in users:
                print("Nama Sudah Terpakai Bro. Untuk Registrasi Silahkan Coba Lagi Ganteng Cantik")
            else:
                users[username] = {"password": password, "role": "user", "playlist": {}}
                print(f"Selamat Akun Anda berhasil terdaftar dengan username: {username}")

        elif opsi == "2":
            print("Hi, Silahkan login dulu ya bos!")
            username = input("Username: ")
            password = input("Password: ")
            if username in users and users[username]["password"] == password and users[username]["role"] == "user":
                while True:
                    print(f"\nSelamat datang Cantik Ganteng {username}!")
                    print(">>>>> SILAHKAN PILIH YA CANTIK DAN GANTENG! <<<<<")
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
                        print("Lagu baru sudah ditambahkan ke playlist!\n")

                    elif status == "2":
                        if not users[username]["playlist"]:
                            print("Playlist kamu masih kosong bos. Tambahkan lagu dulu lah bos!\n")
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
                                judul_baru = input("Masukkan judul lagu yang baru cantik dan ganteng: ")
                                artis_baru = input("Masukkan nama artis yang baru Ya: ")
                                print("Apa kamu yakin ingin mengedit lagu ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "1":
                                    del users[username]["playlist"][judul_lama]
                                    users[username]["playlist"][judul_baru] = artis_baru
                                    print("Lagu yang kamu pilih sudah di edit ya cantik dan ganteng!\n")
                                else:
                                    print("Aksi untuk mengedit lagu dibatalkan")
                            else:
                                print("Tidak ada nomor lagu yang kamu maksud, silahkan input ulang.\n")

                    elif status == "4":
                        if not users[username]["playlist"]:
                            print("Tidak ada lagu yang bisa dihapus.")
                        else:
                            print("Playlist kamu:")
                            for index, (judul, artis) in enumerate(users[username]["playlist"].items(), 1):
                                print(f"{index}. {judul} - {artis}")
                            hapus = int(input("Lagu nomor berapa yang ingin dihapus Cantik Dan Ganteng!: ")) - 1
                            if 0 <= hapus < len(users[username]["playlist"]):
                                judul_hapus = list(users[username]["playlist"].keys())[hapus]
                                print(f"Apa kamu yakin ingin menghapus lagu ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "1":
                                    del users[username]["playlist"][judul_hapus]
                                    print("Lagu yang kamu pilih sudah dihapus dari playlist!\n")
                                else:
                                    print("Aksi untuk menghapus dibatalkan")
                            else:
                                print("Tidak ada nomor lagu yang kamu maksud, silahkan input ulang\n")

                    elif status == "5":
                        print("Logout berhasil.\n")
                        break

                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")

            else:
                print("USERNAME DAN PASSWORD SALAH TUU MASUKIN YANG BETUL YA ><, MASUKAN YANG BENAR YA CANTIK DAN GANTENG\n")

        else:
            print("Input tidak valid, silahkan pilih 1 atau 2")

    elif role == "3":
        print("Yakin ajakah ingin keluar dari aplikasi ini?")
        print("1. Ya")
        print("2. Tidak")
        confirm_exit = input("Pilih: ")
        if confirm_exit == "1":
            print("Terima kasih! Sampai jumpa Lagi kawan!")
            break
        elif confirm_exit == "2":
            print("Kembali ke menu utama.")
        else:
            print("Pilihan tidak VALID.")
