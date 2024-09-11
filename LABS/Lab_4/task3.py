class Student:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        
    def Print_biodata(self):
        print(f"Name : {self.name} \t Age : {self.age}")
        
st1 =Student("fahad", 19)
st2 =Student("Umar", 20)
st3 =Student("AR", 19)

st1.Print_biodata()
st2.Print_biodata()
st3.Print_biodata()





