# dropna digunakan untuk menghapus cell yang kosong atau bernilai NaN dan None dari dataframe

import pandas as pd

data = {
    "A": [None, 2, 3, 5],
    "B": [1, None, 3, 4],
    "C": [1, 2, None, 4],
}

df = pd.DataFrame(data)
print("Data Sebelum penghapusan")
print(df)

print(" ")

cleaned_df = df.dropna()
print("Data sesudah penghapusan")
print(cleaned_df)

print(" ")

# fillna digunakan untuk mengisi nilai yang kosong contohnya seperti NaN dan Null pada dataframe
data = {
    "A": [1, 2, 3, None],
    "B": [1, 2, 3, None],
    "C": [1, 2, 3, None],
}

df = pd.DataFrame(data)
print("Data sebelum diisi")
print(df)
print(" ")

print("Data sesudah diisi")
filled_df = df.fillna(10)
print(filled_df)

print(" ")

# atau bisa juga
filled_df = df['C'].fillna(100)
print(filled_df)


# method mean(), median(), dan mode()
