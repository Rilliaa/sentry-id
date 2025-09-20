## 🇮🇩 

Folder ini berisi skrip-skrip utama dan kamus jargon yang digunakan dalam proses *preprocessing* serta *flagging* komentar publik dari YouTube. Tujuannya adalah mendeteksi komentar yang berpotensi termasuk **PROMO\_JUDOL** (promosi judi online) dan **RISKY** (komentar berisiko), sekaligus membersihkan data agar siap digunakan untuk eksperimen NLP.

---

### 📑 Isi Folder

#### 1. `jargon_flag.json`

Berisi **daftar kata kunci (flags)** dan pola regex dasar yang digunakan untuk mendeteksi istilah terkait promosi judi online.

* Struktur berupa list kata & pola regex.
* Digunakan sebagai *keyword dictionary* dalam penyaringan komentar.

#### 2. `jargon_glossary.json`

Berisi **glossary (kata + definisi)** dari jargon yang sering muncul dalam komentar.

* Bukan untuk pemrosesan otomatis, melainkan **dokumentasi**.
* Membantu pembaca/non-teknis memahami istilah seperti *gacor*, *maxwin*, *wd*, dsb.

#### 3. `loose_flag_judol.py`

Skrip utama untuk **menyaring komentar PROMO\_JUDOL atau RISKY**.

* Menggunakan kombinasi:

  * Kamus `flags` dari `jargon_flag.json`.
  * Pola *brand spam* (regex nama situs).
  * *Heuristic clues* (ajakan seperti *gabung*, *join*, *buruan*).
* Keluaran: `loose_flag_1.csv`.

⚠️ **Catatan:** Filter bersifat *longgar*, sehingga ada **false positive**, tetapi berguna untuk menangkap kandidat data mentah.

#### 4. `loose_flag_risky-comment.py`

Skrip untuk **fokus mendeteksi kelas RISKY**.

* Regex sederhana:

  ```regex
  (judi|judol|slot)
  ```
* Menyimpan hasil ke `captured_comments.csv`.

#### 5. `cek_jumlah_idetik.py`

Skrip pembersih dataset dari spam/duplikat.

* Mengecek duplikasi berdasarkan kolom `message`.
* Dataset unik → `dataset_kaggle.csv`.
* Duplikat → `kaggle_duplicates.csv`.

---

### ⚖️ Etika & Limitasi

* Data berasal dari **komentar publik YouTube**.
* Hanya untuk **riset akademis & NLP**.
* Tidak ada PII yang disertakan.
* Nama channel/entitas dianonimkan demi privasi.

---

## 🇬🇧 English Version

This folder contains the main scripts and jargon dictionaries used for *preprocessing* and *flagging* YouTube public comments. The goal is to detect comments potentially classified as **PROMO\_JUDOL** (online gambling promotion) and **RISKY** (risky comments), while also cleaning the data for NLP experiments.

---

### 📑 Folder Contents

#### 1. `jargon_flag.json`

Contains a **list of keywords (flags)** and basic regex patterns to detect online gambling promotion terms.

* Structured as a list of words & regex patterns.
* Used as a *keyword dictionary* in comment filtering.

#### 2. `jargon_glossary.json`

Contains a **glossary (word + definition)** of jargon frequently found in comments.

* Intended for **documentation**, not automatic processing.
* Helps readers/non-technical users understand terms like *gacor*, *maxwin*, *wd*, etc.

#### 3. `loose_flag_judol.py`

Main script for **filtering PROMO\_JUDOL or RISKY comments**.

* Combines:

  * Flags from `jargon_flag.json`.
  * *Brand spam* regex (website names).
  * *Heuristic clues* (e.g., *join*, *gabung*, *buruan*).
* Output saved as `loose_flag_1.csv`.

⚠️ **Note:** This is a *loose filter*, leading to **false positives**, but effective for capturing raw candidate data.

#### 4. `loose_flag_risky-comment.py`

Script to **focus on detecting RISKY comments**.

* Regex pattern:

  ```regex
  (judi|judol|slot)
  ```
* Results saved to `captured_comments.csv`.

#### 5. `cek_jumlah_idetik.py`

Dataset cleaning script for spam/duplicates.

* Checks duplicates based on the `message` column.
* Unique dataset → `dataset_kaggle.csv`.
* Duplicates → `kaggle_duplicates.csv`.

---

### ⚖️ Ethics & Limitations

* Data comes from **public YouTube comments**.
* Used strictly for **academic & NLP research purposes**.
* No personally identifiable information (PII) is included.
* Channel names and entities are **anonymized** for privacy.

