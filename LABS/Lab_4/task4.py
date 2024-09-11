class Employee:
    def get_data(self):
        self.employee_name  = input("Enter Employee Name: ")
        self.monthly_salary = float(input("Enter Employee Monthly Salary: "))
        self.percentage_tax =  float(input("Enter Tax Percentage: "))
        
    def Salary_after_tax(self):
        return self.monthly_salary - (self.percentage_tax/100*self.monthly_salary)
    
    def update_tax_percentage(self, update):
        self.percentage_tax = update
        
        
E1 = Employee()
E1.get_data()
print("Salary After Tax: ", E1.Salary_after_tax())  
E1.update_tax_percentage(3)     
print("Updated Salary After Tax: ", E1.Salary_after_tax())