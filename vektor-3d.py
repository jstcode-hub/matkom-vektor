import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Mendefinisikan dua vektor 3D
vector_1 = np.array([1, 2, 3])
vector_2 = np.array([-2, 1, 2])

# Operasi penjumlahan vektor
result_vector = vector_1 + vector_2

# Plotting vektor
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Menambahkan vektor 1
ax.quiver(0, 0, 0, vector_1[0], vector_1[1], vector_1[2], color='b', label='Vektor 1')

# Menambahkan vektor 2
ax.quiver(0, 0, 0, vector_2[0], vector_2[1], vector_2[2], color='r', label='Vektor 2')

# Menambahkan hasil penjumlahan vektor
ax.quiver(0, 0, 0, result_vector[0], result_vector[1], result_vector[2], color='g', label='Hasil Penjumlahan')

# Menambahkan label dan legend
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_zlabel('Sumbu Z')
ax.legend()

# Menampilkan plot
plt.title('Penjumlahan Vektor 3D')
plt.show()
