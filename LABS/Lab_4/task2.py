list1 = ["Hello ", "take "] 
list2 = ["Dear", "Sir"]


#Approach 1
#list3 = []

# for ind1,val1 in enumerate(list1):
#     for ind2,val2 in enumerate(list2):
#         list3.append(val1+val2)

# print(list3)

#Approach 2

list3 = [x+y for x in list1 for y in list2]
print(list3)
