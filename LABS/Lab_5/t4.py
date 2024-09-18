class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def Display_info(self):
        print(f"Name : {self.name}  ID : {self.id}")


class Marks(Student):

    def __init__(self, name, id) -> None:
        super().__init__(name, id)
        self.marks_algo = float(input("Enter Algo Marks : "))
        self.marks_dataScience = float(input("Enter Data Science Marks : "))
        self.marks_calculus = float(input("Enter Calculus Marks : "))

    def Display_info(self):
        super().Display_info()
        print(
            f" Algo Marks : {self.marks_algo} Data Science Marks : {self.marks_dataScience} Calculus Marks : {self.marks_calculus}")


class Result(Marks):

    def __init__(self, name, id) -> None:
        super().__init__(name, id)

    def calculate(self):
        self.Total = self.marks_algo + self.marks_calculus + self.marks_dataScience
        self.average = self.Total / 3

    def Display_info(self):
        super().Display_info()
        print(f"Total marks : {self.Total}/300 Average : {self.average}")


St1 = Result("fahad", "23k-0062")
St1.calculate()
St1.Display_info()