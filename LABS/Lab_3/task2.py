try:
     f = open("temp.txt")
     Content = f.read()
     f.close()
     f = open("temp.txt","w")
     newContent = Content.replace("Muhammad", "Syed")
     f.write(newContent)
     f.close()

except Exception as e:
    print("Error : " + str(e))
