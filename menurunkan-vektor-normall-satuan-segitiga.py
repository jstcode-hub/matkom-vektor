import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compute_unit_normal(vector_u, vector_v):
    # Hitung vektor normal menggunakan cross product
    cross_product = np.cross(vector_u, vector_v)

    # Normalisasi vektor normal
    unit_normal = cross_product / np.linalg.norm(cross_product)

    return unit_normal

# Contoh titik pada segitiga (A, B, C)
point_A = np.array([0, 0, 0])
point_B = np.array([1, 0, 0])
point_C = np.array([0, 1, 0])

# Hitung vektor AB dan AC
vector_AB = point_B - point_A
vector_AC = point_C - point_A

# Hitung vektor normal satuan segitiga
unit_normal_triangle = compute_unit_normal(vector_AB, vector_AC)

# Visualisasi segitiga dan vektor normal satuan
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot segitiga
ax.plot([point_A[0], point_B[0], point_C[0], point_A[0]],
        [point_A[1], point_B[1], point_C[1], point_A[1]],
        [point_A[2], point_B[2], point_C[2], point_A[2]], 'b-', label='Segitiga ABC')

# Plot vektor normal satuan
ax.quiver(point_A[0], point_A[1], point_A[2],
          unit_normal_triangle[0], unit_normal_triangle[1], unit_normal_triangle[2],
          color='r', label='Vektor Normal Satuan')

# Menambahkan label dan legend
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_zlabel('Sumbu Z')
ax.legend()

# Menampilkan plot
plt.title('Visualisasi Vektor Normal Satuan Segitiga')
plt.show()
