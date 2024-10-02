import pandas as pd
df = pd.read_csv("heart.csv")
# print(df)
df.rename(columns =  {'sex' : 'gender'}, inplace = True)
df['gender'] = df['gender'].replace( {0: 'Female' , 1 :'Male'})
grouped = df.groupby('gender')
print(grouped['chol'].mean())

