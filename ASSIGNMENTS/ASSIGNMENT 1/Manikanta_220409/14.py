import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
region1_sales = np.random.randint(50,100,5)
region2_sales = np.random.randint(50,100,5)

x = np.arange(len(products))

plt.figure(figsize=(10, 6))
plt.bar(x - 0.1, region1_sales, width=0.2, label="Region 1")
plt.bar(x + 0.1, region2_sales, width=0.2, label="Region 2")
plt.xticks(x, products)
plt.title("Sales Comparison by Product and Region")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()
plt.show()


