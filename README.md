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

## Bagian 2: Eksekusi dan Penggunaan
1. Jalankan file main.py dengan menggunakan kode berikut:
    > py main.py
2. Program akan menampilkan sebuah window baru berisi basis data.
