import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([2, 5, 9, 4, 9, 15])

# @param ls => line style
# @param color => line color
# @param linewidth => line width
plt.plot(y_points, ls = '--', color = 'g', linewidth = 10)
plt.show()


# multiple line
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()