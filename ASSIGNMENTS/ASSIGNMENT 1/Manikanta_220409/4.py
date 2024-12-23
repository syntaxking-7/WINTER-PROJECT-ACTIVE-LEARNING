import numpy as np
import pandas as pd

array = np.random.randint(10,100,25)

print("Maximum: ", array.max(), "Index: ", array.argmax())
print("Minimum: ", array.min(), "Index: ", array.argmin())

print(array)

for i in range(array.size):
    if array[i]%2 != 0:
        array[i] = -1
    
print(array)


