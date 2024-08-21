sm = 0
arr = []
n = int(input("Enter Size: "))

for i in range(0, n):
    arr.append(int(input("Enter List elements : ")))

for i in arr:
    sm += i

print("Sum of all Elements: ", sm)
