
list1 = input("Enter list 1 elements (space-separated): ").split(" ")
list2 = input("Enter list 2 elements (space-separated): ").split(" ")

dic = {}

if len(list1) == len(list2):

    for j in range(len(list1)):
        dic[list1[j]] = list2[j]

    for key, value in dic.items():
        print(f"Key: {key}, Value: {value}")
else:
    print("The lists have different lengths, unable to create a dictionary.")
