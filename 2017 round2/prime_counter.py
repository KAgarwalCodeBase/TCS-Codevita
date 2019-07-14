#prime counter
def primeNo(n):
    l=[]
    arr=[True]*(n+1)
    arr[0]=False;arr[1]=False
    p=2
    while (p*p<=n):
        if arr[p] ==True:
            for i in range(2*p,n+1,p):
                arr[i] = False
        p+=1

    for i in range(2,n+1):
        if arr[i]==True:
            l.append(i)
    return l
prime=primeNo(1000000)
hold_dict = dict.fromkeys(prime,1)
d=[0]*(10**6+1)
#prime=primeNo(31)
#d=[0]*32
last=10**6+1
d[0]=0;d[1]=0;d[2]=1
for  i in range(0,len(prime)-1):
    j=prime[i]
    while j<prime[i+1]:
        d[j]=i+1
        j+=1
for i in range(prime[-1],last):
    d[i]=len(prime)

if __name__=="__main__":
    for _ in range(int(input())):
        l,r = map(int,input().split())
        count=0
        for i in range(l,r+1):
            if d[i] in hold_dict:
                count+=1
        print(count)

    hold_dict = None
