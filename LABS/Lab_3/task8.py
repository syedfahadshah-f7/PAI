try:
    a = int(input("Enter two numbers for division : "))
    b  = int(input())
    print(f"Ans: {a/b}")
except ZeroDivisionError:
    print("Number can't be divide by Zero!!")
except ValueError:
    print("Enter Value is not Int")