import pandas as pd

# ini digunakan untuk mengatasi format yg salah contohnya misal pada penanggalan

data = {
    "nama": ["John", "Budi", "Jane"],
    "tgl_lahir": [20050508, 20060927, "2007/10/19"],
    "hobi": ["Makan", "Tidur", "Game"]
}

df = pd.DataFrame(data)
# Mengonversi semua nilai dalam kolom 'tgl_lahir' menjadi string
df['tgl_lahir'] = df['tgl_lahir'].astype(str)

# Mengonversi format tanggal yang menggunakan "/" menjadi format datetime
df['tgl_lahir'] = pd.to_datetime(df['tgl_lahir'], errors='coerce')

print(df.to_string())

print(" ")

# menghapus nilai dengan NULL
df.dropna(subset=['tgl_lahir'], inplace = True)
print(df)