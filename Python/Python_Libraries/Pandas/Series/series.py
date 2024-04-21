import pandas as pd

# Series adalah struktur data satu dimensi mirip dengan array di python. Setiap elemen dalam Series memiliki label yang disebut indeks, yang memungkinkan akses dan pengindeksan data dengan mudah.

data = [10, 20, 30, 40, 50]

print("Output dari series 1: ")
series1 = pd.Series(data)
print(series1)


print(" ")


# labeling index
print("Output dari series 2: ")
indexes = ["A", "B", "C", "D", "E"]
series2 = pd.Series(data, index = indexes)
print(series2)


print(" ")


# bisa juga dengan operasi matematika
print("Output dari series 3: ")
series3 = pd.Series(data, index=indexes)
# mengakses element series
print(series3.iloc[0])
series3 = series3 * 2
print(series3)

