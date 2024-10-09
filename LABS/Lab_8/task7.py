import numpy as np
arr = np.random.rand(1000)
average = np.mean(arr)
variance = np.var(arr)
std_deviation = np.std(arr)

filename = "stats_file.txt"
with open(filename, 'w') as file:
    file.write(f"Average: {average}\n")
    file.write(f"Variance: {variance}\n")
    file.write(f"Standard Deviation: {std_deviation}\n")
