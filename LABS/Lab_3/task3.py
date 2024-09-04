
list1 = input("Enter list 1 elements (space-separated): ").split(" ")
list2 = input("Enter list 2 elements (space-separated): ").split(" ")

dic = {}
try:
    if len(list1) == len(list2):

        for j in range(len(list1)):
            dic[list1[j]] = list2[j]

        f = open("temp3.txt",'w')
        f.write(str(dic))
        f.close()
    else:
        print("The lists have different lengths, unable to create a dictionary.")
except Exception as e:
    print("Error : " + str(e))
