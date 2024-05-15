import numpy as np
from scipy import stats

data = [29, 40, 99, 76, 54, 20]


# mencari nilai rata-rata (mean)
mean = np.mean(data)
print(f"Rata-rata dari data adalah {mean}")


# mencari nilai tengah (median)
median = np.median(data)
print(f"Nilai tengah dari data adalah {median}")


# mencari nilai yang sering muncul (mode)
mode = stats.mode(data).mode
print(f"Nilai yang sering muncul dari data adalah {mode}")


# mencari selisih min & max (range)
ptp = np.ptp(data)
print(f"Range min & max dari data adalah {ptp}")


# mencari variasi data (variance)
variance = np.var(data)
print(f"Variasi dari data adalah {variance}")


# mencari simpangan baku (standard deviation)
std = np.std(data)
print(f"Standard deviation dari data adalah {std}")
