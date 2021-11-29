# **API Fakultas Prodi dengan Flask - MongoDB**
Sampel program yang digunakan dalam open proyek KOMPETEGRAM mengenai public API fakultas - prodi. Selengkapnya dapat mengujungi repositori [berikut](https://github.com/PROYEK-KOMPETEGRAM/docs-fakultas-prodi-api)

### ***Disclaimer***
Kode dari program ini tentu masih bersifat sederhana dan masih jauh dari pola *best-practice* yang dianjurkan dan direkomendasikan. Adapun tujuan utama dari kode program ini untuk memudahkan dalam memberikan gambaran *business logic* ataupun *luaran API* yang diperoleh.

### **Teknologi**
```
Python = sebagai bahasa pemrograman
Flask = sebagai framework Back-End
MongoDB = sebagai database
```

### **Tata Cara Menjalankan**
Silakan *clone* atau unduh repositori berikut, dapat melalui cara berikut :
```bash
$ git clone https://github.com/satrio-pamungkas/flask-mongodb-fakultas-prodi-api
```
Setelah itu, dalam *root* folder buat *virtual environment* untuk memberi *scope* dari *library-library* yang digunakan. Kemudian aktifkan *virtual environment* tersebut :
```bash
$ virtualenv env
$ cd env/bin && source activate && cd ../../
```
Install seluruh *library* yang dibutuhkan dengan pip (pastikan telah sukses terinstall semuanya) :
```bash
$ pip install -r requirements.txt
```
Buat file bernama `.env` 
```
$ touch .env
```
Dan isi file tersebut dengan teks berikut untuk mengisi konfigurasi kredensial MongoDB Atlas :
```bash
DB_USERNAME = isi dengan kredensial username MongoDB
DB_PASSWORD = isi dengan kredensial password MongoDB
DB_NAME = isi dengan nama database MongoDB
DB_COLLECTION = isi dengan nama collection MongoDB
```
Jalankan program dengan prefiks ( `py`, `python3`, atau `python`) seperti berikut :
```bash
$ python app.py
```
Program akan berjalan pada `http://localhost:5000` dan memiliki *endpoint* sesuai spesifikasi API masing-masing.

### **Pertanyaan, Saran, dan Masukan**
Jika terdapat kebingungan atau permasalahan dalam menjalankan program, ataupun memiliki saran dan masukan. Silakan dapat menghubungi pengurus atau *maintainer* utama repositori ini.
