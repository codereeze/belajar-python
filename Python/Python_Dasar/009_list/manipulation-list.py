# kita juga bisa memanipulasi data list
# seperti menambah, menghapus, mengubah, dan lain-lain

#** <=================================================================> **#
#** <=================================================================> **#

cat_family = ["kucing", "singa", "harimau"]

# menambah dan menyisipkan data pada index tertentu
cat_family.append("jaguar")
cat_family.insert(1, "macan")

print(cat_family)

# menghapus data pada list
cat_family.remove("singa") # menghapus berdasarkan nilai

poped_element = cat_family.pop(0) # menghapus dan mengembalikan nilai pada index tertentu
print(poped_element) 
print(cat_family)

del cat_family[2] # menghapus nilai berdasarkan index
print(cat_family)

# mengubah nilai
cat_family[0] = "leopard"
print(cat_family)


print()


# menggabungkan list
abjad_satu = ["a", "b", "c", "d", "e", "f", "g"]
abjad_dua = ["h", "i", "j", "k", "l", "m", "n"]

abjad_satu.extend(abjad_dua)
print(abjad_satu)


# mengetahui panjang list
print(len(abjad_satu))


# mengurutkan list
random_number = [9,3,4,6,8,7,1,2,5,0]
random_number.sort()
print(random_number)


# me-reverse urutan list
random_number.reverse()
print(random_number)