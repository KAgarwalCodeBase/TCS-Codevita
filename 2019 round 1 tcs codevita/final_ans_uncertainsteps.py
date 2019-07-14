def countWays(n) :
    if n==0 or n==1 or n==2 :
        return n
    if n==3:
        return 4
    d = [0]*(n+1)
    d[0]=1;d[1]=1;d[2]=2;d[3]=4;
        
    res = [0] * (n + 1)
    res[0] = 1;res[1] = 1;res[2] = 2

    for i in range(3, n + 1) :
        res[i] = (res[i - 1]%(10**9+7) + res[i - 2]%(10**9+7))%(10**9+7)
        d[i] = (d[i-1]%(10**9+7) +d[i-2]%(10**9+7) +res[i-3]%(10**9+7))%(10**9+7)

    return d[n]
def find(n):
    res = [0,1,2,4,7,13]
    if n<6:
        return res[n]
    a=1;b=2;x=7;y=13
    for i in range(6,n+1):
        c =(a%(10**9+7)+b%(10**9+7))%(10**9+7) 
        a=b 
        b=c
        z=(x%(10**9+7)+y%(10**9+7)+c%(10**9+7))%(10**9+7) 
        x = y 
        y = z 
    return z    
if __name__=="__main__":
    # Driver code
    n = int(input())
    print(find(n))