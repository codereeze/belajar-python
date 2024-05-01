import matplotlib.pyplot as plt
import numpy as np

x_points = np.array(['PHP', 'JavaScript', 'TypeScript', 'Python', 'C++', 'Dart'])
y_points = np.array([100, 250, 500, 300, 1000, 400])

# jika ingin horizontal gunakan barh()
plt.bar(x_points, y_points)
plt.title("Statistik bahasa pemrograman harian", fontdict={'color': 'green', 'size': 15}, loc='left')
plt.xlabel('Bahasa pemrograman', fontdict={'family': 'sans-serif', 'color': 'red'})
plt.ylabel('Pengguna harian', fontdict={'family': 'sans-serif', 'color': 'red'})

plt.show()