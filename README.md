# Sentry-ID Level 1 — MVP Judol Detector

Sentry-ID adalah proyek eksperimen deteksi teks untuk mengidentifikasi konten promosi **judi online (judol)** berbahasa Indonesia.  
Fokus tahap ini (Level 1) adalah klasifikasi teks komentar YouTube ke dalam tiga kelas:

- **PROMO_JUDOL** — konten promosi/ajakan bermain
- **RISKY** — menyebut judi/slot tanpa promosi (berita, opini, diskusi)
- **NORMAL** — teks umum

## 🚀 Output Proyek
- Baseline: TF-IDF + Logistic Regression
- Fine-tune: IndoBERT/IndoBERTweet (planned)
- Evaluasi: F1-macro, confusion matrix, PR curve
- Demo: Streamlit (planned)

## 📂 Struktur Repo
- `data/` — dataset (tidak di-push ke GitHub, hanya placeholder)
- `notebooks/` — EDA & eksperimen model
- `src/` — modul Python (crawler, preprocessing, training)
- `glossary/` — kamus jargon judol
- `reports/` — hasil eksperimen (figures, json, dsb.)

## ⚖️ Etika & Limitasi
Dataset diambil dari komentar publik (YouTube).  
Data digunakan hanya untuk tujuan akademis & riset NLP.  
Tidak ada PII (Personal Identifiable Information) yang disertakan.
