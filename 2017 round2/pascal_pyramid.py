#pascal pyramid
from itertools import permutations
n = int(input())
arr = list(map(int,input().split(",")))
arr.sort(reverse=True)
arr=arr[:6]
permu = permutations(arr)
maxx=0
for x in permu:
   x=list(x)
   for i in range(4):
       for i in range(len(x)-1):
           x[i]+=x[i+1]
       x.pop()
   maxx=max(maxx,x[0]*x[1])
print(maxx)

