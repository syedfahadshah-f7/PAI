import pandas as pd

# Reading the CSV file
df = pd.read_csv("sample_who_data.csv")


df.set_index('Year', inplace=True)

print("1987 \n",df.loc[1987])
print("1989 \n",df.loc[1989])
