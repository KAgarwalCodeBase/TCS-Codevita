n = int(input())
arr = list(map(float,input().split()))
arr.sort()
rate = float(input())
factor = (100-rate)/100
val=0
for i in range(n):
    day = n-i-1
    temp = (arr[i]**3)*(factor**day)
    val +=temp
res ="%0.5f"%(val*4*3.14/3)
print(res[:-3])