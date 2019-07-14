def nCr(n,r):
    if n<r:
        return False
    if r==0 or n==0:
        return 1
    if r==1:
        return n
    step = min(r,n-r)
    mul=1
    for i in range(step,0,-1):
        mul *=n/i
        n-=1
    return round(mul)

import sys
#this is the paper generation program
#taking input from user
x = int(input())
s = int(input())
y = int(input())
m = int(input())
z = int(input())
cp = int(input())
a,b =input().split()
c = input()

#contains actual no. of question in order of their occurence in different sections
sec = [x,y,z]

#contains actual no. of question which should be included in paper
inc = [s,m,cp]

#total questions cummulative sum
ques =[x,x+y,x+y+z]

#storing the numbered value of constraint
info =[ord(a)-64,ord(b)-64,ord(c)-64]

#it contains the information about constraint in which section they lie
store =[0]*3

for i in range(3):
    if info[0]<=ques[i]:
        store[0]=i
        break

for i in range(3):
    if info[1]<=ques[i]:
        store[1]=i
        break

for i in range(3):
    if info[2]<=ques[i]:
        store[2]=i
        break

count=1
if (sec[store[0]]-1)<inc[store[0]] and sec[store[1]]-1<inc[store[1]]:
    print(0)
    sys.exit()
if (sec[store[2]]-1)<inc[store[2]]:
    print(1)
    sys.exit()

#decreasing the count by 1 of questions for section which include last constraint
sec[store[2]]-=1

flag1=False;flag2=False
if (sec[store[0]]-1)<inc[store[0]]:
    flag1=True
if sec[store[1]]-1<inc[store[1]]:
    flag2=True

if flag1==False:
    sec[store[0]]=sec[store[0]]-1
    count += nCr(sec[0],inc[0])*nCr(sec[1],inc[1])*nCr(sec[2],inc[2])
    sec[store[0]]+=1
if flag2==False:
    sec[store[1]]=sec[store[1]]-1
    count += nCr(sec[0],inc[0])*nCr(sec[1],inc[1])*nCr(sec[2],inc[2])
    sec[store[1]]+=1
print(nCr(x,s)*nCr(y,m)*nCr(z,cp))
print(count)

