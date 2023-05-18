
import nltk
from nltk.stem.isri import ISRIStemmer
import pandas as pd
pd.options.display.max_rows = 99999
st = ISRIStemmer()
#17070
lstest = []
def test(stt,ls):
    too = nltk.tokenize.word_tokenize(stt)
    for x in range(len(too)):
        too[x] = st.suf32(too[x])
        ls.append(too[x])


df = pd.read_csv("Positive+Tweets.tsv",sep="  ",nrows=17070,encoding='utf-8',engine='python')
alf = df.to_string().split("\n")
for x in alf:
    test(x,lstest)

fd = nltk.FreqDist(lstest)
for x in fd.most_common(150):
    print(x)

