import matplotlib.pyplot as plt
import numpy as np

MIN = -15
MAX = 39
N = abs(MIN) + MAX

cmap = plt.colormaps['turbo']
valeurs = np.linspace(0, 1, N)

COULEUR = [
    f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"
    for (r, g, b, _) in cmap(valeurs)
]
