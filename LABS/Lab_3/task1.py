import math


def trapezoid():
    print("Enter Trapezoid Values: \n")
    a = int(input("Enter Val 1: "))
    b = int(input("Enter Val 2: "))
    h = int(input("Enter Height: "))

    return (a+b)/2 * h


def parallelogram():
    print("Enter parallelogram Values: \n")
    b = int(input("Enter Base: "))
    h = int(input("Enter Height: "))

    return b*h


def areaofcyinder():
    print("Enter areaofcyinder Values: \n")
    r = int(input("Enter Radius: "))
    h = int(input("Enter Height: "))

    return (2* math.pi*h*r) + (2* math.pi*r*r)


def volumecfcyinder():
    print("Enter volumecfcyinderValues: \n")
    r = int(input("Enter Radius: "))
    h = int(input("Enter Height: "))

    return 2* math.pi*h*r


print(f"Area of Parallelogram: {parallelogram()}")
print(f"Area of Parallelogram: {trapezoid()}")
print(f"Area of Parallelogram: {volumecfcyinder()}")
print(f"Area of Parallelogram: {areaofcyinder()}")
