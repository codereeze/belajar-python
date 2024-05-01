import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 6, 3, 12, 3, 15])

plt.plot(y_points, marker = 'o')
plt.show()


# marker using format string
# @param ms => point size
# @param mec => border radius color at points
# @param mfc => set color inside the edge of markers

plt.plot(y_points, 'o-r', ms = 10, mec = 'b', mfc = 'hotpink')
plt.show()