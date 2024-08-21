count = 0
arr = []
n = int(input("Enter Size: "))

for i in range(0, n):
    arr.append(int(input("Enter List elements : ")))

for i in arr:
    if i % 2 == 0:
        count += 1

print("Total Count of Even Numbers: ", count)
