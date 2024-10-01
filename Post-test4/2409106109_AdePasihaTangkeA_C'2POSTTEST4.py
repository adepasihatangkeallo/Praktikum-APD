loop = 0
while loop < 3:
    username = input("Masukan Nama Anda: ")
    try:
        password = int(input("Masukan Password Anda: "))
    except ValueError:
        print("Password harus berupa angka.")
        continue

    if username == "ade" and password == 109:
        continue_program = input("Apakah Anda Ingin Melanjutkan Program Ini? (ya/tidak): ").lower()
        if continue_program == "ya":
            print("Pilih Merk Mobil:")
            print("1. Tesla")
            print("2. Toyota")
            print("3. Hyundai")
            try:
                car_choice = int(input("Masukan Merk Mobil (1-3): "))
                if car_choice not in [1, 2, 3]:
                    print("Pilihan mobil tidak valid.")
                    continue
            except ValueError:
                print("Masukan harus berupa angka.")
                continue
            
            price = float(input("Masukan Harga: "))
            

            discounts = {1: 0.17, 2: 0.21, 3: 0.23}
            discount = discounts.get(car_choice, 0)
            discounted_price = price - (price * discount)

            print(f"Harga mobil {car_choice}: Rp {discounted_price:.2f}")
        else:
            print("Program Anda telah selesai.")
            break
    else:
        exit_program = input("Apakah Anda Ingin Mengakhiri Program Ini? (iya/tidak): ").lower()
        if exit_program == "iya":
            print("Program Anda Telah Selesai.")
            break
        else:
            loop = loop + 1
            perulangan = 3 - loop
            print(f"Batas Percobaan Yang Tersisa: {perulangan}")
