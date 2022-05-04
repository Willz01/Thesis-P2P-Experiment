import pandas as pd
import matplotlib.pyplot as plt

cos_sim_df = pd.read_csv('cos_sim.csv', sep='\t')
print(cos_sim_df)

# speed comparisons (graph) ?? TEST
speed = cos_sim_df['runtime(ns)']
cosine = cos_sim_df['score']
plt.figure(figsize=(15, 10))
plt.plot(cosine, speed, 'ro')  # x: score, y:speed
plt.ylabel('Speed(ns)')
plt.xlabel('Score')
plt.show()


# score (mean, median) cosine similarity of distributed files descriptors

# speed (mean, avg) runtime to compute cos_sim

# cosine sim values ranges
def get_range(score):
    if score <= .3:  # percentage of (score < .3) # not similar (Likely to be TYPE 1 spam)
        return '<=.3'
    elif 0.3 < score <= 0.5:  # percentage of (score < .5) (0.3 - .5)
        return '<=.5'
    elif 0.5 < score <= 0.8:  # percentage of (score > .5) (not likely to be spam TYPE 1) [.5 - .8]
        return "<=.8"
    else:  # [.8 - 1] not TYPE 1 spam
        return '>.8'


cos_sim_df['range'] = cos_sim_df['score'].apply(get_range)

print(cos_sim_df)
# range[0 - 0.3, 0.3 - 0.5, 0.5 - 0.8 , 0.8 - 1.0]
range0_3 = cos_sim_df[cos_sim_df['range'] == '<=.3']
range3_5 = cos_sim_df[cos_sim_df['range'] == '<=.5']
range5_8 = cos_sim_df[cos_sim_df['range'] == '<=.8']
range8_1 = cos_sim_df[cos_sim_df['range'] == '>8']

print(cos_sim_df.describe())
print(range8_1.describe())
print(range0_3.describe())
range0_3.to_csv('sets/0-3.csv', sep='\t')
range3_5.to_csv('sets/3_5.csv', sep='\t')
range5_8.to_csv('sets/5_8.csv', sep='\t')
range8_1.to_csv('sets/8_1.csv', sep='\t')



