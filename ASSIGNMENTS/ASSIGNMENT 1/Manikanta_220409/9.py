import numpy as np
import pandas as pd

data = pd.read_csv('Titanic-Dataset.csv')
print(data.shape)

list1 = []

for i in range(len(data)):
    if data.loc[i,'Age'] < 18 :
        list1.append(i)

print(data.iloc[list1, : ])

list2 = []

for i in range(len(data)):
    if data.loc[i, "Sex"] == "female" and data.loc[i, "Survived"] :
        list2.append(i)

print(data.iloc[list2, :])