from collections import Counter
def check(p,s):
    d = {}
    #ordering the new alphabate in order
    k=1
    for ch in p:
      d[ch] = k
      k+=1
    counter = Counter(s)
    d2 ={}
    for ch in s:
      if ch not in d2:
        d2[ch] = d[ch]
    res = []
    
    for k in d2:
      res.append([d2[k],k])
    res.sort()
    for x in res:
      print(x[1]*counter[x[1]],end='')
    print()
    
    
      
for _ in range(int(input())):
        p=list(input() )
        s=list(input())
        check(p,s)
       