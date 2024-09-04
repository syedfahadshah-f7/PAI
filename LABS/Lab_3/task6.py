Sentence = input("Enter a Sentence: ")
try:
    if Sentence[len(Sentence) - 1] == '?':
        f = open("question.txt", 'w')
        f.write(Sentence)
    else:
        print("Sentence is not a question")

except Exception as e:
    print("Error : " + str(e))
