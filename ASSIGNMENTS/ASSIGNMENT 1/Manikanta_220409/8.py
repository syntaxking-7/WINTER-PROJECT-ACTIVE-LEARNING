import numpy as np
import pandas as pd

data = {
    "Product" : ["Soap", "Shampoo", "Conditioner", "Face Wash", "Moisturizer", "Sunscreen", "Talcumm", "Perfurm"],
    "Price" : np.random.randint(100,500,8),
    "Quantity" : np.random.randint(1,5,8)
}

df = pd.DataFrame(data, index=range(1,9))

# print(df)

total_value = []


for i in range(8):
    total_value.append(df.iloc[i,1]*df.iloc[i,2])

print("Total Values = ", total_value)

df['Total'] = total_value

print(df)



