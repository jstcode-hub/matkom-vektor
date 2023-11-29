import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan dua vektor 2D
vector_1 = np.array([5, 3])
vector_2 = np.array([-8, 2])

# Operasi penjumlahan vektor
result_vector = vector_1 + vector_2

# Plotting vektor
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, vector_1[0], vector_1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vektor 1')
plt.quiver(0, 0, vector_2[0], vector_2[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vektor 2')
plt.quiver(0, 0, result_vector[0], result_vector[1], angles='xy', scale_units='xy', scale=1, color='g', label='Hasil Penjumlahan')

# Menambahkan label, grid, dan legend
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Penjumlahan Vektor 2D')

# Menampilkan hasil penjumlahan vektor
plt.text(result_vector[0], result_vector[1], f'{result_vector}', fontsize=12, ha='right')

plt.show()
