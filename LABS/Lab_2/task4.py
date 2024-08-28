def employee(name, salary = 10000):
    print(f"Name: {name}, Salary {salary - ((salary/100)*2)}")


employee("Fahad")