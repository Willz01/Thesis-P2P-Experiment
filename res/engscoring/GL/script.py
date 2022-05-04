import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

GL_df = pd.read_csv('GL.csv', sep='\t')

#################################
GL_runtimes = GL_df['runtime(ns)']
GL_mean = GL_runtimes.mean()
GL_median = GL_runtimes.median()
GL_SD = GL_runtimes.describe().std()
print(GL_runtimes)
print(f'GL runtimes mean {GL_mean}')
print(f'GL runtimes median {GL_median}')
print(f'GL runtimes sd {GL_SD}')

print(GL_runtimes.describe())
avg_runtime = GL_runtimes.values.sum() / GL_runtimes.describe().count()
print(avg_runtime)

GL_msg_size = GL_df['message']


def getsize(values):
    sizeslist = []
    for msg in values:
        sizeslist.append(len(msg))
    return sizeslist


sizes = getsize(GL_msg_size.values)
runtimes = GL_runtimes.values

plt.scatter(sizes, runtimes, color='red')
plt.xlabel('GL runtimes(ns)')
plt.ylabel('GL msgs lengths')
plt.show()
