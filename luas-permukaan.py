import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_surface_area(A, B, C):
    # Menghitung dua vektor pada bidang segitiga
    u = B - A
    v = C - A

    # Menghitung vektor normal
    normal_vector = np.cross(u, v)

    # Menghitung magnitudo vektor normal
    magnitude = np.linalg.norm(normal_vector)

    # Menghitung luas permukaan segitiga
    surface_area = 0.5 * magnitude

    return surface_area

# Mendefinisikan titik-titik segitiga
A = np.array([1, 1, 1])
B = np.array([2, 4, 1])
C = np.array([3, 2, 2])

# Menghitung luas permukaan segitiga
surface_area = calculate_surface_area(A, B, C)

print("Luas Permukaan Segitiga:", surface_area)

# Plotting segitiga
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], [A[2], B[2], C[2], A[2]], 'b-', label='Segitiga')

# Menambahkan label dan legend
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_zlabel('Sumbu Z')
ax.legend()

# Menampilkan plot
plt.title('Luas Permukaan Segitiga')
plt.show()
