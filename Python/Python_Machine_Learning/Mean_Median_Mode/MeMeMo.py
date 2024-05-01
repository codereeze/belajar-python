import numpy as np
from scipy import stats

nilai = [70, 80, 75, 86, 90, 96, 87, 77, 60, 98, 90]

# rata-rata (mean)
rata_rata_nilai = np.mean(nilai)
print(rata_rata_nilai)


# mencari nilai tengan (median)
nilai = [70, 80, 75, 86, 90, 96, 87, 77, 60, 98, 90]
nilai_tengah = np.median(nilai)
print(nilai_tengah)


# mencari nilai yang sering muncul (mode)
nilai_sering_muncul = stats.mode(nilai)
print(nilai_sering_muncul.mode)

