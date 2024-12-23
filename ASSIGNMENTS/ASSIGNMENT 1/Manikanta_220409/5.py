import numpy as np

matrix = np.random.randint(0,100,(5,5))
print(matrix)

diagonal_ele = []

for i in range(5):
    diagonal_ele.append(matrix[i][i])

print(diagonal_ele, "\n")

sum = 0

for i in range(5):
    for j in range(5):
        if j > i :
            sum += matrix[i][j]

print("Sum = ", sum)