
arr = []
n = int(input("Enter Size: "))
num = int(input("Enter Number: "))

for i in range(0, n):
    arr.append(int(input("Enter List elements : ")))

arr = [i for i in arr if i >= num]


print(f"LIST after removing elements: {arr}")
