import time

from langdetect import detect, detect_langs, DetectorFactory


# for same result on short or ambiguous text
from log import log

DetectorFactory.seed = 0

"""
    Enforcing constraint on only allowing english messages
    Every other language is classified as spam during result visualization
"""


# top probability
def lang_probability(msg) -> None:
    # LP - Language probability
    # msg, LP, prediction[0], runTime
    start = time.time_ns() / 1_000_000
    result = detect_langs(msg)
    runTime = (time.time_ns() / 1_000_000) - start
    # print(result)
    log(msg, "LP", result, runTime)


# get lang
def getlang(msg) -> None:
    # Get Lang - GL
    start = time.time_ns() / 1_000_000
    result = detect(msg)
    runTime = (time.time_ns() / 1_000_000) - start
    # print(result)
    log(msg, "GL", result, runTime)


def score_lang(msg) -> None:
    lang_probability(msg)
    getlang(msg)
