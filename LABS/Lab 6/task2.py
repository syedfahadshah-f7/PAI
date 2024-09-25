data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 40, 20, 50, 30],
    'C': [100, 200, 300, 500, 400]
}
df = pd.DataFrame(data)
df.sort_values(by='B',ascending=False)
