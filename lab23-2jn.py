import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import matplotlib.pyplot as plt

# Datos
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Crear figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot de la superficie
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, antialiased=False)

# Personalizar el eje z
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Añadir barra de colores
fig.colorbar(surf, shrink=0.5, aspect=5)

# Mostrar gráfico
plt.show()