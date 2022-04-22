import time

import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import confusion_matrix

# https://towardsdatascience.com/spam-or-ham-introduction-to-natural-language-processing-part-2-a0093185aebd
from logger.log import log

data = pd.read_csv("../../spam.csv", encoding="latin-1")
data = data[['v1', 'v2']]
data = data.rename(columns={'v1': 'label', 'v2': 'text'})

lemmatizer = WordNetLemmatizer()
# problem downloading nltk stopwords
english_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
                     "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
                     'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
                     "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
                     'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
                     'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
                     'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
                     'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
                     'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
                     'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
                     'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
                     'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
                     'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now',
                     'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
                     'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
                     "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn',
                     "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
                     'won', "won't", 'wouldn', "wouldn't"]
stopwords = set(english_stopwords)


def review_messages(msg):
    # converting messages to lowercase
    msg = msg.lower()
    return msg


def alternative_review_messages(msg):
    # converting messages to lowercase
    msg = msg.lower()

    # uses a lemmatizer (wnpos is the parts of speech tag)
    # unfortunately wordnet and nltk uses a different set of terminology for pos tags
    # first, we must translate the nltk pos to wordnet
    nltk_pos = [tag[1] for tag in pos_tag(word_tokenize(msg))]
    msg = [tag[0] for tag in pos_tag(word_tokenize(msg))]
    wnpos = ['a' if tag[0] == 'J' else tag[0].lower() if tag[0] in ['N', 'R', 'V'] else 'n' for tag in nltk_pos]
    msg = " ".join([lemmatizer.lemmatize(word, wnpos[i]) for i, word in enumerate(msg)])

    # removing stopwords
    msg = [word for word in msg.split() if word not in stopwords]

    return msg


# Processing text messages
data['text'] = data['text'].apply(review_messages)

# train test split
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.1, random_state=1)

# training vectorizer
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)

# training the classifier
svm = svm.SVC(C=1000)  # why
svm.fit(X_train, y_train)

# testing against testing set
X_test = vectorizer.transform(X_test)
y_pred = svm.predict(X_test)
print(confusion_matrix(y_test, y_pred))


# test against new messages
def pred(msg):
    plainText = msg
    start = time.time_ns() // 1_000_000
    print(start)
    msg = vectorizer.transform([msg])
    prediction = svm.predict(msg)

    end = time.time_ns() // 1_000_000
    print(end)
    runTime = end - start
    # SA - Semantic analysis
    # msg, semantic analysis, prediction[0], runTime
    log(plainText, "SA", prediction[0], runTime)
    return prediction[0]


# Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
print(pred(
    "Hey guys!"))
