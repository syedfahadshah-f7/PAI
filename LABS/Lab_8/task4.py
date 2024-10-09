import numpy as np

data_type =[("name","S15"),("class",int),("height",float)]
students =[("Fahad",14,5.8),("umar",10,5.7),("Raghib",18,5.2),("Saif",5,6.0)]

arr = np.array(students, dtype = data_type)
print(arr);

arr = np.sort(arr, order=["class", "height"])
print("After Sort: \n",arr);
