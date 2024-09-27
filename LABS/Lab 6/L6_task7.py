import pandas as pd

df = pd.read_excel("employee.xlsx")
specified_year = 2019
print(df[df['YearOfJoining'] > specified_year])
