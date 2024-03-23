# pengkondisian (conditional) atau percabangan adalah konsep dalam pemrograman yang digunakan untuk menguji suatu kondisi.
# jika suatu kondisi terpenuhi maka akan menjalankan blok kode benar dan jika tidak terpenuhi maka akan menjalankan blok kode salah

# di Python kita tidak menggunakan kurung kurawal sebagai pemisah block kode
# tapi menggunakan indentasi whitespace / spasi
# selama space depannya sama maka akan dianggap masih satu block

#** <=================================================================> **#
#** <=================================================================> **#


# if statement
# if statement akan di eksekusi jika kondisinya benar, jika kondisinya salah maka akan di lewati
size = "lg"
if size == "lg":
    print("saya memilih baju ukuran", size)

# kode dibawah ini sudah diluar block if
print("Terimakasih sudah membeli di toko kami")


print()


# if else statement
# block else baru akan dijalankan jika block if kondisinya tidak terpenuhi
size = "medium"
if size != "medium":
    print("stok ukuran", size, "masih tersedia banyak")
else:
    print("mohon maaf, kami tidak menyediakan ukuran", size)


print()


# if elif else statement
# elif akan dieksekusi ketika kondisi if tidak terpenuhi, namun tidak akan dieksekusi juga jika kondisi elif tidak terpenuhi
size = "small"
if size == "large":
    print("ukuran", size, "masih tersedia")
elif size == "small":
    print("anda memilih baju dengan ukuran", size)
    print("terimakasih sudah berbelanja di toko kami")
else:
    print("ukuran baju", size, "tidak ada di toko kami")