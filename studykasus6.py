def lihat_barang():
    print()
    print("=== DAFTAR BARANG ===")
    try:
        with open("inventaris.txt", "r") as file:
            data_barang = file.readlines()
            
            if len(data_barang) == 0:
                print("Belum ada data barang.")
            else:
                nomor = 1
                for baris in data_barang:
                    item = baris.strip().split(",")
                    print(f"{nomor}. {item[0]} | Stok: {item[1]} | Harga: Rp {item[2]}")
                    nomor += 1
    except FileNotFoundError:
        print("Belum ada data barang.")

def tambah_barang():
    print()
    print("=== TAMBAH BARANG ===")
    nama = input("Nama barang : ")
    stok_input = input("Stok        : ")
    harga_input = input("Harga (Rp)  : ")

    if nama == "":
        print("Data tidak valid! Nama harus diisi.")
        return

    try:
        stok = int(stok_input)
        harga = int(harga_input)
        
        with open("inventaris.txt", "a") as file:
            file.write(f"{nama},{stok},{harga}\n")
            
        print("Barang berhasil ditambahkan!")
    except ValueError:
        print("Data tidak valid! Stok & harga harus angka.")

while True:
    print()
    print("=== INVENTARIS TOKO KELONTONG ===")
    print("1. Lihat barang")
    print("2. Tambah barang")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        lihat_barang()
    elif pilihan == "2":
        tambah_barang()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak ada!")