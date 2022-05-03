import pandas as pd
import matplotlib.pyplot as plt

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Wills', 'Ben'])
print(purchases)
print(purchases.loc['Wills'])

print("*******************")

# read data from CSV
df = pd.read_csv('log.csv')
print(df.head())
print("*******************")
print(df.info())

print(df.shape)
print("*******************")

runtimes = df['runtime(ns)']  # creating variable from a column(series)
print(runtimes)
print(runtimes.mean())
print(df['score'].describe())

# filter out based on method type (cosine sim)
cos_sim = df[df['method'] == 'C-SIM']

speed = cos_sim['runtime(ns)'].head(20)
score = cos_sim['score'].head(20)
plt.figure(figsize=(15, 10))
plt.plot(score, speed, 'ro')
plt.ylabel('Speed(ns)')
plt.xlabel('Score')
plt.show()

print(cos_sim)
cos_sim.to_csv('cos_sim.csv', sep='\t', index=0)

# (Semantic Analysis)
sem_anl = df[df['method'] == 'SA']
print(sem_anl.head(10))
sem_anl.to_csv('sem_anl.csv', sep='\t', index=0)

# (English scoring)-(GL, LP)
eng_scoring = df[(df['method'] == 'GL') | (df['method'] == 'LP')]
print(eng_scoring.head(10))
eng_scoring.to_csv('eng_scoring.csv', sep='\t', index=0)
