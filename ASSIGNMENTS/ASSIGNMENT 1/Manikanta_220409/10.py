import numpy as np
import pandas as pd

data = pd.read_csv('IRIS.csv')
# data.head(10)

data = data.sort_values(by = 'species')

setosa_pl, versicolor_pl, virginica_pl = 0, 0, 0
setosa_sw, versicolor_sw, virginica_sw = 0, 0, 0
setosa_n, versicolor_n, virginica_n = 0, 0, 0



# print(len(data))

for i in range(len(data)):
    if data.loc[i,"species"] == 'Iris-setosa':
        setosa_pl += data.loc[i, "petal_length"]
        setosa_sw += data.loc[i, "sepal_width"]
        setosa_n += 1
    elif data.loc[i,"species"] == 'Iris-versicolor':
        versicolor_pl += data.loc[i, "petal_length"]
        versicolor_sw += data.loc[i, "sepal_width"]
        versicolor_n += 1
    else:
        virginica_pl += data.loc[i, "petal_length"]
        virginica_sw += data.loc[i, "sepal_width"]
        virginica_n += 1


print("Mean of petal lengths:")
print("1. Iris-setosa: ", setosa_pl/setosa_n)
print("2. Iris-versicolor: ", versicolor_pl/versicolor_n)
print("3. Iris-virginica: ", virginica_pl/virginica_n)
print("Mean of sepal widths:")
print("1. Iris-setosa: ", setosa_sw/setosa_n)
print("2. Iris-versicolor: ", versicolor_sw/versicolor_n)
print("3. Iris-virginica: ", virginica_sw/virginica_n)

