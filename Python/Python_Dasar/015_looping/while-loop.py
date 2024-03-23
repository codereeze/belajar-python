# while-loop adalah perulangan dengan acuan kondisinya
# selama kondisinya terpenuhi maka while-loop akan terus dijalankan

#** <=================================================================> **#
#** <=================================================================> **#

i = 0
while i < 10: # jika kondisinya true maka akan dijalankan
    print("ini adalah loop ke", i)
    i += 1


print()

# while else statement
# block else akan dieksekusi jika kondisi while tidak terpenuhi
i = 10
while i < 10:
    print("Hello World!")
else:
    print("nilai variable i sama dengan 10")


