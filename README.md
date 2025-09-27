# 🛡️ Sentry-ID Level 1 — MVP Gambling Detector
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)]()
[![HuggingFace](https://img.shields.io/badge/HF-Transformers-yellow.svg)](https://huggingface.co)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)]()

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
* **Fine-tuning:** IndoBERTweet
* **Evaluation:** F1-macro, and confusion matrix

---

### 📂 Repository Structure

* `data/` — dataset (placeholder, not pushed to GitHub)
* `notebooks/` — EDA & model experiments
* `src/` — Python modules (crawler, glossary)
* `results/` — Training artefacts & demo

---

### 📊 Model Evaluation

#### IndoBERTweet (Fine-tuned)

**With Augmentation**

* Accuracy: **0.990**
* Macro F1: **0.993**
* Performance is highly stable across all classes, including minority class *RISKY*.

```
              precision    recall  f1-score   support
      NORMAL      0.989     0.989     0.989        90
 PROMO_JUDOL      0.989     0.989     0.989        91
       RISKY      1.000     1.000     1.000        25
```

**Without Augmentation**

* Accuracy: **0.969**
* Macro F1: **0.958**
* Strong results overall, but lower recall for *RISKY*.

```
              precision    recall  f1-score   support
      NORMAL      0.967     0.978     0.972        90
 PROMO_JUDOL      0.967     0.978     0.973        91
       RISKY      1.000     0.867     0.929        15
```

---

#### TF-IDF + Logistic Regression (Baseline)

**With Augmentation**

* Accuracy: **0.932**
* Macro F1: **0.939**
* Balanced performance, slightly weaker than BERT-based approach.

```
              precision    recall  f1-score   support
      NORMAL      0.889     0.978     0.931        90
 PROMO_JUDOL      0.976     0.879     0.925        91
       RISKY      0.960     0.960     0.960        25
```

**Without Augmentation**

* Accuracy: **0.923**
* Macro F1: **0.914**
* Shows difficulty in detecting *RISKY* reliably.

```
              precision    recall  f1-score   support
      NORMAL      0.897     0.967     0.930        90
 PROMO_JUDOL      0.943     0.901     0.921        91
       RISKY      1.000     0.800     0.889        15
```

## 🚀 Live Demo

Try our interactive demo on **Streamlit Cloud**:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sentry-id-ww5vv8cgu4cfmbudssbdeg.streamlit.app/)

For detailed usage and code examples, see the [app folder](sentry-id/app).

📌 **Summary:**

* **IndoBERTweet + augmentation** achieved the best results (Accuracy: 99.0%, Macro F1: 99.3%).
* Augmentation consistently improved performance, especially for minority class *RISKY*.
* TF-IDF + Logistic Regression remains a solid baseline but is outperformed by transformer-based fine-tuning.
* Future research is encouraged to specifically enrich the variety of RISKY comments, enabling the model to better capture borderline text patterns and improve classification accuracy in ambiguous cases

---

### ⚖️ Ethics & Limitations

* Dataset comes from **public YouTube comments**.
* Used strictly for **academic & NLP research purposes**.
* No **PII (Personally Identifiable Information)** is included.
* The author does not recommend any gambling related activities at all.

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
* **Fine-tune:** IndoBERTweet
* **Evaluasi:** F1-macro, dan confusion matrix

---

### 📂 Struktur Repo

* `data/` — dataset (placeholder, tidak di-*push* ke GitHub)
* `notebooks/` — EDA & eksperimen model
* `src/` — modul Python (crawler, kamus jargon judol)
* `results/` — artefak pelatihan & demo

---

### 📊 Evaluasi Model

#### IndoBERTweet (Fine-tuned)

**Dengan Augmentasi**

* Akurasi: **0.990**
* Macro F1: **0.993**
* Performa sangat stabil pada semua kelas, termasuk kelas minoritas *RISKY*.

```
              precision    recall  f1-score   support
      NORMAL      0.989     0.989     0.989        90
 PROMO_JUDOL      0.989     0.989     0.989        91
       RISKY      1.000     1.000     1.000        25
```

**Tanpa Augmentasi**

* Akurasi: **0.969**
* Macro F1: **0.958**
* Masih kuat, tetapi recall untuk *RISKY* lebih rendah.

```
              precision    recall  f1-score   support
      NORMAL      0.967     0.978     0.972        90
 PROMO_JUDOL      0.967     0.978     0.973        91
       RISKY      1.000     0.867     0.929        15
```

---

#### TF-IDF + Logistic Regression (Baseline)

**Dengan Augmentasi**

* Akurasi: **0.932**
* Macro F1: **0.939**
* Performa seimbang, meski lebih lemah dibanding model BERT.

```
              precision    recall  f1-score   support
      NORMAL      0.889     0.978     0.931        90
 PROMO_JUDOL      0.976     0.879     0.925        91
       RISKY      0.960     0.960     0.960        25
```

**Tanpa Augmentasi**

* Akurasi: **0.923**
* Macro F1: **0.914**
* Cenderung kesulitan mengenali kelas *RISKY*.

```
              precision    recall  f1-score   support
      NORMAL      0.897     0.967     0.930        90
 PROMO_JUDOL      0.943     0.901     0.921        91
       RISKY      1.000     0.800     0.889        15
```

---

## 🚀 Demo Langsung

Coba demo interaktif kami di **Streamlit Cloud**:  
[![Buka di Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sentry-id-ww5vv8cgu4cfmbudssbdeg.streamlit.app/)

Untuk panduan penggunaan dan contoh kode lebih lengkap, silakan lihat di [folder app](sentry-id/app).


📌 **Ringkasan:**

* **IndoBERTweet + augmentasi** adalah kombinasi terbaik (Akurasi: 99.0%, Macro F1: 99.3%).
* Augmentasi terbukti membantu, terutama untuk meningkatkan deteksi kelas minoritas.
* Baseline TF-IDF + Logistic Regression masih kompetitif, namun kalah jauh dari pendekatan transformer.
* Penelitian selanjutnya disarankan untuk secara khusus memperkaya variasi komentar kategori RISKY, sehingga model dapat mengenali pola teks borderline secara lebih baik dan meningkatkan ketepatan klasifikasi pada kasus ambigu

---

### ⚖️ Etika & Limitasi

* Dataset diambil dari **komentar publik YouTube**.
* Digunakan hanya untuk **tujuan akademis & riset NLP**.
* Tidak ada **PII (Personal Identifiable Information)** yang disertakan.
* Penulis sama sekali tidak merekomendasikan kegiatan yang berhubungan dengan judi online.

