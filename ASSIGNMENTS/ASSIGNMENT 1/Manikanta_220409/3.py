import pandas as pd
import numpy as np



data = {
    "Names" : ["Mani", "Hary", "Saga", "Vank", "Katt"],
    "Age" : np.random.randint(18,21, 5),
    "Score" : np.random.randint(50,100, 5)
}

df = pd.DataFrame(data, index = [x for x in range(1,6)])

df.to_csv('data.csv')

new_df = pd.read_csv('data.csv')
new_df = new_df.drop(new_df.columns[0], axis = 1)

list1 = []

for i in range(0,5):
    if new_df.iloc[i,2] > 75:
       list1.append(i)

print(data.iloc[list1, : ])


