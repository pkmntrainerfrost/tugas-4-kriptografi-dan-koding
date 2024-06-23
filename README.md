# Tugas 4 II4031 Kriptografi dan Koding
## Dibuat oleh:
- 18221115 Christopher Febrian Nugraha
- 18221102 Salman Ma'arif Achsien

# Deskripsi Tugas 
Program ini merupakan program basis data transkrip nilai sederhana yang memiliki fitur enkripsi dengan modified RC4, digital signature dengan RSA dan SHA-3, serta export laporan terenkripsi menggunakan AES.

# Cara Menjalankan Aplikasi pada Windows OS
## Bagian 1: Persiapan dan Instalasi
1. Clone repositori ini ke perangkat komputer Anda.
2. Buatlah sebuah _virtual environment_ baru dengan menjalankan kode berikut terminal CLI Windows:
    > py -m venv venv
    - Pastikan terlebih dahulu Anda sudah memiliki _Python_ yang terinstal. Jika belum, Anda dapat melihat panduan [berikut ini](https://docs.python.org/3/using/windows.html#using-on-windows).
    - Pastikan juga Anda berada pada _root_ dari folder repositori ini sebelum membuat _virtual environment_.
3. Jalankan _virtual environment_ yang baru saja dibuat dengan menggunakan kode berikut:
    > venv/Scripts/activate
4. Lakukan instalasi modul yang diperlukan untuk aplikasi ini dengan menjalankan kode ini:
    > pip install pyqt6 pyqt6-tools sympy pdfkit pandas pyaescrypt
5. Install wkhtmltopdf dari tautan [berikut ini](https://wkhtmltopdf.org/downloads.html).

## Bagian 2: Eksekusi dan Penggunaan
1. Jalankan file main.py dengan menggunakan kode berikut:
    > py main.py
2. Program akan menampilkan sebuah window baru berisi basis data.
3. Di menu "Data", lakukan dekripsi dengan kunci "Test" dan "Test". Sebagai alternatif, hapus entri dari csv secara manual sebelum menjalankan program.
4. Bangkitkan kunci RSA untuk digital signature di menu "RSA".
5. Tambahkan mahasiswa dengan tombol di kanan bawah. Jika sudah berhasil, Data dapat diekspor sebagai PDF dan diverifikasi tanda tangannya.
6. Simpan data dengan melakukan enkripsi menggunakan tombol sesuai di menu "Data".

## Batasan
- Basis data harus dalam status terdekripsi untuk menambahkan data
- Data tidak tersimpan sampai dilakukan enkripsi
