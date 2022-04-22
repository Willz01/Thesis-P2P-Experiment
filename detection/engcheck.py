from langdetect import detect, detect_langs, DetectorFactory


# for same result on short or ambiguous text
from logger.log import log

DetectorFactory.seed = 0

"""
    Enforcing constraint on only allowing english messages
    Every other language is classified as spam during result visualization
"""


# top probability
def lang_probability(msg) -> None:
    # LP - Language probability
    # msg, LP, prediction[0], runTime
    result = detect_langs(msg)
    # print(result)
    log(msg, "LP", result, 0)


# get lang
def getlang(msg) -> None:
    # Get Lang - GL
    result = detect(msg)
    # print(result)
    log(msg, "GL", result, 0)


def both(msg) -> None:
    lang_probability(msg)
    getlang(msg)


print(getlang("chelsea"))
