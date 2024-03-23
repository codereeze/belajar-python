# sama seperti list kita bisa memanipulasi dictionary
# menambah, menghapus, mengubah dan lain-lain

#** <=================================================================> **#
#** <=================================================================> **#


person = {
    "name": "Faiz Akamz",
    "age": 30,
    "color favorite": "Red",
    "address": {
        "street name": "Jl. Semoga lancar selalu",
        "district": "Balaraja",
        "city": "New York",
        "country": "USA"
    }
}

body_characteristics = {
    "skin_color": "black",
    "eye_color": "black",
    "hair type": "curly"
}




# mengubah 
person["name"] = "Faiz Nurhidayat"
print(person["name"])


# menambah
person["hobby"] = "dance, singing"
print(person["hobby"])


# menghapus
del person["color favorite"]
print(person)


# menggabungkan dictionary
person.update(body_characteristics)
print(person)


# menghapus semua element
body_characteristics.clear()
print(body_characteristics)