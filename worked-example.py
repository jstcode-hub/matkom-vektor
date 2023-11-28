import numpy as np

def calculate_surface_area_and_normal_vector(A, B, C):
    # Menghitung vektor u dan v
    u = B - A
    v = C - A

    # Menghitung vektor normal
    normal_vector = np.cross(u, v)

    # Menghitung magnitudo vektor normal
    magnitude = np.linalg.norm(normal_vector)

    # Menghitung luas permukaan segitiga
    surface_area = 0.5 * magnitude

    return surface_area, normal_vector

# Mendefinisikan titik-titik segitiga
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])

# Menghitung luas permukaan dan vektor normal
area, normal_vector = calculate_surface_area_and_normal_vector(A, B, C)

print("Vektor Normal:", normal_vector)
print("Luas Permukaan Segitiga:", area)
