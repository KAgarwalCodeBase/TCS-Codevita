#bank statement
rate = float(input())
entries = int(input())
arr = [0]*entries
#sum of all balance
s_f_b = 0
k=1;flag=0
fault =[]
for i in range(entries-2):
    arr[i]= list(input().split())
    arr[i][1]=int(arr[i][1])
    arr[i][3]=int(arr[i][3])
    s_f_b +=int(arr[i][-1])
    if k!=int(arr[i][0]) and flag==0:
        fault=[k,k+1];flag=1
    k+=1
Interest = float(input())
Interest = float('{:06f}'.format(Interest))

#first entry after fault entries
feaf = fault[0] - 1
#last entry before fault entries
lebf = feaf-1

#ms1-> missed serial no. 1
#ms2-> missed serial no. 2
#ma1-> missed amount 1
#ma2-> missed amount 2
#mtt1-> missed transaction type 1
#mtt2-> missed transaction type 2
#mb1-> missed balance 1
#mb2-> missed balance 2

if arr[feaf][2]=='debit':
    mb2 = int(arr[feaf][1]) + int(arr[feaf][3])
elif arr[feaf][2]=='credit':
    mb2 = int(arr[feaf][3]) - int(arr[feaf][1])

s_f_b+=mb2
mb1 = round((Interest*100*365)/8- s_f_b)

res =[0]*2
if fault[0]==1:
    res[0]=[1,mb1,'credit',mb1]
    if mb2>mb1:
        res[1]=[2,mb2-mb1,'credit',mb2]
    else:
        res[1]=[2,mb1 - mb2,'debit',mb2]


else:
    # debit on fault entry 1
    if  arr[lebf][3]>mb1:
          res[0]=[fault[0],arr[lebf][3]-mb1,'debit',mb1]
    #credit on fault entry1
    elif arr[lebf][3]<mb1:
          res[0]=[fault[0],mb1-arr[lebf][3],'credit',mb1]
    #debit on fault entry2
    if mb2<mb1:
          res[1] =[fault[1],mb1-mb2,'debit',mb2]
    #credit on fault entry 2
    else:
          res[1] = [fault[1],mb2-mb1,'credit',mb2]

print(*res[0])
print(*res[1])

