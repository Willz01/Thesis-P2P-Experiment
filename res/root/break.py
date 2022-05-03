import pandas as pd

df = pd.read_csv('log.csv')
print(df.head())

# Cosine Sim
cos_sim = df[df['method'] == 'C-SIM']
print(cos_sim)
cos_sim.to_csv('../cos_sim/cos_sim.csv', sep='\t', index=0)

# (Semantic Analysis)
sem_anl = df[df['method'] == 'SA']
print(sem_anl.head(10))
sem_anl.to_csv('../sem/sem_anl.csv', sep='\t', index=0)

# (English scoring)-(GL, LP)
eng_scoring = df[(df['method'] == 'GL') | (df['method'] == 'LP')]
print(eng_scoring.head(10))
eng_scoring.to_csv('../engscoring/eng_scoring.csv', sep='\t', index=0)
