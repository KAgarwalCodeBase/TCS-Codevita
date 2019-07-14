#hop game
def count(arr,flag,i):
    if i==len(arr):
        return 0
    val1=0
    if flag==False and (i+3)<len(arr):
        val1 = arr[i]+2*arr[i+3]+count(arr,True,i+3)

    val2 = arr[i]+count(arr,flag,i+1)

    val3=0
    if i+2<len(arr):
        val3 = arr[i]+arr[i+2]+count(arr,flag,i+2)

    return max(val1,val2,val3)



n = int(input())
arr = list(map(int,input().split()))
print(count(arr,False,0))