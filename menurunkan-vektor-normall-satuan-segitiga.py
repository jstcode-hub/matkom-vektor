import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_unit_normal_vector(A, B, C):
    # Menghitung dua vektor pada bidang segitiga
    u = B - A
    v = C - A

    # Menghitung vektor normal
    normal_vector = np.cross(u, v)

    # Menghitung magnitudo vektor normal
    magnitude = np.linalg.norm(normal_vector)

    # Menghitung vektor normal satuan
    unit_normal_vector = normal_vector / magnitude

    return unit_normal_vector

# Mendefinisikan titik-titik segitiga
A = np.array([1, 1, 1])
B = np.array([2, 4, 1])
C = np.array([3, 2, 2])

# Menghitung vektor normal satuan
unit_normal_vector = calculate_unit_normal_vector(A, B, C)

# Plotting segitiga dan vektor normal satuan
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Menambahkan segitiga
ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], [A[2], B[2], C[2], A[2]], 'b-', label='Segitiga')

# Menambahkan vektor normal satuan
ax.quiver(A[0], A[1], A[2], unit_normal_vector[0], unit_normal_vector[1], unit_normal_vector[2],
          color='r', label='Vektor Normal Satuan')

# Menambahkan label dan legend
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_zlabel('Sumbu Z')
ax.legend()

# Menampilkan plot
plt.title('Vektor Normal Satuan Segitiga')
plt.show()

print("Vektor Normal Satuan:", unit_normal_vector)
