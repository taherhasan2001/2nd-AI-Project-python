import joblib
import regex
import pandas as pd
#import csv
from sklearn import tree
from sklearn import naive_bayes
from sklearn.tree import DecisionTreeClassifier
from sklearn import neural_network
pd.options.display.max_rows = 99999






LSPosEmoji = "😂🌹😍🌸🤣💪🙏🙂🌝😎✨😊✅🌷😁👌👋😀😃😄😁😆😅☺😇🙃😉😌🥰🎊😘😗😙🎁😚😋😎🎵😅🤩🥳❀🌻😻❁🌟✌🎶😺💐🥴🤗👍😜🌺💫"
Love = "❤️🧡💛💚💙💜🖤🤍🤎❤️‍🔥❤️‍🩹❣️💕💞💓💗💖💘💝❥♡ﷺ"
NegEmoji = "😒😞😔😟😕🙁☹️😣😖😫😩😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤔🌚🙈🥀⛔😴🍯😑😐😈👿👹👺🤡💩👻💀☠"
#____________________________________________________________________________________
lsDoaa = []
lsPosAG = []
lsAngAS = []
lsNegAB = []

f1 = open("Doaa.txt","r",encoding="utf-8")
f2 = open("PosGood.txt","r",encoding="utf-8")
f3 = open("AngASwer.txt","r",encoding="utf-8")
f4 = open("NegABad.txt","r",encoding="utf-8")
for x in f1:
    x = x.replace("\n","")
    lsDoaa.append(x)
for x in f2:
    x = x.replace("\n", "")
    lsPosAG.append(x)
for x in f3:
    x = x.replace("\n", "")
    lsAngAS.append(x)
for x in f4:
    x = x.replace("\n", "")
    lsNegAB.append(x)




















def FerEmo(sp,slo,sne,sam):
    emoji = regex.findall(r'[^\w\⁠s,. ]', sam)
    if(len(emoji) == 0):
        return 0
    else:
        coup = 0
        coune = 0
        for x in emoji:
            if(x == "💔"):
                coune += 30
            elif(x in slo):
                coup += 10
            elif(x in sp):
                coup += 8
            elif(x in sne):
                coune += 8
        if(coup > coune):
            return 1
        elif(coune > coup):
            return -1
        else:
            return 0

def FerDoaa(ls,sam):
    for x in ls:
        if(x in sam):
            return 1
    return 0

def FerPosG(ls,sam):
    for x in ls:
        if(x in sam):
            return 1
    return 0

def FerAngSwr(ls,sam):
    for x in ls:
        if(x in sam):
            return 1
    return 0

def FerNegBad(ls,sam):
    for x in ls:
        if(x in sam):
            return 1
    return 0


df = pd.read_csv("Positive+Tweets.tsv",sep="  ",nrows=17070,encoding='utf-8',engine='python')
alf = df.to_string().split("\n")
df2 = pd.read_csv("Negative+Tweets.tsv",sep="  ",nrows=17400,encoding='utf-8',engine='python')
alf2 = df2.to_string().split("\n")


Feturse = ["Emoji","HeyAndPrey","PosAndGood","AngryAndSewer","NegAndBad","State"]
Feturse2 = ["Emoji","HeyAndPrey","PosAndGood","AngryAndSewer","NegAndBad"]

DataSet = []

def MakeDataSet(sampls,e1,e2,e3,ls1,ls2,ls3,ls4,data):
    for x in sampls:
        lstemp = []
        lstemp.append(FerEmo(e1,e2,e3,x))
        lstemp.append(FerDoaa(ls1,x))
        lstemp.append(FerPosG(ls2, x))
        lstemp.append(FerAngSwr(ls3, x))
        lstemp.append(FerNegBad(ls4, x))
        lstemp.append(1)
        data.append(lstemp)

MakeDataSet(alf,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,DataSet)

def MakeDataSet2(sampls,e1,e2,e3,ls1,ls2,ls3,ls4,data):
    for x in sampls:
        lstemp = []
        lstemp.append(FerEmo(e1,e2,e3,x))
        lstemp.append(FerDoaa(ls1,x))
        lstemp.append(FerPosG(ls2, x))
        lstemp.append(FerAngSwr(ls3, x))
        lstemp.append(FerNegBad(ls4, x))
        lstemp.append(0)
        data.append(lstemp)

MakeDataSet2(alf2,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,DataSet)

#with open("DataSet.csv","w",encoding="UTF8",newline="")as fl:
    #wr = csv.writer(fl)
    #wr.writerows(DataSet)


df3 = pd.read_csv("DataSet.csv",names=Feturse,header=None)
X = df3[Feturse2]
y = df3["State"]
Dtree = DecisionTreeClassifier()
Dtree = Dtree.fit(X.values, y.values)
Naive = naive_bayes.GaussianNB()
Naive = Naive.fit(X.values, y.values)
NuNet = neural_network.MLPClassifier(solver='lbfgs', alpha=0.2,hidden_layer_sizes=(2, 5), random_state=1)
NuNet = NuNet.fit(X.values,y.values)


def Predction(sampls,e1,e2,e3,ls1,ls2,ls3,ls4,D):
    c1 = 0
    c2 = 0
    for x in sampls:
        lstemp = []
        lstemp.append(FerEmo(e1,e2,e3,x))
        lstemp.append(FerDoaa(ls1,x))
        lstemp.append(FerPosG(ls2, x))
        lstemp.append(FerAngSwr(ls3, x))
        lstemp.append(FerNegBad(ls4, x))
        #print(lstemp)
        an = D.predict([lstemp])
        if(an == 1):
            c1 += 1
        else:
            c2 += 1
    print(c1)
    print(c2)
    sum = c1 + c2
    perspos = (c1/sum) * 100.0
    preneg = (c2/sum) * 100.0
    print(perspos,"% Pos")
    print(preneg, "% Neg")


print("for Neg File")
df4 = pd.read_csv("Negative+Tweets.tsv",sep="  ",skiprows=17400,encoding='utf-8',engine='python')
alf3 = df4.to_string().split("\n")
Predction(alf3,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,Dtree)
Predction(alf3,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,Naive)
Predction(alf3,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,NuNet)
print("------------------------------------------------------------------------------------------------")
print("for Pos File")
df5 = pd.read_csv("Positive+Tweets.tsv",sep="  ",skiprows=17400,encoding='utf-8',engine='python')
alf4 = df5.to_string().split("\n")
Predction(alf4,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,Dtree)
Predction(alf4,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,Naive)
Predction(alf4,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,NuNet)





#with open('Naive.joblib', 'wb') as f:
 #   joblib.dump(Naive,f)
#with open('NuNet.joblib', 'wb') as f:
 #   joblib.dump(NuNet,f)