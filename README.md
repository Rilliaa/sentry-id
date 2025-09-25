# 🛡️ Sentry-ID Level 1 — MVP Gambling Detector

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

📌 **Summary:**

* **IndoBERTweet + augmentation** achieved the best results (Accuracy: 99.0%, Macro F1: 99.3%).
* Augmentation consistently improved performance, especially for minority class *RISKY*.
* TF-IDF + Logistic Regression remains a solid baseline but is outperformed by transformer-based fine-tuning.

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

📌 **Ringkasan:**

* **IndoBERTweet + augmentasi** adalah kombinasi terbaik (Akurasi: 99.0%, Macro F1: 99.3%).
* Augmentasi terbukti membantu, terutama untuk meningkatkan deteksi kelas minoritas.
* Baseline TF-IDF + Logistic Regression masih kompetitif, namun kalah jauh dari pendekatan transformer.

---

### ⚖️ Etika & Limitasi

* Dataset diambil dari **komentar publik YouTube**.
* Digunakan hanya untuk **tujuan akademis & riset NLP**.
* Tidak ada **PII (Personal Identifiable Information)** yang disertakan.
* Penulis sama sekali tidak merekomendasikan kegiatan yang berhubungan dengan judi online.

