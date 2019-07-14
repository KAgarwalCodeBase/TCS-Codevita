import sys
#Numbers with non-decreasing digits

n= input()
sign = False if int(n)>0 else True

if len(n)==1 or (len(n)==2 and n[0]=='-'):
    print(n)
    sys.exit()

if sign:
    n=n[1:]
prev =''
flag=0
res=[]
for i in range(len(n)-1):
    if flag==1 and sign==False:
        res.append(str(9))
        continue
    if flag==1 and sign==True:
        res.append(prev)
        continue
    ch1 = int(n[i])
    ch2 = int(n[i+1])
    if ch1>ch2 and sign==False:
        res.append(str(ch1-1))
        flag=1
    elif ch1>ch2 and sign==True:
        res.append(str(ch1))
        prev=str(ch1)
        flag=1
    else:
        res.append(str(ch1))


if flag==1 and sign==False:
    res.append(str(9))
elif flag==1 and sign:
    res.append(prev)
else:
    res.append(n[-1])


if sign==False:
    print(int(''.join(res)))
else:
    print(int('-'+''.join(res)))






