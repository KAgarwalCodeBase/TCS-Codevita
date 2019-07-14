from collections import deque
from functools import reduce
from copy import deepcopy
def deciToB6(num):
    queue=deque()
    while num:
        rem = num%6 
        queue.appendleft(rem)
        num=num//6 
    return reduce((lambda x,y:x+y),queue)
    
    
def inversion(arr):
    arrSorted = sorted(deepcopy(arr))
    dA ={}  # to map index of actual array to corresponding value
    dS={}   # to map index of sorted array to corresponding value
    for i in range(len(arrSorted)):
        dA[arr[i]] = i 
        dS[arrSorted[i]] = i
    count=0    
    for i in range(len(arr)):
        val = (i - dS[arr[i]] )
        if  val > 0:
            count+= val
    return count        
    
if __name__=="__main__":
    n = int(input())
    arr = list(map(int,input().split(',')))
    darr=[0]*n
    for i in range(n):
        darr[i]=deciToB6(arr[i])
    print(inversion(darr))    