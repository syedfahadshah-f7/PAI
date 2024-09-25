import pandas as pd


movies = ["FAF 1", "FAF 2", "FAF 3", "FAF 4", "FAF 5"]
revenue = [2000000, 1000000, 4000000, 7000000, 8000000]
spent = [2000000, 600000, 4000000, 300000, 350000]

df = pd.DataFrame({
    'Movies': movies,
    'Revenue': revenue,
    'Spent': spent
})

print(df[(df['Revenue']>2000000) & (df['Spent']<1000000)])
