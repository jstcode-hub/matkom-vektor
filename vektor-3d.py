import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fungsi untuk operasi vektor
def perform_vector_operation():
    print("Pilih operasi vektor:")
    print("1. Penjumlahan")
    print("2. Pengurangan")

    operation_choice = input("Masukkan nomor operasi yang diinginkan (1-2): ")

    if operation_choice not in ['1', '2']:
        print("Pilihan tidak valid.")
        return

    # Meminta input pengguna untuk komponen vektor
    print('Masukkan komponen vektor pertama:')
    x1 = float(input("Komponen X: "))
    y1 = float(input("Komponen Y: "))
    z1 = float(input("Komponen Z: "))
    vector_1 = np.array([x1, y1, z1])

    print('Masukkan komponen vektor kedua:')
    x2 = float(input("Komponen X: "))
    y2 = float(input("Komponen Y: "))
    z2 = float(input("Komponen Z: "))
    vector_2 = np.array([x2, y2, z2])

    # Melakukan operasi sesuai pilihan
    if operation_choice == '1':
        result_vector = vector_1 + vector_2
    elif operation_choice == '2':
        result_vector = vector_1 - vector_2

    print('Hasil operasi vektor:', result_vector)

    # Plotting vektor dan sumbu
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Menambahkan vektor 1
    ax.quiver(0, 0, 0, vector_1[0], vector_1[1], vector_1[2], color='b', label='Vektor 1')

    # Menambahkan vektor 2
    ax.quiver(0, 0, 0, vector_2[0], vector_2[1], vector_2[2], color='r', label='Vektor 2')

    # Menambahkan hasil operasi vektor
    ax.quiver(0, 0, 0, result_vector[0], result_vector[1], result_vector[2], color='g', label='Hasil Operasi')

    # Menambahkan label dan legend
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')
    ax.legend()

    # Menambahkan plot sumbu X
    plt.plot([0, vector_1[0]], [0, vector_1[1]], [0, vector_1[2]], 'b--', label='Sumbu X')

    # Menambahkan plot sumbu Y
    plt.plot([0, vector_2[0]], [0, vector_2[1]], [0, vector_2[2]], 'r--', label='Sumbu Y')

    # Menambahkan plot sumbu Z
    plt.plot([0, result_vector[0]], [0, result_vector[1]], [0, result_vector[2]], 'g--', label='Sumbu Z')

    # Menampilkan plot
    plt.title('Operasi Vektor 3D')
    plt.show()

# Memanggil fungsi operasi vektor
perform_vector_operation()
