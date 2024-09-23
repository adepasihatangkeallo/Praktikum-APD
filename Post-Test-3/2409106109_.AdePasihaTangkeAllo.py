while True:
    try:
        harga_mobil = float(input("Masukkan harga mobil: "))
        pilihan_mobil = input("Pilih mobil (tesla/toyota/hyundai/tidak): ")

        diskon = 0

        if pilihan_mobil == "tesla":
            diskon = 0.17 * harga_mobil
        elif pilihan_mobil == "toyota":
            diskon = 0.21 * harga_mobil
        elif pilihan_mobil == "hyundai":
            diskon = 0.23 * harga_mobil
        elif pilihan_mobil == "tidak":
            print("Bu Navira tidak jadi membeli mobil.")
            break
        else:
            print("Pilihan mobil tidak valid. Silakan pilih tesla, toyota, hyundai, atau tidak.")
            continue

        harga_setelah_diskon = harga_mobil - diskon
        print(f"Harga setelah diskon: Rp {harga_setelah_diskon:.2f}")

        ulangi = input("Apakah Anda ingin menghitung harga mobil lainnya? (ya/tidak): ")
        if ulangi.lower() != "ya":
            break

    except ValueError:
        print("Masukkan harga mobil dalam bentuk angka.")