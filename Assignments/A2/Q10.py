import numpy as np

def Normalize(arr):
    mean = arr.mean()
    std = arr.std()
    arr = [(i-mean)/std for i in arr]
    return arr
arr = np.array([2,4,6,7,8,5,3,2,6])
print(f"Original Array: {arr}")
arr = np.array(Normalize(arr))
print(f"After Normalizing: {arr}")

