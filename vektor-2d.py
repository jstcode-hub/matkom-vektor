import numpy as np
import matplotlib.pyplot as plt

# Definisi operasi
def vector_addition(vector1, vector2):
    return vector1 + vector2

def vector_subtraction(vector1, vector2):
    return vector1 - vector2

def vektor_operation():
    print("Pilih operasi:")
    print("1. Penjumlahan Vektor")
    print("2. Pengurangan Vektor")

    choice = input("Masukkan nomor operasi yang diinginkan (1-2): ")

    if choice not in ['1', '2']:
        print("Pilihan tidak valid.")
        return

    # Meminta input pengguna untuk komponen vektor
    print('Masukkan angka vektor pertama')
    x1 = float(input("Masukkan komponen X: "))
    y1 = float(input("Masukkan komponen Y: "))
    vector1 = np.array([x1, y1])

    print('Masukkan angka vektor Kedua')
    x2 = float(input("Masukkan komponen X: "))
    y2 = float(input("Masukkan komponen Y: "))
    vector2 = np.array([x2, y2])

    # Melakukan operasi sesuai pilihan
    if choice == '1':
        result = vector_addition(vector1, vector2)
        operation_label = 'Penjumlahan'
    elif choice == '2':
        result = vector_subtraction(vector1, vector2)
        operation_label = 'Pengurangan'

    print('Hasil operasi vektor:', result)

    # Plotting vektor dan hasil operasi
    plt.figure(figsize=(8, 8))

    # Plot vektor 1
    plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vektor 1')

    # Plot vektor 2
    plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vektor 2')

    # Plot hasil operasi vektor
    plt.quiver(0, 0, result[0], result[1], angles='xy', scale_units='xy', scale=1, color='g', label=f'Hasil {operation_label}')

    # Menambahkan label, grid, dan legend
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title(f'Operasi Vektor 2D - {operation_label}')

    # Menampilkan hasil operasi vektor
    plt.text(result[0], result[1], f'{result}', fontsize=12, ha='right')

    # Menunjukkan sumbu x dan y sebagai garis biru pada plot
    plt.plot([0, vector1[0]], [0, vector1[1]], 'b--', label='Sumbu X')
    plt.plot([0, vector2[0]], [0, vector2[1]], 'g--', label='Sumbu Y')
    plt.plot([0, result[0]], [0, result[1]], 'r--', label='Sumbu Y')

    plt.show()

# Memanggil fungsi operasi vektor
vektor_operation()
