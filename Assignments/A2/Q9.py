import  numpy as np

arr= np.random.randint(1,100,25)

print(f"Matrix: \n {arr}")
print(f" 75th percentile: {np.percentile(arr,75)}")