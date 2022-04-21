from langdetect import detect, detect_langs, DetectorFactory

# for same result on short or ambiguous text
DetectorFactory.seed = 0
print(detect_langs("jag kommer"))


# top probability
def lang_probability(msg) -> str:
    return detect_langs(msg)


# get lang
def getlang(msg) -> str:
    return detect(msg)


print(getlang("chelsea"))
