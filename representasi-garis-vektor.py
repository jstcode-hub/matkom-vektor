import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan titik awal P dan vektor arah v
P = np.array([1, 2])
v = np.array([2, 3])

# Menghitung titik Q pada garis untuk t=2
t = 2
Q = P + t * v

# Plot titik P dan Q
plt.plot([P[0], Q[0]], [P[1], Q[1]], marker='o', label='Garis')
plt.text(P[0], P[1], ' P', fontsize=12, ha='right')
plt.text(Q[0], Q[1], ' Q', fontsize=12, ha='right')

# Menandai vektor arah v
plt.quiver(P[0], P[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vektor Arah')

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.legend()
plt.grid(True)
plt.show()
