import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

eng_score_df = pd.read_csv('eng_scoring.csv', sep='\t')
print(eng_score_df)

GL_df = eng_score_df[eng_score_df['method'] == 'GL']
print(GL_df.head())
print(GL_df.describe())
print(GL_df.info)

LP_df = eng_score_df[eng_score_df['method'] == 'LP']
print(LP_df.head())
print(LP_df.describe())
print(LP_df.info)

GL_df.to_csv('GL/GL.csv', sep='\t')
LP_df.to_csv('LP/LP.csv', sep='\t')

#################################
GL_runtimes = GL_df['runtime(ns)']
GL_mean = GL_runtimes.mean()
GL_median = GL_runtimes.median()
GL_SD = GL_runtimes.std()
# print(GL_runtimes)
print(f'GL runtimes mean {GL_mean}')
print(f'GL runtimes median {GL_median}')
print(f'GL runtimes sd {GL_SD}')
sum = GL_df['runtime(ns)'].values.sum()
count = len(GL_df['runtime(ns)'].values)
print(f'{sum} {count}')
avg = sum / count
print(f'AVG runtime GL {avg}')

#################################
LP_runtimes = LP_df['runtime(ns)']
LP_mean = LP_runtimes.mean()
LP_median = LP_runtimes.median()
LP_SD = LP_runtimes.describe().std()
# print(LP_runtimes)
print(f'LP_ runtimes mean {LP_mean}')
print(f'LP_ runtimes median {LP_median}')
print(f'LP_ runtimes sd {LP_SD}')
sum = LP_df['runtime(ns)'].values.sum()
count = len(LP_df['runtime(ns)'].values)
print(f'{sum} {count}')
avg = sum / count
print(f'AVG runtime LP {avg}')
"""
    LP - Lang prop runtime wise is perform slower than GL. LP takes more time to 
    identify spam messages because of it comparably high runtime avg.
"""
# GL and LP runtimes
LP_runtime_values = LP_runtimes.values
GL_runtime_values = GL_runtimes.values
print(LP_runtime_values)
print(LP_runtime_values.size)
print(GL_runtime_values.size)

print('ggg')
# LP scores
lp_scores = LP_df['score']
print(lp_scores)

# GL scores
gl_scores = GL_df['score']
gl_values = gl_scores.values
wordcloud = WordCloud().generate(' '.join(gl_values))

plt.imshow(wordcloud)
plt.axis("on")
plt.show()
print(gl_scores)

#########################
GL_msg_size = GL_df['message']
LP_msg_size = LP_df['message']


def getsize(values):
    sizeslist = []
    for msg in values:
        sizeslist.append(len(msg))
    return sizeslist


#####################
GL_sizes = getsize(GL_msg_size)
LP_sizes = getsize(LP_msg_size)
runtimes_gl = GL_runtimes.values
runtimes_lp = LP_runtimes.values
print(GL_sizes)
print(runtimes_gl)

print(LP_sizes)
print(runtimes_lp)

plt.scatter(runtimes_gl, GL_sizes, color='red')
plt.xlabel('Runtimes(ns)')
plt.ylabel('Msg length')
plt.title('GL')
plt.show()

plt.scatter(runtimes_lp, LP_sizes, color='blue')
plt.xlabel('Runtimes(ns)')
plt.ylabel('Msg length')
plt.title('LP')
plt.show()

# scatter
# GL
plt.scatter(runtimes_gl, GL_sizes, color='red', label='GL')

# LP
plt.scatter(runtimes_lp, LP_sizes, color='blue', label='LP')
plt.xlabel('Runtimes(ns)')
plt.ylabel('Message lengths')
plt.legend()
plt.title('GL and LP')

plt.show()

plt.boxplot(runtimes_lp)
plt.boxplot(runtimes_gl)
plt.show()

scores = eng_score_df['score']
total_size = scores.values.size
print(total_size)
print(scores)


def get_count(scs, t):
    c = 0
    for s in scs:
        if s == 'en':
            c = c + 1
        elif 'en' in s:
            c = c + 1
            pass
        else:  # other langs
            print(s)
            pass
    print(((c / t) * 100))


get_count(scores, total_size)
