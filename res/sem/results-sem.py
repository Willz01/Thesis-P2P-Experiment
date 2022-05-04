import pandas as pd
import matplotlib.pyplot as plt

cos_DF = pd.read_csv('sem_anl.csv', sep='\t')
print(cos_DF)
print(cos_DF.head())

# speed
"""
- mean speed
- avg runtime of method
- avg length of messages
"""
runtimes = cos_DF['runtime(ns)']
count = len(runtimes.values)
sum = runtimes.values.sum()
avg_runtime = sum / count
print("Semantic analysis AVG runtime: ", avg_runtime)
print(f'mean {runtimes.describe().mean()}')
print(f'median {runtimes.describe().median()}')
print(f'sd {runtimes.describe().std()}')

# success rate | false positive
score = cos_DF['score'].values
actual = cos_DF['actual'].values
c = 0
for i in range(score.size):
    if score[i] == actual[i]:
        c = c + 1


print(c)
print(score)
print(actual)

# faster to classify as spam OR ham
