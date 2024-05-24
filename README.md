# Tugas 4 II4031 Kriptografi dan Koding
## Dibuat oleh:
- 18221115 Christopher Febrian Nugraha
- 18221102 Salman Ma'arif Achsien

# Deskripsi Tugas 
Mahasiswa ditugaskan untuk sebuah program yang mengaplikasikan penggunaan algoritma RSA untuk simulasi enkripsi/dekripsi pesan pada aplikasi chat/instant messaging. Algoritma ini dijalankan melalui perantara GUI dengan bahasa pemrograman yang dibebaskan. Mahasiswa diharapkan membuat algoritma RSA sendiri tanpa menggunakan library apapun kecuali **tes bilangan prima**, **invers modulo**, maupun library lain yang tidak berhubungan dengan kriptografi. 
Konsep yang digunakan untuk program kali ini adalah GUI berupa layout aplikasi dengan tampilan dua pengguna berbeda (Alice dan Bob) beserta kunci privat dan kunci publik yang dibangkitkan secara acak menggunakan algoritma RSA.

# Spesifikasi
- Program dapat menerima _message_ (ke depannya disebut _plaintext_) berupa teks yang diketikkan dari _keyboard_ atau file sembarang.
- Program dapat mengenkripsi _plaintext_ menggunakan RSA.
- Program dapat mendekripsi _ciphertext_ menjadi _plaintext_ semula menggunakan RSA sehingga dapat dibuka atau diinterpretasikan seperti semula sebelum enkripsi.
- Program akan menampilkan _plaintext_ dan _ciphertext_ di layar percakapan. Hal ini tidak terjadi bagi _plaintext_ atau _ciphertext_ berupa file attachment (hanya akan ditampilkan pesan notifikasi pengiriman dan penerimaan file).
- Program dapat menyimpan file kiriman pengguna ke dalam file sembarang dalam direktori tertentu. Pengguna juga dapat memilih untuk mendekripsi file _ciphertext_ sebelum disimpan dalam direktori.
- Pembangkitan kunci dari algoritma RSA terotomatisasi dan dilakukan secara acak serta disimpan dalam sebuah folder direktori tertentu.
- Proses enkripsi dan dekripsi dapat menggunakan kunci RSA yang sudah pernah dibangkitkan atau dari input pengguna.

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
    > pip install pyqt6 pyqt6-tools sympy
    - Modul **pyqt6** digunakan untuk membangun GUI layar menggunakan Qt6 untuk Python.
    - Modul **sympy** digunakan untuk membangkitkan bilangan prima yang akan digunakan pada pembangkitan kunci RSA.
## Bagian 2: Eksekusi dan Penggunaan
1. Jalankan file chat.py dengan menggunakan kode berikut:
    > py chat.py
2. Program akan menampilkan sebuah window baru berisi GUI layar percakapan.
3. Selamat mencoba simulasi percakapan/chat menggunakan algoritma RSA.