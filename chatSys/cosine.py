import random

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
import similarity


# https://pypi.org/project/strsim/


def get_index() -> str:
    index = random.randint(1, 10)
    with open("descriptors.txt", "r") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1
            if index == count:
                print(line)
                return line.strip()


def compute_sim(read_msg):
    f_name = read_msg.split(" ")[1]  # get name ('request , ...txt')
    index_f_name = get_index()  # get random file name index
    s0 = index_f_name
    s1 = f_name
    print(s0, s1, similarity.get_similarity(s0, s1))


compute_sim("request drake.txt")
