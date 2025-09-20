import pandas as pd

# --- 1. Load dataset ---
df = pd.read_csv("<CHANNEL_NAME>.csv")  

# --- 2. Cek duplikat berdasarkan kolom Comment ---
duplicates = df[df.duplicated(subset=["message"], keep=False)]  
clean = df.drop_duplicates(subset=["message"], keep="first")    

# --- 3. Simpan hasil ---
clean.to_csv("dataset_kaggle.csv", index=False, encoding="utf-8")
duplicates.to_csv("kaggle_duplicates.csv", index=False, encoding="utf-8")

print(f"Total data awal: {len(df)}")
print(f"Data unik tersisa: {len(clean)}")
print(f"Data duplikat ditemukan: {len(duplicates)} (sudah dipisahkan ke kaggle_duplicates.csv)")
