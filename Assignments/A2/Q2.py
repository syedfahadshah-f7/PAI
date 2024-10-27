import numpy as np

arr = np.arange(1,10).reshape(3,3)
print(f"Original Matrix: \n {arr}")

arr = np.transpose(arr)
print(f"Transposed Matrix:\n {arr}")