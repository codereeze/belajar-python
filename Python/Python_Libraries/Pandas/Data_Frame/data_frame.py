import pandas as pd

weather_notes = {
    "temperatures": [39, 29, 30, 35, 40],
    "day": [1, 2, 3, 4, 5]
}

frame = pd.DataFrame(weather_notes)
# mengambil data dari index ke-0
print(frame.loc[0])

print(" ")

# mengambil data index ke-0 dan index ke-3
print(frame.loc[[0, 3]])

print(" ")


# mengganti index dengan key
days = ['Day-1', 'Day-2', 'Day-3', 'Day-4', 'Day-4']
frame = pd.DataFrame(weather_notes, index = days)
print(frame)

print(" ")

# ambil lokasi
print(frame.loc['Day-1'])


# penggunaan sama seperti diatas