#greedy hostler
n= int(input()) #total no. of meters
arr = list(input().split())
reading = float(input())
d = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
summ=0
for x in arr:
    x=x.upper()
    count=0
    for i in range(len(x)-1):
        ch1 = x[i]
        ch2 = x[i+1]
        if ch1=='J' and ch2=='A':
            count=count*10+0
        elif ch1 =='I' and ch2=='B':
            count=count*10+1
        elif ch1 =='H' and ch2=='C':
            count=count*10+2
        elif ch1 =='G' and ch2=='D':
            count= count*10+ 3
        elif ch1 =='F' and ch2=='E':
            count= count*10+4
        else:
            count= count*10 + d[ch1]
    #adding last character place value
    count=count*10+d[x[-1]]
    summ+=count
# print(summ,reading)
if summ>reading:
    print('GREEDY')
else:
    print('INNOCENT')