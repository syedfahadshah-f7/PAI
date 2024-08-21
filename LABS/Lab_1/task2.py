n1 = int(input("Enter Value 1: "))
n2 = int(input("Enter Value 2: "))

ope = input("Enter Operaton: ")

match ope:
    case '+':
        print(f"Ans is {n1+n2}")
    case '-':
        print(f"Ans is {n1 - n2}")
    case '*':
        print(f"Ans is {n1 * n2}")
    case '/':
        print(f"Ans is {n1 + n2}")
    case _:
        print("Invalid Operation ")

