import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([3.31, 7.05, 10.17, 13.16, 16, 18.75, 20.69, 22.62, 25.31, 26.89, 27.82, 30.06, 31.34, 33.14, 34.9, 38.51, 41.77, 45.24, 48.45])
y = np.array([4.38, 5.97, 7.46, 8.25, 10, 11.07, 10.63, 10.15, 12.57, 10.59, 12.26, 10.59, 11.16, 10.32, 9.13, 8.61, 6.8, 5.26, 4.29])

cs_sujeto = CubicSpline(x, y, bc_type='clamped')  

cs_natural = CubicSpline(x, y, bc_type='natural')  

x_new = np.linspace(min(x), max(x), 500)
y_sujeto = cs_sujeto(x_new)
y_natural = cs_natural(x_new)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Datos Originales', markersize=6)  
plt.plot(x_new, y_sujeto, label='Interpolación Cúbica Sujeto', linestyle='--')  
plt.plot(x_new, y_natural, label='Interpolación Cúbica Natural', linestyle='-')  
plt.title('Interpolación Cúbica Sujeto y Natural')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()