#ome egg problem
m,eggs = map(int,input().split())
x=eggs
arr=[0]*m
summ=0
for i in range(m):
    arr[i]=int(input())
    summ += arr[i]

#creatimg list of tuple of index amd values
arr2=[0]*m
for i in range(m):
    arr2[i]=[i,arr[i]]
#sortimg list accordimg to secomd value
arr2.sort(key=lambda x:x[1],reverse=True)

if x>=summ:
    print("Sorry, we cam omly supply",sum(arr)-1,'eggs')
    minn = min(arr)
    ind = arr[::-1].index(minn)
    for i in range(m):
        if i==(m-ind-1):
            print(arr[i],arr[i]-1,1)
        else:
            print(arr[i],arr[i],0)
else:
    d={}
    adjind=-1
    adjust=0
    for i in range(m):
        if x>0:
            if arr2[i][1]<x:
                x-=arr2[i][1]
                d[arr2[i][0]]=1
            else:
                adjind=arr2[i][0]
                adjust = arr2[i][1] - x
                x=0
        else:
            break

    print("Thamk you, your order for",eggs,"eggs are accepted ")
    for i in range(m):
        if i==adjind:
            print(arr[i],arr[i]-adjust,adjust)
        elif i in d:
            print(arr[i],arr[i],0)
        else:
            print(arr[i],0,arr[i])


