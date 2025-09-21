# 🛡️ Sentry-ID Level 1 — MVP Judol Detector

## 🇬🇧 English Version

### 🎯 Project Description

Sentry-ID is an experimental text detection project designed to identify **online gambling (judol)** promotional content in Indonesian.
At this first stage (Level 1), the focus is to classify YouTube comments into three classes:

* **PROMO\_JUDOL** — promotional/invitation content
* **RISKY** — mentions gambling/slots without promotion (e.g., news, opinion, discussion)
* **NORMAL** — general comments

---

### 🚀 Project Output

* **Baseline:** TF-IDF + Logistic Regression
* **Fine-tuning:** IndoBERT / IndoBERTweet *(planned)*
* **Evaluation:** F1-macro, confusion matrix, PR curve
* **Demo:** Streamlit *(planned)*

---

### 📂 Repository Structure

* `data/` — dataset (placeholder, not pushed to GitHub)
* `notebooks/` — EDA & model experiments
* `src/` — Python modules (crawler, glossary)
* `results/` —  Training Artefacts 


---

### ⚖️ Ethics & Limitations

* Dataset comes from **public YouTube comments**.
* Used strictly for **academic & NLP research purposes**.
* No **PII (Personally Identifiable Information)** is included.

**🇮🇩 Bahasa Indonesia** 

---

## 🇮🇩 Versi Bahasa Indonesia

### 🎯 Deskripsi Proyek

Sentry-ID adalah proyek eksperimen deteksi teks untuk mengidentifikasi konten promosi **judi online (judol)** berbahasa Indonesia.
Fokus tahap awal (Level 1) adalah klasifikasi komentar YouTube ke dalam tiga kelas:

* **PROMO\_JUDOL** — konten promosi/ajakan bermain
* **RISKY** — menyebut judi/slot tanpa promosi (mis. berita, opini, diskusi)
* **NORMAL** — komentar umum

---

### 🚀 Output Proyek

* **Baseline:** TF-IDF + Logistic Regression
* **Fine-tune:** IndoBERT / IndoBERTweet *(planned)*
* **Evaluasi:** F1-macro, confusion matrix, PR curve
* **Demo:** Streamlit *(planned)*

---

### 📂 Struktur Repo

* `data/` — dataset (placeholder, tidak di-*push* ke GitHub)
* `notebooks/` — EDA & eksperimen model
* `src/` — modul Python (crawler, kamus jargon judol)
* `results/` —  Artefak pelatihan


---

### ⚖️ Etika & Limitasi

* Dataset diambil dari **komentar publik YouTube**.
* Digunakan hanya untuk **tujuan akademis & riset NLP**.
* Tidak ada **PII (Personal Identifiable Information)** yang disertakan.

---


