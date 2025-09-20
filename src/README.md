Folder ini berisi skrip-skrip utama dan kamus jargon yang digunakan dalam proses *preprocessing* serta *flagging* komentar publik dari YouTube. Tujuannya adalah mendeteksi komentar yang berpotensi termasuk **PROMO\_JUDOL** (promosi judi online) dan **RISKY** (komentar berisiko), sekaligus membersihkan data agar siap digunakan untuk eksperimen NLP.

---

## 📑 Isi Folder

### 1. `jargon_flag.json`

Berisi **daftar kata kunci (flags)** dan pola regex dasar yang digunakan untuk mendeteksi istilah terkait promosi judi online.

* Struktur sederhana berupa list kata & pola regex.
* Digunakan sebagai *keyword dictionary* dalam proses penyaringan komentar.

---

### 2. `jargon_glossary.json`

Berisi **glossary (kata + definisi)** dari jargon yang sering muncul dalam komentar.

* Tujuannya bukan untuk pemrosesan otomatis, melainkan sebagai **dokumentasi**.
* Membantu pembaca/non-teknis memahami istilah seperti *gacor*, *maxwin*, *wd*, dsb.

---

### 3. `loose_flag_judol.py`

Skrip utama untuk **menyaring komentar berpotensi PROMO\_JUDOL atau RISKY** dari kumpulan dataset mentah.

* Menggunakan kombinasi:

  * Kamus `flags` dari `jargon_flag.json`.
  * Pola *brand spam* (regex khusus nama situs).
  * *Heuristic clues* (kata ajakan seperti *gabung*, *join*, *buruan*).
* Setiap komentar diberi skor, lalu diklasifikasikan ke:

  * `PROMO_JUDOL` → jika skor tinggi (keyword + brand).
  * `RISKY` → jika ada indikasi tapi lemah.
  * `None` → normal, tidak diproses lebih lanjut.
* Hasilnya disimpan sebagai `loose_flag_1.csv`.

⚠️ **Catatan:**
Filter ini bersifat *longgar (loose)*, sehingga cukup banyak **false positive**:

* Komentar normal masuk kategori PROMO\_JUDOL.
* Komentar RISKY masuk ke PROMO\_JUDOL.
* Komentar PROMO\_JUDOL justru masuk ke RISKY.

Namun demikian, skrip ini efektif untuk **menangkap kandidat data mentah** sebelum diproses lebih ketat.

---

### 4. `loose_flag_risky-comment.py`

Skrip untuk **fokus mendeteksi kelas RISKY** dari dataset komentar.

* Menggunakan pola regex dasar:

  ```
  (judi|judol|slot)
  ```
* Pencarian dilakukan pada kolom `message` dan `cleaned_message`.
* Komentar yang cocok disimpan ke `captured_comments.csv`.

Fungsinya sebagai *komplemen* dari `loose_flag_judol.py`, agar kelas **RISKY** tidak terlalu sedikit dalam dataset akhir.

---

### 5. `cek_jumlah_idetik.py`

Skrip pembersih dataset dari **komentar spam/duplikat**.

* Mengecek duplikasi berdasarkan kolom `message`.
* Memisahkan data unik ke `dataset_kaggle.csv`.
* Menyimpan duplikat ke `kaggle_duplicates.csv` untuk keperluan analisis lebih lanjut.

Dengan ini, dataset menjadi **lebih bersih, unik, dan representatif**.

---

## ⚖️ Etika & Limitasi

* Dataset diambil dari **komentar publik YouTube**.
* Data digunakan hanya untuk **tujuan akademis & riset NLP**.
* Tidak ada informasi pribadi (PII) yang disertakan.
* Nama channel atau entitas lain yang muncul dalam komentar telah **dianonimkan** untuk menjaga privasi.
