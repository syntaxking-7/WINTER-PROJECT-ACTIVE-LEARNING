import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("IRIS.csv")

species = iris['species'].unique()
colors = ['r', 'g', 'b']

plt.figure(figsize=(10, 6))
for sp, color in zip(species, colors):
    subset = iris[iris['species'] == sp]
    plt.scatter(subset['petal_length'], subset['petal_width'], label=sp, color=color)

plt.title("Petal Length vs Petal Width by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend(title="Species")
plt.grid(True)
plt.show()
