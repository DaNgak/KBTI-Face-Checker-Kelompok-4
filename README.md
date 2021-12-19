# KBTI-Face-Checker

## Kelompok 4

-   Aliyya Putri Setiyomadani (2041720115)
-   Aria Pratama Effendi (2041720112)
-   Zalfa' Putri Nabilah (2041720103)

## Cara Instalasi Face Checker

<details>
    <summary><b>Tentang Python</b></summary>

[Python](https://www.python.org) adalah sebuah bahasa pemrograman tingkat tinggi (high-level) dan multi guna. Tingkat tinggi yang dimaksud adalah dari cara kita berinteraksi dengan komputer menggunakan bahasa yang hampir mirip dengan bahasa manusia tanpa perlu mengerti dan memahami detail dari sistem operasi atau komputer itu sendiri. Berbeda dengan bahasa pemrograman tingkat rendah seperti Assembly atau C yang mana kita perlu memahami cara memanage memory dan sebagainya.

Python diciptakan pada akhir tahun 1980-an oleh [Guido Van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) seorang programmer dari Belanda. Python dirilis pertama kali pada tahun 1991, Python 2.0 dirilis pada tahun 2000 dan Python 3.0 dirilis pada tahun 2008. Saat ini buat teman-teman yang ingin belajar Python, saya sarankan langsung mulai dengan Python versi 3+.

Karena populernya bahasa ini dan bisa digunakan untuk berbagai macam keperluan, kita akan sering melihat Python digunakan dalam web development, pembuatan API, program berbasis CLI, embedded system, scripting engine untuk game dan lain sebagainya.

</details>

<details>
    <summary><b>Tentang Aplikasi Face Checker</b></summary>

![Gambar Aplikasi Face Checker](https://cdn.discordapp.com/attachments/878508823873196114/921677584947875880/unknown.png)

Face Checker merupakan contoh biometrika berdasakan bagian tubuh. Sistem ini adalah sistem untuk mengenali identitas seseorang secara otomatis melalui teknologi komputer yang bertujuan untuk mendukung proses pengecekan dan pengenalan wajah penggunakan dengan cepat dan tepat.

</details>

<details>
    <summary><b>Instalasi Python</b></summary>

-   Download Python [disini](https://www.python.org/downloads/)
-   Lakukan Instalasi Python sesuai dengan device kalian
-   [Windows](https://www.youtube.com/watch?v=OSmaWPSgvTQ)
-   [MacOs](https://www.youtube.com/watch?v=HSAm6s10G7g)
</details>

<details>
    <summary><b>Instalasi Package PIP (Python Installs Packages)</b></summary>

-   `pip install tk`
    ![Gambar Install tk](https://cdn.discordapp.com/attachments/878508823873196114/921679267409059860/unknown.png)

-   `pip install tkinter-page`
    ![Gambar Install tkinter-page](https://cdn.discordapp.com/attachments/878508823873196114/921680126008254464/unknown.png)

-   `pip install opencv-python`
    ![Gambar Install opencv-python](https://cdn.discordapp.com/attachments/878508823873196114/921680621284257832/unknown.png)

-   `pip install pytest-shutil`
    ![Gambar Install pytest-shutil](https://cdn.discordapp.com/attachments/878508823873196114/921698985524211732/unknown.png)

-   `pip install python-csv`
    ![Gambar Install python-csv](https://cdn.discordapp.com/attachments/878508823873196114/921698451606110248/unknown.png)

-   `pip install Pillow`
    ![Gambar Install Pillow](https://cdn.discordapp.com/attachments/878508823873196114/921681561013870622/unknown.png)

-   `pip install numpy`
    ![Gambar Install numpy](https://cdn.discordapp.com/attachments/878508823873196114/921681845488336926/unknown.png)

-   `pip install pandas`
    ![Gambar Install pandas](https://cdn.discordapp.com/attachments/878508823873196114/921682069774557184/unknown.png)

-   `pip install face_recognition`
![Gambar Install face_recognition](https://cdn.discordapp.com/attachments/878508823873196114/921683163678408734/unknown.png)
</details>

<details>
    <summary><b>Running Aplikasi</b></summary>

1.  Pertama jalankan file `index.py`
    ![Gambar Run App](https://cdn.discordapp.com/attachments/878508823873196114/921701475892228146/unknown.png)
       <hr>
1.  Selanjutnya akan tampil GUI Aplikasi seperti berikut
    ![Gambar Aplikasi Face Checker](https://cdn.discordapp.com/attachments/878508823873196114/921677584947875880/unknown.png)
    <hr>
1.  Masukkan _**ID Student**_ dan _**Nama Student**_
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921704311493394432/unknown.png)
    <hr>
1.  Klik tombol `take images` untuk mendapatkan sample / gambar
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921783574385004544/unknown.png)
    <hr>
1.  Setelah klik tombol `take images` akan muncul kamera untuk mengenali dan mengambil sample dari object
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921905508259070013/unknown.png)
    <hr>
1.  Setelah system berhasil mendeteksi object, akan muncul notifikasi pada label _Notification System_ yang berisikan _**ID Student**_ dan _**Nama Student**_ yang telah diinputkan, lalu klik tombol `train images`
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921783767146827826/unknown.png)
     <hr>
1.  Jika berhasil maka akan muncul notifikasi pada label _Notification System_
    dengan message `image trained`
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921783837246230578/unknown.png)
    <hr>
1.  Untuk melihat apakah datanya udah masuk bisa dilihat di folder `StudentDetails` untuk melihat apakah data nya berhasil di _train_ atau tidak
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921913156522098698/unknown.png)
    <hr>
1.  Selanjutnya klik tombol `take images` dan kamera nantinya akan terbuka
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921783837246230578/unknown.png)
    <hr>
1.  Setelah terdeteksi oleh kamera seperti gambar dibawah
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921907155223863326/unknown.png)
    <hr>
1.  Tekan huruf `Q` yang ada pada keyboard device anda masing-masing, dan nantinya akan muncul _**ID Student**_ - _**Nama Student**_ dan _**DATETIME**_ ketika proses `take images` berlangsung
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921907805076746300/unknown.png)
    <hr>
1.  Untuk mengetahui apakah datanya sudah masuk, anda bisa melihat di folder `Attandance` lalu buka file csv nya, nanti akan terlihat seperti gambar berikut
    ![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921910878415249478/unknown.png)
    <hr>
1.  Jika telah melakukan semua langkah diatas, maka aplikasi sudah selesai digunakan dan Anda bisa men klik tombol `Quit` dan nantinya aplikasi akan `exit()` dengan sendirinya
![Gambar Aplikasi Demo](https://cdn.discordapp.com/attachments/878508823873196114/921910878415249478/unknown.png)
<hr>
</details>

## Penutup

> Sekian pengenalan aplikasi Face Checker dari kelompok 4. Akhir kata kami ucapkan `terima kasih` karena telah mencoba aplikasi yang kami develop. Salam [#AtapNegeri](https://www.youtube.com/user/fiersabesari)

```
“Kalaupun harus gagal, setidaknya gagal dengan cepat dan tegas.
Daripada berputar-putar, masuk friendzone, jadi teman curhat,
menunggu dia putus, main kode, berusaha jujur,
eh sudah begitu gagal-gagal juga.”

– Fiersa Besari
```
