nums = input("Enter Lists Element: ").split()

max =0

for i in nums:
    if int(i) > max:
        max = int(i)

print("Max Element in list is: ",max)
