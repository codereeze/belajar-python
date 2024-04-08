# kita bisa menginputkan data melalui terminal
# yaitu menggunakan method input, perlu diingat methon input selalu mengembalikan nilai berupa string
# jadi misalkan kita ingin nilainya sesuai dengan keinginan, kita harus melakukan casting / konversi tipe data

#** <=================================================================> **#
#** <=================================================================> **#


# menggunakan method input tanpa casting
name = input("Masukkan nama lengkap Anda: ")
print("Nama saya,", name)

# menggunakan method input dengan casting
age = int(input("Masukkan umur Anda: "))
print("Umur saya,", age, "tahun")