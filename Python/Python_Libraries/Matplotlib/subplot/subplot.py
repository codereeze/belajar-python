import matplotlib.pyplot as plt
import numpy as np

x1_points = np.array(['PHP', 'JavaScript', 'TypeScript', 'Python', 'C++', 'Dart'])
y1_points = np.array([100, 250, 500, 300, 1000, 400])

x2_points = np.array(['MySQL', 'Postgree SQL', 'MongoDB', 'Redis', 'Oracle', 'SQLite'])
y2_points = np.array([500, 700, 1000, 100, 200, 400])


# plot 1
plt.subplot(1, 2, 1) # row, column, sequence
plt.plot(x1_points, y1_points)
plt.title("Statistik bahasa pemrograman",)
plt.xlabel('Bahasa pemrograman', fontdict={'family': 'sans-serif', 'color': 'red'})
plt.ylabel('Pengguna', fontdict={'family': 'sans-serif', 'color': 'red'})
plt.grid()

# plot 2
plt.subplot(1, 2, 2)
plt.plot(x2_points, y2_points)
plt.title("Statistik Database")
plt.xlabel('Database', fontdict={'family': 'sans-serif', 'color': 'green'})
plt.ylabel('Pengguna', fontdict={'family': 'sans-serif', 'color': 'green'})
plt.grid()


plt.suptitle('Statistik Tech Stack')
plt.show()