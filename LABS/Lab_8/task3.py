import numpy as np

arr = np.arange(2,19,2).reshape(3,3)

def multiply(x,y):
    return x*y

MUL_Func = np.frompyfunc(multiply,2,1)

newarr = MUL_Func(arr,4)

brr = np.multiply(np.eye(3,3),newarr)

print(arr,'\n')
print(newarr,'\n')
print(brr)
