import pandas as pd
from pathlib import Path
import re

INPUT_GLOB = Path(r"Dataset Komentar/dataset_<CHANNEL_NAME>").glob("*.csv")
OUTPUT_FILE = Path("captured_comments.csv")

pattern = r'(judi|judol|slot)'
regex = re.compile(pattern, flags=re.IGNORECASE)

dfs = []
for csv_path in INPUT_GLOB:
    # coba berbagai delimiter + encoding
    for sep in [',',';','\t']:
        try:
            df = pd.read_csv(csv_path, dtype=str, sep=sep, encoding='utf-8-sig')
            if len(df.columns) >= 5:  # indikasi kolom terpisah benar
                break
        except Exception:
            continue
    
    print(f"\n[DEBUG] {csv_path} kolom:", df.columns.tolist())
    print(df.head(2).to_string())  # cek sampel
    
    # isi NaN
    df = df.fillna("")
    
    # pastikan ada kolom 'message' & 'cleaned_message'
    if "message" not in df.columns or "cleaned_message" not in df.columns:
        continue
    
    mask = df['message'].str.contains(regex, na=False) | df['cleaned_message'].str.contains(regex, na=False)
    matched = df[mask]
    if not matched.empty:
        dfs.append(matched.assign(source_file=str(csv_path)))

if dfs:
    result = pd.concat(dfs, ignore_index=True)
    result.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
    print(f"\nTotal komentar terdeteksi: {len(result)}")
    print(result[['datetime','author_name','message']].head().to_string(index=False))
else:
    print("Tidak ada komentar yang terdeteksi.")
