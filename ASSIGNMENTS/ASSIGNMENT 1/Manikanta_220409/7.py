import numpy as np

array1 = np.random.randint(1,20,(4,4))
array2 = np.random.randint(1,20,4)

# print(array1, "\n")
# print(array2)

result = np.zeros_like(array1)

for i in range(4):
    result[i, :] = array1[i, :] + array2

print(result)
