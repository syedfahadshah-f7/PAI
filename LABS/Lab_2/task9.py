file = open("Lab_2/temp.txt", "r")
word =0

for f in file:
    word += len(f)
    
print(f"Total characters: {word}")