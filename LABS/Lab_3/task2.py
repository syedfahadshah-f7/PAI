user = input("Enter any thing: ")

vow = ['a','e','i','o','u']
flag = False
for i in vow:
    if(user.endswith(i)):
        flag = True
        print("String ends with Vowels")
        break


if(flag != True):
    print("String ends with Constant")
