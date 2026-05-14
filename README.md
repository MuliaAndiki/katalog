# 🛒 Website Katalog Produk Sederhana dengan Django

Sebuah website katalog produk sederhana yang dibuat menggunakan framework Django untuk menampilkan daftar produk, detail produk, halaman kontak, dan homepage.

---

## 📋 Deskripsi Project

Project ini adalah implementasi praktikum yang bertujuan untuk memahami dasar-dasar Django framework, termasuk:

- Routing URL (URL patterns)
- Views (function-based views)
- Templates (rendering data dengan Django template engine)
- Data management (menggunakan hardcoded data dalam bentuk list of dictionaries)

**Catatan:** Project ini tidak menggunakan database sama sekali. Semua data produk disimpan dalam bentuk hardcoded list di `views.py`.

---

## 🏗️ Struktur Project

```
Tugas3/
├── .venv/                          # Virtual environment
├── core/                           # Project utama Django
│   ├── settings.py                 # Konfigurasi project
│   ├── urls.py                     # URL routing project
│   ├── wsgi.py                     # WSGI configuration
│   └── asgi.py
├── katalog/                        # Django app untuk katalog produk
│   ├── templates/
│   │   └── katalog/
│   │       ├── homepage.html       # Template halaman utama
│   │       ├── daftar_produk.html  # Template daftar semua produk
│   │       ├── detail_produk.html  # Template detail satu produk
│   │       └── kontak.html         # Template halaman kontak
│   ├── views.py                    # Fungsi-fungsi view dan data produk
│   ├── urls.py                     # URL routing app
│   ├── models.py                   # (Tidak digunakan)
│   └── apps.py
├── manage.py                       # Django management command
├── db.sqlite3                      # Database SQLite (buat otomatis saat migrate)
└── Readme.md                       # File dokumentasi ini
```

---

## 🎯 Fitur-Fitur

### 1. **Homepage** (`/`)

- Menampilkan pesan sambutan kepada pengunjung
- Menyediakan link navigasi ke halaman daftar produk dan kontak
- Design responsif dengan gradient background

### 2. **Daftar Produk** (`/produk/`)

- Menampilkan semua produk dalam bentuk grid kartu (cards)
- Setiap kartu menampilkan: nama, harga, deskripsi, dan tombol "Lihat Detail"
- Menggunakan loop template Django `{% for %}`
- Design responsif dan menarik

### 3. **Detail Produk** (`/produk/<id>/`)

- Menampilkan informasi lengkap satu produk berdasarkan parameter ID
- Menampilkan: nama, harga, deskripsi, dan ID produk
- Error handling untuk ID yang tidak ditemukan (404)
- Link kembali ke halaman sebelumnya

### 4. **Halaman Kontak** (`/kontak/`)

- Menampilkan informasi kontak statis
- Termasuk: email, telepon, alamat fisik, jam operasional
- Link media sosial placeholder
- Design profesional dan user-friendly

---

## 📦 Data Produk

Project ini menyertakan 4 produk hardcoded:

| ID  | Nama Produk                   | Harga         | Deskripsi                                                                          |
| --- | ----------------------------- | ------------- | ---------------------------------------------------------------------------------- |
| 1   | Laptop Dell XPS 13            | Rp 15.999.000 | Laptop premium dengan prosesor Intel Core i7, layar 4K, dan desain yang elegan     |
| 2   | Smartphone Samsung Galaxy A52 | Rp 5.999.000  | Smartphone mid-range dengan kamera 64MP, baterai 4500mAh, dan layar AMOLED         |
| 3   | Headphone Sony WH-1000XM4     | Rp 3.499.000  | Headphone noise-cancelling dengan kualitas audio terbaik dan baterai tahan lama    |
| 4   | Tablet iPad Pro 12.9"         | Rp 12.999.000 | Tablet flagship dengan prosesor M1, layar Liquid Retina, dan dukungan Apple Pencil |

---

## 🚀 Cara Setup & Menjalankan

### **Langkah 1: Persiapan Environment**

```bash
# Masuk ke folder project
cd ~/Kuliah/ppl/prak/Tugas3

# Aktifkan virtual environment
source .venv/bin/activate
```

### **Langkah 2: Setup Database (Opsional)**

```bash
# Terapkan migrasi Django bawaan
python manage.py migrate
```

> **Catatan:** Database hanya diperlukan untuk fitur admin Django. Data katalog produk disimpan dalam bentuk hardcoded.

### **Langkah 3: Jalankan Development Server**

```bash
python manage.py runserver
```

Server akan berjalan di: `http://127.0.0.1:8000/`

### **Langkah 4: Akses Website di Browser**

Buka browser dan akses URL-URL berikut:

| Halaman                | URL                             |
| ---------------------- | ------------------------------- |
| **Homepage**           | http://127.0.0.1:8000/          |
| **Daftar Produk**      | http://127.0.0.1:8000/produk/   |
| **Detail Produk ID 1** | http://127.0.0.1:8000/produk/1/ |
| **Detail Produk ID 2** | http://127.0.0.1:8000/produk/2/ |
| **Detail Produk ID 3** | http://127.0.0.1:8000/produk/3/ |
| **Detail Produk ID 4** | http://127.0.0.1:8000/produk/4/ |
| **Halaman Kontak**     | http://127.0.0.1:8000/kontak/   |

---

## 📝 Routing URLs

### **katalog/urls.py** (App level)

```python
path('', views.homepage, name='homepage')              # Homepage
path('produk/', views.daftar_produk, name='daftar_produk')  # Daftar produk
path('produk/<int:id>/', views.detail_produk, name='detail_produk')  # Detail produk
path('kontak/', views.kontak, name='kontak')          # Kontak
```

### **core/urls.py** (Project level)

```python
path('admin/', admin.site.urls)                        # Admin panel
path('', include('katalog.urls'))                      # Include semua URL dari app katalog
```

---

## 🎨 Template Django yang Digunakan

### **Tag Template Django:**

- `{{ variable }}` - Menampilkan variabel dari context
- `{% for item in items %}...{% endfor %}` - Loop data
- `{% if condition %}...{% else %}...{% endif %}` - Kondisional

### **Contoh di daftar_produk.html:**

```html
{% for produk in produk_list %}
<div class="product-card">
  <h3>{{ produk.nama }}</h3>
  <div class="price">{{ produk.harga }}</div>
  <p>{{ produk.deskripsi }}</p>
  <a href="/produk/{{ produk.id }}/">Lihat Detail</a>
</div>
{% endfor %}
```

---

## 🛠️ Technology Stack

- **Backend Framework:** Django 4.2+
- **Python Version:** 3.12+
- **Frontend:** HTML5 + CSS3 (vanilla)
- **Database:** SQLite3 (Django bawaan)
- **Server:** Django Development Server

---

## 📌 Batasan Project

✅ **Yang Ada:**

- 4 halaman dengan URL berbeda
- Routing URL menggunakan `urls.py`
- Views berbentuk function-based views
- Data hardcoded dalam bentuk list of dictionaries
- Templates menggunakan Django template engine
- Design responsive dan modern

❌ **Yang Tidak Ada:**

- Database models (tidak menggunakan `models.py`)
- Migrations untuk app katalog
- Form untuk input data
- Authentication/Login
- API endpoints
- JavaScript interaktif

---

## 📖 Pembelajaran Django

### **Konsep yang Dipelajari:**

1. **Project vs App Structure**
   - Project: Container untuk seluruh aplikasi
   - App: Modul functionality terpisah

2. **URL Routing**
   - Menghubungkan URL dengan functions di views
   - Parameter dynamic di URL (`<int:id>`)

3. **Views (Function-Based)**
   - Menerima request dari browser
   - Merender template dengan context data

4. **Templates**
   - Rendering HTML dengan data dari views
   - Menggunakan template tags Django

5. **Settings.py**
   - Konfigurasi INSTALLED_APPS
   - Template configuration
   - Database settings

---

## 🎓 Panduan Pengembangan Lebih Lanjut

Jika ingin mengembangkan project ini lebih lanjut, bisa menambahkan:

1. **Database Models**

   ```python
   class Produk(models.Model):
       nama = models.CharField(max_length=200)
       harga = models.DecimalField(max_digits=10, decimal_places=2)
       deskripsi = models.TextField()
   ```

2. **Admin Interface**

   ```python
   admin.site.register(Produk)
   ```

3. **Search & Filter**
   - Search berdasarkan nama produk
   - Filter berdasarkan harga range

4. **Cart & Checkout**
   - Shopping cart functionality
   - Fake payment gateway

5. **Authentication**
   - User registration
   - User login/logout
   - User profile

---

---

## 📄 Lisensi

Project ini adalah bagian dari tugas praktikum perkuliahan.

---

## ✍️ Catatan Pengembang

- Project ini dibuat sebagai pembelajaran dasar Django
- Data bersifat dummy/hardcoded
- Semua halaman responsif dan dapat diakses dari berbagai ukuran layar
- Code siap production untuk keperluan pembelajaran

---
