import os
users = []

while True:
    print("==========================================================")
    print("|Selamat datang di aplikasi Playlist Lagu saya           |")
    print("|1. Daftar Akun Dulu Dong                                |")
    print("|2. Login                                                |")
    print("|3. Exit                                                 |")
    print("==========================================================")
    print(" ")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("HALO CANTIK DAN GANTENG! Ayo buat akun dulu YAAA")
        username = input("Username: ")
        user_exists = any(user[0] == username for user in users)
        if user_exists:
            print("Nama Sudah Terpakai Bro. Untuk Registrasi Silahkan Coba Lagi Ganteng Cantik")
        else:
            password = input("Password: ")
            users.append([username, password, []])
            print(f"Selamat Akun Anda berhasil terdaftar dengan username: {username}")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya bos!")
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user[0] == username and user[1] == password:
                print("====================================================")
                while True:
                    print(f"\nSelamat datang Cantik Ganteng {username}!")
                    print(">>>>>SILAHKAN PILIH YA CANTIK DAN GANTENG!<<<<<<<")
                    print("1. Tambah lagu baru ke playlist")
                    print("2. Lihat playlist")
                    print("3. Edit lagu di playlist")
                    print("4. Hapus lagu dari playlist")
                    print("5. Logout")
                    print("=================================================")

                    status = input("Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        judul_lagu = input("Judul lagu: ")
                        artis = input("Nama artis: ")
                        user[2].append([judul_lagu, artis])
                        print("Lagu baru sudah ditambahkan ke playlist!\n")

                    elif status == "2":
                        if not user[2]:
                            print("Playlist kamu masih kosong bos. Tambahkan lagu dulu lah bos!\n")
                        else:
                            print("Playlist kamu:")
                            for indeks, lagu in enumerate(user[2]):
                                print(f"{indeks + 1}. {lagu[0]} - {lagu[1]}")
                            print()

                    elif status == "3":
                        if not user[2]:
                            print("Tidak ada lagu yang bisa diedit.")
                        else:
                            edit = int(input("Lagu nomor berapa yang ingin kamu edit: ")) - 1
                            if 0 <= edit < len(user[2]):
                                judul_baru = input("Masukkan judul lagu yang baru cantik dan ganteng: ")
                                artis_baru = input("Masukkan nama artis yang baru Ya: ")
                                print("Apa kamu yakin ingin mengedit lagu ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "1":
                                    user[2][edit] = [judul_baru, artis_baru]
                                    print("Lagu yang kamu pilih sudah di edit ya cantik dan ganteng!\n")
                                elif memastikan_edit == "2":
                                    print("Aksi untuk mengedit lagu dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("Tidak ada nomor lagu yang kamu maksud, silahkan input ulang.\n")
                    
                    elif status == "4":
                        if not user[2]:
                            print("Tidak ada lagu yang bisa dihapus.")
                        else:
                            hapus = int(input("Lagu nomor berapa yang ingin dihapus Cantik Dan Ganteng!: ")) - 1
                            if 0 <= hapus < len(user[2]):
                                print(f"Apa kamu yakin ingin menghapus lagu ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "1":
                                    del user[2][hapus]
                                    print("Lagu yang kamu pilih sudah dihapus dari playlist!\n")
                                elif memastikan_hapus == "2":
                                    print("Aksi untuk menghapus dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("Tidak ada nomor lagu yang kamu maksud, silahkan input ulang\n")

                    elif status == "5":
                        print("Logout berhasil.\n")
                        break

                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break
        else:
            print("USERNAME DAN PASSWORD SALAH TUU MASUKIN YANG BETUL YA ><, MASUKAN YANG BENAR YA CANTIK DAN GANTENG\n")

    elif opsi == "3":
        print("Yakin ajakah ingin keluar dari aplikasi ini nanti nyesal loh? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih ya cantik dan ganteng sudah menggunakan aplikasi Playlist Lagu, SEMOGA HARIMU SENIN TERUS YAA >< !")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")