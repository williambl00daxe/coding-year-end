#scorequiz
scorelist=[45,50,80,62,90,75,66,88,78,55,92]
passlist=0
faillist=0
numscores=0
sumscore=0
for score in scorelist:
    numscores=numscores+1
    sumscore=sumscore+score
    if score <70:
        faillist=faillist+1
    else:
        passlist=passlist+1

avgscore=sumscore/numscores
print('number passed',passlist)
print('number failed',faillist)
print('average score',avgscore)



