#not solved yet
from collections import Counter
from itertools import combinations
def check(x,f):
    p1,p2,p3,p4 = x
    l=[[p1//f,p1%f],[p2//f,p2%f],[p3//f,p3%f],[p4//f,p4%f]]
    res=[]
    for i in range(3):
        for j in range(i+1,4):
            x1 = l[i][0]
            y1 = l[i][1]
            x2 = l[j][0]
            y2 = l[j][1]
            midx = abs(x1+x2)/2 
            midy= abs(y1+y2)/2
            val = [midx,midy] 
            if val not in res:
                res.append([midx,midy])
            else:
                print(x,res,val)
                return True
    # counter = Counter(res)
    # for x in counter.values():
    #     if x>1:
    #         return True
    # if len(res)!=len(set(res)):        
    #     print(x,res)
    #     return True
    # else:
    return False
    
def printArray(arr,m):
    for i in range(m):
        for j in range(m):
            print(arr[i][j],end=' ')
        print()    
n = int(input())
arr = list([0]*(n+1) for i in range(n+1))
k=0
for i in range(n+1):
    for j in range(n+1):
        arr[i][j]= k 
        k+=1
f = n+1 
combi = combinations(range(f*f),4)
count = 0
for x in combi:
    x = list(x)
    if check(x,f):
        count+= 1 
print(count)        


printArray(arr,n+1)        