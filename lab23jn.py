import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Semilla para reproducibilidad
np.random.seed(19680801)

# Generación de datos
x = np.arange(5)
y = np.random.rand(5)
z = np.zeros(5)

# Crear una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Colores para diferentes planos
colors = ['r', 'g', 'b', 'y']

# Graficar barras en diferentes planos y
for i in range(4):
    ax.bar(x, y, zs=i, zdir='y', color=colors[i], alpha=0.8)

# Etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Gráficos de Barras 2D en Diferentes Planos 3D')

# Mostrar gráfico
plt.show()