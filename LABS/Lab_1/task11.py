dic ={}
avg = 0
per = 0
for i in range(3):
    key = input("Enter Subject Name: ")
    Val = int(input("Enter Marks : "))
    dic[key] = Val
    avg += Val

per = (avg/300) *100
avg = avg /3

print(f"Average marks: {avg} \n Percentage is: {per}")
