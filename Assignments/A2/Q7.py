import numpy as np
import random
arr = np.random.randint(1,100,50)
print(f"Matrix: \n {arr}")
print(f"Maximum Index: {np.argmax(arr)}")
print(f"Minimum Index: {np.argmin(arr)}")
