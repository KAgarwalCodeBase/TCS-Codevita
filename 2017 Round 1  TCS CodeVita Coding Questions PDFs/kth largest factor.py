import math
import heapq
def factor(num):
    res=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            res.append(i)
            if i!=num//i:
                res.append(num//i)
        i+=1 
    return res    
    
    
if __name__=="__main__":
    arr = list(input().split(';'))
    for i in range(len(arr)):
        val=arr[i]
        n,k=map(int,val.split(','))
        temp = factor(n)
        if len(temp)<k:
            print(1)
        else:
            temp2 = heapq.nlargest(k,temp)
            print(temp2[-1])
            
