def ArraySum(arr):
    summ=0
    for ch in arr:
        if ord(ch)>=48 and ord(ch)<=54:
            summ+=int(ch)
    return summ        

runrate1= float(input())
Sbat1,Nbat2 = map(int,input().split())
arr = list(input().split())
runrate2 = float(input())
#total delivery in break
d=len(arr)

if d>=50 or d<=0:
    sys.exit()
# let b1 be ball before break
b = int((d*runrate2 - 6*ArraySum(arr))/(runrate1 - runrate2))

total_run = int((b+d)*runrate2/6)
#ball delivered in over
b = b%6
k=b 
for i in range(len(arr)):
    if k%6==0:
        Sbat1,Nbat2=Nbat2,Sbat1
    k=k%6
    if arr[i]=='W':
        Sbat1 = 0
    elif arr[i]=='1':
        Sbat1+=1 
        Sbat1,Nbat2=Nbat2,Sbat1
    elif arr[i]=='3':
        Sbat1+=3 
        Sbat1,Nbat2=Nbat2,Sbat1
    elif arr[i]=='5':
        Sbat1+=5 
        Sbat1,Nbat2=Nbat2,Sbat1
    elif arr[i]=='2':
        Sbat1+=2 
    elif arr[i]=='4':
        Sbat1+=4 
    elif arr[i]=='6':
        Sbat1+=6 
    k+=1    
if (b+d)%6==0:
    Sbat1,Nbat2=Nbat2,Sbat1
    
print(total_run,Sbat1,Nbat2)        
    
       
       
        