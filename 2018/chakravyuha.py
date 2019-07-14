n=int(input())  #n-> last row index
m=n             #m-> last column index
r=0;c=0         #starting row index and column index
powerpoint =[(0,0)]
size = n                 
arr= list([0]*n for i in range(n))
k=1
while r<n and c<m:
    #print first row 
    for i in range(c,m):
        #power point calculation-----------
        if  k%11==0:
            powerpoint.append(tuple([r,i]))
        #end-------------------------------
        arr[r][i]=k
        k+=1 
    r+=1        
    
    #print last column
    for i in range(r,n):
        #power point calculation------------
        if  k%11==0:
            powerpoint.append(tuple([i,n-1]))
        #end----------------------------------
        arr[i][n-1] = k 
        k+=1 
    m-=1    

    #print last row
    if r<n:
        for i in range(m-1,c-1,-1):
            #power point calculation-------------
            if  k%11==0:
                powerpoint.append(tuple([n-1,i]))
            #end--------------------------------
            arr[n-1][i]=k
            k+=1
        n-=1
    
    #print first column
    if c<m:    
        for i in range(n-1,r-1,-1):
            #power point calculation------------
            if  k%11==0:
                powerpoint.append(tuple([i,c]))
            #end--------------------------------    
            arr[i][c]=k 
            k+=1 
        c+=1
        
for i in range(size):
    for j in range(size):
        print(arr[i][j],end=' ')
    print()    
    
print('Total Power points :',len(powerpoint))    
for x in powerpoint:
    print('(',x[0],',',x[1],')',sep='')