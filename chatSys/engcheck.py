import time

import langdetect
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
    try:
        start = time.time_ns() / 1_000_000
        result = detect_langs(msg)
        runTime = (time.time_ns() / 1_000_000) - start
    except langdetect.LangDetectException:
        result = "error"
        runTime = 0
    # print(result)
    log(msg, "LP", result, runTime)


# get lang
def getlang(msg) -> None:
    # Get Lang - GL
    try:
        start = time.time_ns() / 1_000_000
        result = detect(msg)
        runTime = (time.time_ns() / 1_000_000) - start
    except langdetect.LangDetectException:
        result = "error"
        runTime = 0
    # print(result)
    log(msg, "GL", result, runTime)


def score_lang(msg) -> None:
    lang_probability(msg)
    getlang(msg)
