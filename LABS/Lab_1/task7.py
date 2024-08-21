str = input("Enter String to Reverse: ")
ctr = ""
for i in range(0,len(str)):
    ctr += str[len(str)-i-1]

print(ctr)
