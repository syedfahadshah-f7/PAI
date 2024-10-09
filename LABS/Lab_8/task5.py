import numpy as np

arr = np.random.choice([2,5,9,10],size = (4,4))
print("Array \n",arr,'\n')
arr = np.multiply(arr,np.eye(4,4))
print("Array after multiplying Identity Matrix \n",arr,'\n')
newarr = np.arange(1,32,2)
newarr = newarr.reshape(4,4)
print("Odd Values Array \n",newarr,'\n')
brr = np.add(arr,newarr)
print("After adding both arrays \n",brr,'\n')

