import random

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
import similarity
import time

# https://pypi.org/project/strsim/
from log import log

"""
    Get random file name to simulate false descriptor text
"""


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


"""
    f_name : split request command read from node and get requested file name
    index_f_name : random file name gotten from save descriptors text
    Compute and print, and return computed Similarity.
"""


def compute_sim(read_msg):
    f_name = read_msg.split(" ")[1]  # get name ('request , ...txt')
    index_f_name = get_index()  # get random file name index
    s0 = index_f_name
    s1 = f_name
    start = time.time_ns() // 1_000_000
    cos_sim = similarity.get_similarity(s0, s1)
    runTime = (time.time_ns() // 1_000_000) - start
    print(s0, s1, cos_sim)
    log(f'${s1}=?${s0}', "C-SIM", cos_sim, runTime)


compute_sim("request drake.txt")
