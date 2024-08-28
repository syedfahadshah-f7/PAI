from statistics import mean 
temp = [20,21,22,23,24,25,26,27,28,29,30,11,12,13,14,15,16,17,18,19,1,2,3,4,5,6,7,8,9,10]

print(f"Average: {mean(temp)}")
print(f"Highest: {max(temp)}, Lowest: {min(temp)} ")
temp.sort()
print(f"Sorted Temperature: {temp}")

day = int (input("Enter day number to remove temp: "))
temp.remove(temp[day-1])
print(f"After removing day {day} Temperature: {temp}")
