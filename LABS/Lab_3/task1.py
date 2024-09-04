
try:
     file = open("temp.txt")
     content = file.read()
     cnt = 0
     for i in content:
        cnt += 1
     print(f"Word Count: {cnt}")
     file.close()

except Exception as e:
    print("Error : " + str(e))

