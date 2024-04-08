# list adalah tipe data yang bisa menampung banyak data sekaligus tanpa terbatas panjangnya
# list bisa menampung berbagai jenis tipe data
# perlu diingat index list dimulai dari 0 bukan 1


#** <=================================================================> **#
#** <=================================================================> **#

this_list = ["Budi", "Budiman", "Budiono", "Budianto", 18, False]

# mengakses data list
print("Hello my name is", this_list[0], this_list[1], this_list[2], this_list[3])
print("My age is", this_list[4])
print("Girlfriend?", this_list[5])



# kita juga bisa memasukan list didalam list
address_data = ["Jl. Pengairan", ["Senayan", "no.100"], "Jakarta Pusat"]

# akses data list didalam list
print(address_data[0])
print(address_data[1][0])
print(address_data[1][1])
print(address_data[2])
