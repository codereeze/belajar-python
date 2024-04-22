# duplicated() dalam Pandas digunakan untuk mengidentifikasi baris-baris yang merupakan duplikat dari baris-baris sebelumnya dalam DataFrame. Dengan kata lain, fungsi ini akan mengembalikan nilai True untuk setiap baris yang merupakan duplikat dari baris-baris sebelumnya, dan False untuk baris-baris yang unik.
# drop_duplicates() digunakan untuk membersihkan DataFrame dari baris-baris yang duplikat.

import pandas as pd

# data = pd.read_csv('coffee.csv')



data = {'A': [1, 2, 2, 3, 4],
        'B': ['a', 'b', 'b', 'c', 'd']}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Identifikasi baris-baris yang duplikat
dup_rows = df.duplicated()
print("\nBaris-baris yang duplikat:")
print(dup_rows)

# Hapus baris-baris yang duplikat
cleaned_df = df.drop_duplicates()
print("\nDataFrame setelah penghapusan baris duplikat:")
print(cleaned_df)