import pandas as pd

data = pd.read_csv('../coffee.csv')

# mencetak lima row pertama dari atas (default)
print(data.head())
print(" ")

# set menjadi 10 row
print(data.head(10))
print(" ")




# mencetak lima row pertama dari bawah (default)
print(data.tail())
print(" ")

# set menjadi 10
print(data.tail(10))
print(" ")


# mengambil informasi mengenai dataset
print(data.info())
print(" ")


# cek duplikasi data
print(data.nunique())
print(" ")


# perhitungan nilai
print(data.isnull()) # digunakan untuk mengetahui record yang tidak memiliki nilai
print(data.isnull().sum()) # digunakan untuk mendapatkan jumlah record yg hilang di setiap kolom
print(" ")