import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score

cos_DF = pd.read_csv('sem_anl.csv', sep='\t')
# print(cos_DF)
# print(cos_DF.head())

# speed
"""
- mean speed
- avg runtime of method
- avg length of messages
"""
runtimes = cos_DF['runtime(ns)']
print('values')
print(f'mean {runtimes.mean()}')
print(f'median {runtimes.median()}')
print(f'sd {runtimes.std()}')

# success rate | false positive
score = cos_DF['score'].values
actual = cos_DF['actual'].values
print(score.size)
print(actual.size)
accuracy = accuracy_score(actual, score)
results = confusion_matrix(actual, score)
print(results)
print("accuracy: ", accuracy)
c_ham = 0
c_spam = 0
x = 0
for i in range(score.size):
    if score[i] == 'ham':
        if score[i] == actual[i]:
            c_ham = c_ham + 1
        else:
            x = x + 1
    elif score[i] == 'spam':
        if score[i] == actual[i]:
            c_spam = c_spam + 1

print(c_ham)
print(c_spam)
print(x)
print(score)
print(actual)

# faster to classify as spam OR ham
