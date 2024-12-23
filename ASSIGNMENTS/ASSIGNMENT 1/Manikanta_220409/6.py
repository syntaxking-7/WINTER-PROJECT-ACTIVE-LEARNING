import numpy as np

array = np.random.ranf((3,4,5))

print(array, "\n")

print("Mean :", array.mean())
print("Median :", np.median(array))
print("Standard deviation :", np.std(array), "\n")

normalized_array = (array - array.mean())/np.std(array)
print(normalized_array)