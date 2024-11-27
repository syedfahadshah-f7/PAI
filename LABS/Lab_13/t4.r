# income <- as.numeric(readline(prompt = "Enter Income: "))
# print(income)
income = 40000

if (income < 30000) {
  print("No tax is applied")
} else if (income >= 30000 && income < 70000) {
  tax = income / 100 * 10
  income = income - tax  
} else if (income >= 70000 && income < 100000) {
  tax = income / 100 * 15
  income = income - tax  
} else {
  tax = income / 100 * 20
  income = income - tax 
}

print(paste("Income After Tax: ", income))
