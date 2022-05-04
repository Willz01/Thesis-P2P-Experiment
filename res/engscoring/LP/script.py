import pandas as pd
import matplotlib.pyplot as plt

LP_df = pd.read_csv('LP.csv', sep='\t')

LP_runtimes = LP_df['runtime(ns)']
LP_mean = LP_runtimes.mean()
LP_median = LP_runtimes.median()
LP_SD = LP_runtimes.describe().std()
print(LP_runtimes)
print(f'LP_ runtimes mean {LP_mean}')
print(f'LP_ runtimes median {LP_median}')
print(f'LP_ runtimes sd {LP_SD}')

print(LP_runtimes.describe())
avg_runtime = LP_runtimes.values.sum() / LP_runtimes.describe().count()
print(avg_runtime)

LP_msg_size = LP_df['message']


def getsize(values):
    sizeslist = []
    for msg in values:
        sizeslist.append(len(msg))
    return sizeslist


sizes = getsize(LP_msg_size.values)
runtimes = LP_runtimes.values

plt.scatter(sizes, runtimes, color='blue')
plt.xlabel('LP runtimes(ns)')
plt.ylabel('LP msgs lengths')
plt.show()
