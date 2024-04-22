import pandas as pd

# Membuat DataFrame contoh
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 2, 1, 2, 1]}

df = pd.DataFrame(data)

# Menghitung korelasi antara kolom-kolom dalam DataFrame
correlation_matrix = df.corr()

print("Matrix Korelasi:")
print(correlation_matrix)
