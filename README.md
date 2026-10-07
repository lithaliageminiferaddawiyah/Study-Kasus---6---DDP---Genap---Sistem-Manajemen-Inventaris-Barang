# Study-Kasus---6---DDP---Genap---Sistem-Manajemen-Inventaris-Barang
**Nama:** [Lithalia Geminifer Addawiyah]  
**NIM:** [2609116088 (Genap)]  
**Kelas:** [C]  
Program ini dirancang untuk mencatat dan mengelola ketersediaan stok barang pada toko kelontong berbasis bahasa pemrograman Python dan penyimpanan data berformat JSON.

---

## Deskripsi Singkat

Program ini berfungsi sebagai sistem pencatatan inventaris gudang interaktif. Seluruh data barang tersimpan secara permanen dalam file berformat JSON, sehingga data yang telah diinput tidak akan hilang ketika program dihentikan dan dijalankan kembali.

---

## Isi Repository

1. `studykasus6.py` : File program utama Python yang berisi logika alur dan fungsi-fungsi sistem.
2. `daftar_barang.json` : File penyimpanan database utama berbasis JSON.
3. `README.md` : Dokumentasi lengkap mengenai struktur dan cara penggunaan program.

---

## Alur Penggunaan Program

1. Pastikan lingkungan eksekusi Python sudah terpasang pada perangkat.
2. Unduh atau clone repository ini ke dalam direktori lokal.
3. Buka terminal atau Command Prompt pada folder direktori repository.
4. Jalankan perintah untuk mengeksekusi file program utama.
5. Pilih opsi menu yang tersedia dengan memasukkan angka 1, 2, atau 3.

Program ini hanya menggunakan pustaka bawaan Python (`json` dan `os`), sehingga tidak memerlukan instalasi pustaka pihak ketiga.

---

## Ringkasan Fitur

- Opsi 1 (Lihat Data Barang) : Menampilkan seluruh daftar barang yang tersimpan dalam file JSON secara terstruktur beserta jumlah stok dan harganya.
- Opsi 2 (Tambah Barang Baru) : Menerima input nama, stok, dan harga barang baru dari pengguna, lalu menyimpannya secara otomatis ke dalam file JSON.
- Opsi 3 (Keluar) : Menghentikan perulangan program secara aman.

Sistem menggunakan perulangan utama sehingga menu akan terus ditampilkan sampai pengguna memilih opsi untuk keluar.

---

## Penjelasan Struktur dan Logika Kode

1. Pengaturan Pustaka dan Lokasi File
   Program memanfaatkan pustaka `json` untuk membaca dan menulis data, serta pustaka `os` untuk memverifikasi keberadaan file. Variabel `path` dikonfigurasi menggunakan Jalur Relatif (*Relative Path*) agar program dapat dijalankan di perangkat mana pun tanpa perlu mengubah direktori secara manual.

2. Pemuatan Data (`muat_data_inventaris`)
   Fungsi ini bertugas membaca struktur data dari file JSON. Apabila file terdeteksi dan valid, isi file dimuat ke dalam bentuk *list*. Jika file belum terbentuk atau mengalami eror pemformatan (`JSONDecodeError`), fungsi akan mengembalikan *list* kosong untuk menjaga kestabilan program.

3. Penyimpanan Data (`simpan_ke_json`)
   Fungsi ini menangani penulisan data kembali ke file JSON. Data ditulis dalam struktur yang rapi dengan penataan indentasi agar mudah dibaca. Penulisan dilakukan secara menyeluruh sehingga data lama tetap terjaga.

4. Menampilkan Data (`lihat_inventaris`)
   Fungsi ini mengambil seluruh item dari pemuat data dan menampilkannya satu per satu secara berurutan. Format tampilan dilengkapi dengan penomoran otomatis serta pemisah ribuan pada nilai harga barang untuk memudahkan pembacaan.

5. Penambahan Data (`tambah_barang_baru`)
   Fungsi ini membaca data yang sudah ada terlebih dahulu, kemudian menerima input barang baru. Terdapat penanganan pengecualian (*exception handling*) untuk mengonversi stok dan harga menjadi bilangan bulat, sehingga meminimalkan potensi eror saat pengguna memasukkan format input yang tidak sesuai.

6. Perulangan Utama Program
   Menggunakan kontrol perulangan `while True` untuk menjaga program tetap aktif menerima perintah hingga pengguna memilih opsi keluar.

---

## Tangkapan Layar (Screenshot) Hasil Pengujian


---

### 1. Tampilan Menu Utama dan Menampilkan Data
(TEMPEL FILE SCREENSHOT 1 DI SINI)
Melihat daftar barang.

---

### 2. Proses Penambahan Barang Baru
(TEMPEL FILE SCREENSHOT 2 DI SINI)
Mengisi nama barang, stok, dan harga sampai muncul konfirmasi berhasil.

---

### 3. Persistensi Data Setelah Program Dijalankan Ulang
(TEMPEL FILE SCREENSHOT 3 DI SINI)
Saat program dihentikan lalu dijalankan kembali, dilanjutkan dengan memilih opsi 1 untuk membuktikan data baru tetap tersimpan.

---

### 4. Struktur Isi File JSON
(TEMPEL FILE SCREENSHOT 4 DI SINI)
Tampilan file `daftar_barang.json` di editor teks yang memperlihatkan data tersimpan dalam bentuk list dan dictionary.

---

## Kesimpulan

Pengerjaan studi kasus ini memberikan pemahaman mendasar mengenai:
- Pengelolaan file dan format data JSON dalam Python.
- Penerapan fungsi modular untuk efisiensi penulisan kode.
- Penggunaan kontrol perulangan interaktif pada aplikasi berbasis CLI (*Command Line Interface*).
- Penanganan pengecualian (*exception handling*) untuk meningkatkan keandalan program.
