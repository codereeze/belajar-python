import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points)
plt.show()


# tanpa garis

x_points = np.array([2, 12])
y_points = np.array([4, 14])

plt.plot(x_points, y_points, "o")
plt.show()


# multiple points

x_points = np.array(["PHP", "JavaScript", "Python", "TypeScript"])
y_points = np.array([100, 200, 500, 900])

plt.plot(x_points, y_points)
plt.show()


# default X-point
# otomatis akan digenerate jika tidak ada xpoints

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()