import numpy as np

arr = np.random.randint(1,100,9).reshape(3,3)
print(f"Original Matrix: \n {arr}")

arr = np.transpose(arr)
print(f"Transposed Matrix:\n {arr}")
