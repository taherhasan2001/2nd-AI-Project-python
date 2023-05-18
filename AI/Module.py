import joblib
import regex



LSPosEmoji = "😂🌹😍🌸🤣💪🙏🙂🌝😎✨😊✅🌷😁👌👋😀😃😄😁😆😅☺😇🙃😉😌🥰🎊😘😗😙🎁😚😋😎🎵😅🤩🥳❀🌻😻❁🌟✌🎶😺💐🥴🤗👍😜🌺💫"
Love = "❤️🧡💛💚💙💜🖤🤍🤎❤️‍🔥❤️‍🩹❣️💕💞💓💗💖💘💝❥♡ﷺ"
NegEmoji = "😒😞😔😟😕🙁☹️😣😖😫😩😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤔🌚🙈🥀⛔😴🍯😑😐😈👿👹👺🤡💩👻💀☠"
#____________________________________________________________________________________
lsDoaa = []
lsPosAG = []
lsAngAS = []
lsNegAB = []

f1 = open(r"AI\Doaa.txt","r",encoding="utf-8")
f2 = open(r"AI\PosGood.txt","r",encoding="utf-8")
f3 = open(r"AI\AngASwer.txt","r",encoding="utf-8")
f4 = open(r"AI\NegABad.txt","r",encoding="utf-8")
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

def PrePro(x,e1,e2,e3,ls1,ls2,ls3,ls4):
    lstemp = []
    lstemp.append(FerEmo(e1,e2,e3,x))
    lstemp.append(FerDoaa(ls1,x))
    lstemp.append(FerPosG(ls2, x))
    lstemp.append(FerAngSwr(ls3, x))
    lstemp.append(FerNegBad(ls4, x))
    return lstemp

with open(r'AI\DTree.joblib', 'rb') as f:
    DtreeMOd = joblib.load(f)
with open(r'AI\Naive.joblib', 'rb') as f:
    NaiveMOd = joblib.load(f)
with open(r'AI\NuNet.joblib', 'rb') as f:
    NutNetMOd = joblib.load(f)


#MakeDataSet(alf,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB,DataSet)

#s2 ="الدودو جايه تكمل علي 💔"
#lstest = PrePro(s2,LSPosEmoji,Love,NegEmoji,lsDoaa,lsPosAG,lsAngAS,lsNegAB)
#print(DtreeMOd.predict([lstest]))
#print(NaiveMOd.predict([lstest]))
#print(NutNetMOd.predict([lstest]))