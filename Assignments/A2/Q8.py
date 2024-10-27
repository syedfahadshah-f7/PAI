import numpy as np

arr = np.array([[2, -1, 1],
              [1, 3, 2],
              [1, -1, 2]])

brr = np.array([8, 13, 17])

print(f"Solution Matrix:\n {np.linalg.solve(arr, brr)}")