#formal way
# =============================================================================
import math
# from itertools import permutations
from collections import deque
def factors(n):
     start=[]
     end=deque()
     for i in range(1,int(math.sqrt(n))+1):
         if n%i==0:
             start.append(i)
             if i!=n//i:
                 end.appendleft(n//i)
     end = list(end)
     return start+end
# for _ in range(int(input())):
#     n = int(input())
#     arr = factors(n)
#     d = dict()
#     for i in range(len(arr)-1):
#         d[arr[i]]=arr[i+1]
#     #filling last position with none
#     d[arr[len(arr)-1]]=None
#     perm = permutations(arr)
#
#     count=0
#     for p in perm:
#         flag=True
#         for i in range(len(p)-1):
#             curr = p[i]
#             nxt = p[i+1]
#             if d[curr]==nxt:
#                 flag=False
#                 break
#         if flag:
#             count+=1
#
#     print(len(arr),count)
# =============================================================================
# =============================================================================
# Pattern formed
# f(x) =  1      x=2;
#         3      x=3,
#         11     x=4    (3*3+2*1=11)
#         53     x=5    (4*11+3*3=53)
# where a
# a=ans;
# x=length of factors
# =============================================================================
d =[0,0,1,3,11]+[0]*66
for i in range(5,71):
    d[i]=d[i-1]*(i-1)+d[i-2]*(i-2)
for _ in range(int(input())):
    n = int(input())
    arr = factors(n)
    length = len(arr)
    print(d[length])
