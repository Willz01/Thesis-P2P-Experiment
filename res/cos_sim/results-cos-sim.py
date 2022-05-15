import pandas as pd
import matplotlib.pyplot as plt

cos_sim_df = pd.read_csv('cos_sim.csv', sep='\t')
print(cos_sim_df)

# speed comparisons (graph) ?? TEST
speed = cos_sim_df['runtime(ns)']
cosine = cos_sim_df['score']

print(speed)
print(f'mean {speed.mean()}')
print(f'median {speed.median()}')
print(f'sd {speed.std()}')

print('------------------')


# score (mean, median) cosine similarity of distributed files descriptors

# speed (mean, avg) runtime to compute cos_sim

# cosine sim values ranges
def get_range(score):
    # if score <= .7:  # percentage of (score < .3) # not similar (Likely to be TYPE 1 spam)
    #     return '<=.7'
    if score <= .3:  # percentage of (score < .3) # not similar (Likely to be TYPE 1 spam)
        return '<=.3'
    elif 0.3 < score <= 0.5:  # percentage of (score < .5) (0.3 - .5)
        return '<=.5'
    elif 0.5 < score <= 0.8:  # percentage of (score > .5) (not likely to be spam TYPE 1) [.5 - .8]
        return "<=.8"
    else:  # [.8 - 1] not TYPE 1 spam
        return '>.8'


cos_sim_df['range'] = cos_sim_df['score'].apply(get_range)

scores = cos_sim_df['score']
runtimes = cos_sim_df['runtime(ns)']
print(scores)
print(f'Mean scores: {scores.mean()}')
print(runtimes)

# range[0 - 0.3, 0.3 - 0.5, 0.5 - 0.8 , 0.8 - 1.0]
range0_3 = cos_sim_df[cos_sim_df['range'] == '<=.3']
range3_5 = cos_sim_df[cos_sim_df['range'] == '<=.5']
range5_8 = cos_sim_df[cos_sim_df['range'] == '<=.8']
range8_1 = cos_sim_df[cos_sim_df['range'] == '>.8']
range0_7 = cos_sim_df[cos_sim_df['range'] == '<=.7']
# range7_1 = cos_sim_df[cos_sim_df['range'] == '>.7']
range0_7.to_csv('sets/0-7.csv', sep='\t')

print(range0_3)
c03 = range0_3['score']
s03 = range0_3['runtime(ns)']
plt.scatter(c03, s03, color='red')  # x: score, y:speed
print(range3_5)
c35 = range3_5['score']
s35 = range3_5['runtime(ns)']
plt.scatter(c35, s35, color='blue')  # x: score, y:speed
print(range5_8)
c58 = range5_8['score']
s58 = range5_8['runtime(ns)']
plt.scatter(c58, s58, color='green')  # x: score, y:speed
c81 = range8_1['score']
s81 = range8_1['runtime(ns)']
plt.scatter(c81,s81, color='yellow')

#
# # print(cos_sim_df.describe())
# # print(range8_1.describe())
# # print(range0_3.describe())
# range0_3.to_csv('sets/0-3.csv', sep='\t')
# range3_5.to_csv('sets/3_5.csv', sep='\t')
# range5_8.to_csv('sets/5_8.csv', sep='\t')
# range8_1.to_csv('sets/8_1.csv', sep='\t')

plt.ylabel('Speed(ns)')
plt.xlabel('Cosine values')
plt.show()

# print(range0_7)
# r71scores = range7_1['score']
# r71runtimes = range7_1['runtime(ns)']
# plt.scatter(r71scores, r71runtimes, color='blue')
# r7scores = range0_7['score']
# r7runtimes = range0_7['runtime(ns)']
# plt.scatter(r7scores, r7runtimes, color='red')
# plt.ylabel('Speed(ns)')
# plt.xlabel('Cosine values')
# print(r7runtimes)
# print(r7scores)
# plt.show()
