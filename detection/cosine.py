import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances

A = np.array([10, 3])
B = np.array([8, 7])
result = cosine_similarity(A.reshape(1, -1), B.reshape(1, -1))
print(result)
