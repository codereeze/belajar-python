import matplotlib.pyplot as plt
import numpy as np

lang_labels = np.array(['PHP', 'JavaScript', 'TypeScript', 'Python', 'C++', 'Dart'])
y = np.array([100, 250, 500, 300, 1000, 400])

# jika ingin horizontal gunakan barh()
plt.pie(y, labels = lang_labels)
plt.title("Statistik bahasa pemrograman harian", fontdict={'color': 'green', 'size': 15}, loc='center')
plt.legend(title = "Bahasa pemrograman")

plt.show()