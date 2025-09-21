## ID
---
Folder ini digunakan sebagai placeholder untuk dataset lokal.  
**Dataset tidak diunggah ke GitHub** karena alasan ukuran, etika, dan privasi.

## 📊 Ringkasan Dataset
- **Sumber**: Komentar publik dari YouTube (±90% dari channel dengan konten mukbang, video dengan view tinggi).  
- **Jumlah sampel**: 1.991 komentar  
- **Distribusi kelas**:
  - NORMAL: 900
  - RISKY: 252 (termasuk 99 hasil augmentasi)
  - PROMO_JUDOL: 906  
- **Format file utama**: `dataset.csv`

| file | comment | label | is_augmented | is_manual |
|------|----------|-------|--------------|-----------|
| Dataset Komentar/<NAMA_CHANNEL>.csv | judi meresahkan blokir laah | RISKY | 0 | 0 |
| Dataset Komentar/<NAMA_CHANNEL>.csv | 𝙈𝙖𝙨𝙪𝙠 𝙗𝙖𝙧𝙪 𝙖𝙟𝙖 𝙨𝙪𝙙𝙖𝙝 𝙖𝙪𝙩𝙤 𝙟𝙚𝙥𝙚𝙮 𝙙𝙞 <SITUS_JUDI> | PROMO_JUDOL | 0 | 0 |
| Dataset Komentar/<NAMA_CHANNEL>.csv | Bang ada kliatan tuyulnya nggak di situ ? 😅😅 | NORMAL | 0 | 1 |

## 🏷️ Label
- **PROMO_JUDOL** — konten promosi/ajakan bermain (misalnya: *bonus new member, link gacor, daftar sekarang*).  
- **RISKY** — menyebut judi/slot tanpa ajakan (berita, opini, diskusi).  
- **NORMAL** — teks umum, tidak relevan dengan judol.  

## ⚠️ Catatan
- Dataset ini hanya digunakan untuk **riset NLP dan tujuan akademis**.  
- Tidak mengandung informasi pribadi (PII).  
- Data asli disimpan secara lokal.  

---

## EN

---

This folder is used as a placeholder for the local dataset.
**The dataset is not uploaded to GitHub** due to size, ethical, and privacy considerations.

## 📊 Dataset Summary

* **Source**: Public YouTube comments (±90% from mukbang-related channels, high-view videos).
* **Number of samples**: 1,991 comments
* **Class distribution**:

  * NORMAL: 900
  * RISKY: 252 (including 99 augmented samples)
  * PROMO\_JUDOL: 906
* **Main file format**: `dataset.csv`

| file                                  | comment                                                   | label        | is\_augmented | is\_manual |
| ------------------------------------- | --------------------------------------------------------- | ------------ | ------------- | ---------- |
| Dataset Komentar/\<CHANNEL\_NAME>.csv | gambling is troubling, it should be blocked               | RISKY        | 0             | 0          |
| Dataset Komentar/\<CHANNEL\_NAME>.csv | Just joined and already auto jackpot on \<GAMBLING\_SITE> | PROMO\_JUDOL | 0             | 0          |
| Dataset Komentar/\<CHANNEL\_NAME>.csv | Bro, can you see the ghost kid in that scene? 😅😅        | NORMAL       | 0             | 1          |

## 🏷️ Labels

* **PROMO\_JUDOL** — promotional content / invitation to gamble (e.g., *new member bonus, winning link, register now*).
* **RISKY** — mentions gambling/slot without invitation (news, opinions, discussions).
* **NORMAL** — general text, not related to gambling.

## ⚠️ Notes

* This dataset is intended **solely for NLP research and academic purposes**.
* It does not contain personally identifiable information (PII).
* The original data is stored locally. 

---
