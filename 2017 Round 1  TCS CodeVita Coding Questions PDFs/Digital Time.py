import sys
from collections import Counter
from itertools import permutations
from copy import deepcopy
arr = list(map(int,input().split(',')))
#prepering reusable copy of original array-> arr
arrcopy = deepcopy(arr)



#making all possible permutations of 2digit and storing in dict->possible
permu = permutations(arr,2)
poss =[str(x[0])+str(x[1]) for x in permu]
possible = dict.fromkeys(poss,1)

#storing all possible hour value with given digits
HH=[]
for i in range(24,-1,-1):
    val = "{:02d}".format(i)
    if val in possible and int(val[0]) in arr and int(val[1]) in arr :  
        HH.append(val)
		
#storing all possible minute value with given digits		
MM=[]        
for i in range(59,-1,-1):
    val = "{:02d}".format(i)
    if val in possible and int(val[0]) in arr and int(val[1]) in arr :  
        MM.append(val)

#storing all possible second value with given digits (i.e. same as minute value)		
SS=deepcopy(MM)

#checking either hour or minute or second values is none if yes than print impossible
if len(HH)==0 or len(MM)==0:
    print('Impossible')
    sys.exit()
#checking for maximum possible value of time	
elif HH[0]=='24' and MM[-1]=='00' and arr.count(0)>=4:
        print('24:00:00')
        sys.exit()
#checking if 24 is present on hour but does not have required zeros
if HH[0]=='24':
    HH.pop(0)
    if len(HH)==0:
        print('Impossible')
        sys.exit()

#if neither of above condition generate result than check for maximum time if possible		
flag=1
while flag:
    arr=deepcopy(arrcopy)
    hour = HH[0]
    arr.remove(int(hour[0]))
    arr.remove(int(hour[1]))
    res=0
    flag2=1 
    while flag2:
        minute = MM[0]
        if int(minute[0]) in arr and int(minute[1]) in arr:
            arr.remove(int(minute[0]))
            arr.remove(int(minute[1]))
            flag2=0
            flag3=1
            while flag3:
                second = SS[0]
                if int(second[0]) in arr and int(second[1]) in arr:
                    arr.remove(int(second[0]))
                    arr.remove(int(second[1]))
                    flag3=0
                    flag2=0
                    flag=0
                    res=1
                else:
                    SS.pop(0)
                    if len(SS)==0:
                        flag3=0
                        flag2=0
        else:            
            MM.pop(0)
            if len(MM)==0:
                flag2=0
    if res==0:
        HH.pop(0)
    if len(HH)==0:
        flag=0
        
if res==0:
    print('Impossible')
else:
    print(hour+':'+minute+':'+second)


    
    
    
    
