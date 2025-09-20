import pandas as pd
import glob
import re
import unicodedata
from unidecode import unidecode

# -----------------------------
# 1. Kamus keyword (base)
flags = [
    "gacor", "hoki", "max win", "maxwin", "jp", "jackpot", "wd cepat", "wd ngebut", 
    "wd kilat", "wd langsung", "wd lancar", "cuan", "auto wd", "langsung cair", 
    "slot", "scatter", "free spin", "freespin", "buy spin", "bonus spin", 
    "big win", "super win", "mega win", "sensational", "maxbet", "bet kecil",
    "spin gacor", "modal receh", "tewas scatter", "pola gacor", "pola hari ini",
    "member","spin", "bonus", "banyak bonus", "cair",
    "jangan tunggu kaya", "bisa jadi sultan", "coba modal receh", "100% jp", 
    "jam hoki", "malam ini gacor", "auto maxwin", 
    "cuan receh", "jepe", "main",
    "target4d", "L-I-V-E-S-L-0-T-3-6-5", 
    "Ｇ ＡＲ ＵＤ Ａ Ｈ ０ Ｋ ｌ", 
    "wd", "dep cepat", "deposit kecil", "depo cepat", "depo kecil", "depo"
]

# -----------------------------
# 2. File CSV
file_patterns = [
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
    r"Dataset Komentar\<CHANNEL_NAME>*.csv",
]

csv_files = []
for pattern in file_patterns:
    csv_files.extend(glob.glob(pattern))

# -----------------------------
# 3. Normalisasi teks (lebih agresif)
def normalize_text(text):
    if not isinstance(text, str):
        return ""
    # Unicode normalize
    text = unicodedata.normalize('NFKC', text)
    # Konversi huruf fancy ke ascii biasa
    text = unidecode(text)
    text = text.lower()
    # Hapus simbol/emoji → ganti spasi
    text = re.sub(r'[^\w\s]', ' ', text)
    # Hapus spasi ganda
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# -----------------------------
# 4. Regex generator untuk keyword
def keyword_to_pattern(kw):
    kw_norm = normalize_text(kw)
    return r'\b' + r'\s*[\W_]*'.join(list(kw_norm)) + r'\b'

flag_patterns = [re.compile(keyword_to_pattern(kw)) for kw in flags]

# -----------------------------
# 5. Brand spam pattern (diperluas)
brand_patterns = [
    re.compile(r'\b\w+4d\b'),                   # target4d, wifi4d
    re.compile(r'\b\w+win\d+\b'),               # ligawin66, maxwin88
    re.compile(r'\b\w+bet\d+\b'),               # istanabet368, win11bet
    re.compile(r'\b[a-z]+\d+(\.\d+)?\b'),       # alexis1.7, weton88, probet855
    re.compile(r'\b(suka\w*|siapbet|asia\w+)\b', re.IGNORECASE),  # sukapjp, siapbet, asiagenting
    re.compile(r'\b(weton\d+|alexis\d+)\b', re.IGNORECASE),       # spesifik brand umum
]

# -----------------------------
# 6. Fungsi classify comment dengan scoring
def classify_comment(comment):
    text_norm = normalize_text(comment)

    keyword_hits = sum(1 for pat in flag_patterns if pat.search(text_norm))
    brand_hits = sum(1 for pat in brand_patterns if pat.search(text_norm))

    score = 0
    score += brand_hits * 2
    score += keyword_hits

    # Heuristik: kata-kata pujian / ajakan join
    promo_clues = ["gabung", "join", "situs", "gampang menang", "buruan", "member", "langsung coba"]
    if any(clue in text_norm for clue in promo_clues):
        score += 1

    # Klasifikasi
    if score >= 2:
        return "PROMO_JUDOL"
    elif score == 1:
        return "RISKY"
    else:
        return None # Kelas Normal didapatkan secara manual dari dataset yang sudah ada dan potensi adanya fals positive hasil akhir

# -----------------------------
# 7. Proses semua file
results = []

for file in csv_files:
    try:
        df = pd.read_csv(file, encoding="utf-8", on_bad_lines="skip")
    except Exception as e:
        print(f"Skip file {file}: {e}")
        continue

    comment_col = None
    if "Comment" in df.columns:
        comment_col = "Comment"
    elif "simpleText" in df.columns:
        comment_col = "simpleText"
    else:
        print(f"Skip file {file}: tidak ada kolom 'Comment' atau 'simpleText'")
        continue

    for _, row in df.iterrows():
        comment = str(row[comment_col])
        label = classify_comment(comment)
        if label:  # hanya ambil PROMO_JUDOL & RISKY
            results.append({
                "File": file,
                "Comment": comment,
                "Label": label
            })

# -----------------------------
# 8. Simpan hasil
output_df = pd.DataFrame(results)
output_df.to_csv("loose_flag_1.csv", index=False, encoding="utf-8")
print("Deteksi selesai! Hasil tersimpan di loose_flag_1.csv")
