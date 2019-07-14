https://ide.geeksforgeeks.org/ScllDJYTxt
from copy import deepcopy
from collections import Counter
string = input()
s=deepcopy(string)
q = int(input())
sol= []
for i in range(q):
    d,a = input().split()
    d = d.upper()
    a=int(a)
    if d=='L':
        s = s[a:]+s[:a]
        sol.append(s[0])
    if d=='R':
        s=s[-a:]+s[:-a]
        sol.append(s[0])
len1 = len(string)
len2 = len(sol)
d={}
for x in sol:
    if x in d:
        d[x]+= 1 
    else:
        d[x] = 1
        
flag=False
for i in range(len1-len2+1):
    counter = Counter(string[i:i+len2])        
    if counter==d:
        print('YES')
        flag=True
        break
if flag==False:
    print("NO")
