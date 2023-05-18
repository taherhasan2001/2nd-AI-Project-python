import nltk
from nltk.stem.isri import ISRIStemmer
import pandas as pd
import regex
pd.options.display.max_rows = 99999
st = ISRIStemmer()
#17300
lstest = []
def test(stt,ls):
    too = nltk.tokenize.sent_tokenize(stt)
    for x in range(len(too)):
        too[x] = st.suf32(too[x])
        ls.append(too[x])

df = pd.read_csv("Negative+Tweets.tsv",sep="  ",nrows=17300,encoding='utf-8',engine='python')
alf = df.to_string().split("\n")
for x in alf:
    test(x,lstest)
fd = nltk.FreqDist(lstest)
for x in fd.most_common(150):
    print(x)

