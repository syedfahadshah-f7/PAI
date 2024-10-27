import numpy as np 

arr = np.arange(1,5).reshape(2,2)

print(f"Determinenet: \n{np.linalg.det(arr)}")
print(f"Inverse: \n{np.linalg.inv(arr)}")
