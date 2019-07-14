from collections import Counter
from itertools import permutations
import sys
#taking input from user
arr = input().split(',')
permu = permutations(arr,2)
possible = [x[0]+x[1] for x in permu]
possible = dict.fromkeys(possible,1)
month =[];day=[];hour=[];minute=[]

#storing all possible value of month
for i in range(12,0,-1):
    val = "{:02d}".format(i)
    if val in possible:
        month.append(val)

#storing all possible value of day
for i in range(31,0,-1):
    val = "{:02d}".format(i)
    if val in possible:
        day.append(val)

#storing all possible value of hour
for i in range(23,-1,-1):
    val =  "{:02d}".format(i)
    if val in possible:
        hour.append(val)

#storing all possible val of minute
for i in range(59,-1,-1):
    val = "{:02d}".format(i)
    if val in possible:
        minute.append(val)


if len(month)==0 or len(day)==0 or len(hour)==0 or len(minute)==0:
    print(0)
    sys.exit()

res=[]
temp = Counter(arr)
flag=False
for m in month:
    res.append(m)
    temp[m[0]] -= 1
    temp[m[1]] -= 1
    for d in day:
        if (temp[d[0]]<=0) or (temp[d[1]]<=0):
                continue
        res.append(d)
        temp[d[0]] -=1
        temp[d[1]] -=1
        for h in hour:
            if (temp[h[0]]<=0) or (temp[h[1]]<=0):
                continue
            res.append(h)
            temp[h[0]] -= 1
            temp[h[1]] -= 1
            for mi in minute:
                if (temp[mi[0]]<=0) or (temp[mi[1]]<=0):
                    continue
                res.append(mi)
                temp[mi[0]] -= 1
                temp[mi[1]] -= 1
                flag=True
                break

            #maximum time find
            if flag: break
            #time not find
            #backtrack from hour
            res.pop()
            temp[h[0]] =+ 1
            temp[h[1]] =+ 1
        #maximum time find
        if flag: break
        #time not find
        #backtrack from day
        res.pop()
        temp[d[0]] =+ 1
        temp[d[1]] =+ 1

    #maximum time find
    if flag: break
    #time not find
    #backtrack from month
    res.pop()
    temp[m[0]] =+ 1
    temp[m[1]] =+ 1

if flag:
    print(res[0],'/',res[1],' ',res[2],':',res[3],sep='')
else:
    print(0)

