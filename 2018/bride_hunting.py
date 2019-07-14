def check(r,c,n,m):
    if r==0 and c==0:
        return False    
    return  r>=0 and r<n and c>=0 and c<m 
    
n,m = map(int,input().split())
arr = [0]*n 
for i in range(n):
    arr[i] = list(map(int,input().split()))

maxxq=0
maxxr=[]
row = [1,-1,0,0,1,1,-1,-1]
col = [0,0,1,-1,1,-1,-1,1]
for i in range(n):
    for j in range(m):
        if (i==0 and j==0) or arr[i][j]==0:
            continue
        
        count=0
        for k in range(8):
            r=i+row[k]
            c=j+col[k]
            if check(r,c,n,m) and arr[r][c]!=0:
                count+=1
        if count>maxxq:
            maxxq=count
            maxxr = [[i,j]]
        elif count==maxxq:
            maxxr.append([i,j])

if len(maxxr)==1:
    print(maxxr[0][0]+1,':',maxxr[0][1]+1,':',maxxq,sep='')
elif maxxq==0:
    print('No suitable girl found',sep='')
else:    
    diff = [0]*len(maxxr)

    k=0
    for x in maxxr:
        diff[k] = x[0]+x[1]
        k+=1    
    
    minn = min(diff)
    count = diff.count(minn)
    if count>1:
        print('Polygamy not allowed',sep='')
    else:
        ind = diff.index(minn)
        print(maxxr[ind][0]+1,':',maxxr[ind][1]+1,":",maxxq,sep='')
                
                