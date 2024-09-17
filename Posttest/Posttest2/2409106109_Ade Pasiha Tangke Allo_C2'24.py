nama = input("masukan nama ")
nim = input("masukan nim ")
harga_setiap_mobil = 300000000
diskon_tesla = 0.17
diskon_toyota = 0.21
diskon_hyundai = 0.23
harga_tesla_setelah_diskon = harga_setiap_mobil * (1 - diskon_tesla)
harga_toyota_setelah_diskon = harga_setiap_mobil * (1 - diskon_toyota)
harga_hyundai_setelah_diskon = harga_setiap_mobil * (1 - diskon_hyundai)
hasil_akhir = int(harga_setiap_mobil) % 7
print(f"Mobil Tesla seharga {harga_setiap_mobil:.2f} diskon {diskon_tesla*100:.0f}% menjadi {harga_tesla_setelah_diskon:.2f},")
print(f"Mobil Toyota seharga {harga_setiap_mobil:.2f} diskon {diskon_toyota*100:.0f}% menjadi {harga_toyota_setelah_diskon:.2f},")
print(f"Mobil Hyundai seharga {harga_setiap_mobil:.2f} diskon {diskon_hyundai*100:.0f}% menjadi {harga_hyundai_setelah_diskon:.2f},")
print(f"dan harga setiap mobil modulus 7 adalah {hasil_akhir}.")


