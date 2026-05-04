import pandas as pd

file_path = "year-2026.merged.csv"

# Keyword BBM
keywords = ["bbm", "bahan bakar", "bensin", "pertamax", "pertalite", 
            "solar", "biosolar", "premium", "avtur", "minyak"]

chunks = []
for chunk in pd.read_csv(file_path, chunksize=100000, low_memory=False):
    # Filter semua kolom yang mengandung keyword (case-insensitive)
    mask = chunk.apply(
        lambda col: col.astype(str).str.contains(
            "|".join(keywords), case=False, na=False
        )
    ).any(axis=1)
    chunks.append(chunk[mask])

# Gabungkan hasil
result = pd.concat(chunks, ignore_index=True)

# Simpan hasil
result.to_csv("hasil_filter_bbm.csv", index=False)
print(f"Selesai! Ditemukan {len(result)} baris.")