import random

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances

A = np.array([10, 3])
B = np.array([8, 7])
result = cosine_similarity(A.reshape(1, -1), B.reshape(1, -1))


# print(result)

def get_index(read_msg) -> str:
    fname = read_msg.split(" ")[1]
    index = random.randint(1, 10)
    with open("descriptors.txt", "r") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1
            if index == count:
                print(line)
                return line.strip()
