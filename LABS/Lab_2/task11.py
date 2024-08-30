def add_grade(dic, grade, stu):
    dic[stu].append(grade)

def print_average(dic, stu):
    if stu in dic and dic[stu]:
        print("Average grade of", stu, ":", sum(dic[stu]) / len(dic[stu]))
    else:
        print(f"No grades available for {stu}.")

def add_new_stu(dic, stu):
    dic[stu] = []

def remove_stu(dic, stu):
    if stu in dic:
        dic.pop(stu)
    else:
        print(f"Student {stu} not found.")

def main():
    # Initialize an empty dictionary to store student grades
    students = {}

    # Hardcoded operations
    # Adding new students
    add_new_stu(students, "Alice")
    add_new_stu(students, "Bob")
    add_new_stu(students, "Charlie")
    
    # Adding grades
    add_grade(students, 85, "Alice")
    add_grade(students, 90, "Alice")
    add_grade(students, 78, "Bob")
    add_grade(students, 88, "Charlie")
    add_grade(students, 92, "Charlie")

    # Printing averages
    print_average(students, "Alice")   
    print_average(students, "Bob")    
    print_average(students, "Charlie") 
    
    # Removing a student
    remove_stu(students, "Bob")

    
    # Adding another student and grades
    add_new_stu(students, "David")
    add_grade(students, 95, "David")
    
    # Print averages for all students again
    print_average(students, "David")
    print_average(students, "Alice")
    print_average(students, "Charlie")

if __name__ == "__main__":
    main()
