import json
dic = {}

for i in range(6):
    name = input("Enter Name and age of Person : ")
    age = int(input())
    dic[name] = age
try:
    f = open("task5.json",'w')
    json.dump(dic,f)
    f.close()
except Exception as e:
    print("error: ", str(e))

try:
    data = {}
    f = open("task5.json")
    data = json.load(f)
    f.close()
except Exception as e:
    print("error: ", str(e))
maxAge = 0
name = " "
sameAge = set()
for i in data:
    if maxAge < data[i]:
        maxAge = data[i]
        name = i
    for j in data:
        if data[i] == data[j] and i != j :
            sameAge.add(i)
            sameAge.add(j)

print("Same age Names: ", sameAge)
print("Max Age",maxAge, "Name: ", name)