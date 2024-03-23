# for-loop digunakan untuk melakukan perulangan pada string, list, dan lain-lain
# for-loop biasanya digunakan untuk mengiterasi element untuk diambil nilainya

#** <=================================================================> **#
#** <=================================================================> **#

# penggunaan pada list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# penggunaan pada string
say_hello = "Hello World!"

for char in say_hello:
    print(char)



# penggunaan for-loop dengan method range
for i in range(5):
    print(i)


# penggunaan method range pada list
matkul = ["dasar pemrograman", "matematika", "logika & algoritma", "entrepreneurship"]

for i in range(len(matkul)):
    print("saya suka mata kuliah", matkul[i])
