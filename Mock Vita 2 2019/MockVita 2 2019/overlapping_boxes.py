#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

#Overlapping Boxes
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int,input().split()))
    
lx=100000;ly=100000;rx=-1;ry=-1
for i in range(n):
    #finding minimum of left x coordinate
    lx = min(lx,arr[i][0])
    #finding minimum of left y coordinate
    ly=min(ly,arr[i][1])
    #finding maximum of right x coordinate
    rx = max(rx,arr[i][2])
    #finding maximum of right y coordinate
    ry = max(ry,arr[i][3])

# print(lx,ly,rx,ry)

#(p,q) bottom left || (r,s) top right
res={}
for i in range(ly,ry):
    for j in range(lx,rx):
        p=j;q=i;r=j+1;s=i+1
        count=0
        for k in range(n):
          if arr[k][0]<=p and arr[k][1]<=q and arr[k][2]>=r and arr[k][3]>=s:
              count+=arr[k][4]
        if count not in res:
            res[count]=1
        else:
            res[count]+=1
# print(res)            
maxx=max(res.keys())
print(res[maxx])

