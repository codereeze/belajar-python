# dictionary adalah tipe data yang memungkinkan kita menyimpan data dengan pasangan key (kunci) dan value (nilai)
# nama key di dictionary bisa bertipe apa saja entah itu string, integer, float, dan lain-lain dengan syarat harus unik (key tidak boleh sama)
# dictionary adalah tipe data yang mirip seperti object literals di JavaScript

#** <=================================================================> **#
#** <=================================================================> **#

person = {
    "name": "Atyla Azfa Al Harits",
    "class": "XII RPL 1",
    1: 18,
    2.1: 50,
    "hobby": "bermain game",
    "school": "SMK Negeri 3 Jakarta"
}

# mengakses data dictionary
print(person["name"])
print(person["class"])
print(person[1], "tahun")
print(person[2.1], "kg")
print(person["hobby"])
print(person["school"])


print()


# kita bisa menggunakan method dictionary untuk mendapatkan data key, value, atau key dan value
print("data keys")
print(person.keys())

print()

print("data values")
print(person.values())

print()

print("data keys dan values")
print(person.items())