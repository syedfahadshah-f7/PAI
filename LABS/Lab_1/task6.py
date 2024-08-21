n = int(input("Enter total subjects: "))
dic = {}

for i in range(n):
    key = input("Enter Course Name: ")
    val = int(input("Enter Marks: "))
    dic[key] = val

avg = 0
highest = 0
name = ""
for x in dic:
    if highest < dic[x]:
        highest = dic[x]
        name = x
    avg += dic[x]

print(f"Average: {avg/3.}")
print(f"Highst Marks taken in : {name}")
