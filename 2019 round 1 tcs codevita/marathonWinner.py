if __name__=="__main__":
    n = int(input())
    t = int(input())
    #for storing time-> steps values
    arr = [0]*n 
    for i in range(n):
        arr[i] = list(map(int,input().split()))
    
    if n==1 or t==1:
        print(1)
    else:    
        
        #for calculating accumulative sum of distance at different time 
        summ= [[0]*t for i in range(n) ]  
        for i in range(n):
            f = arr[i][-1]
            prev = 0
            for j in range(t):
                summ[i][j]= prev+arr[i][j]*f
                prev = summ[i][j]
    
        #for storing result of different lap
        res=[]
        for i in range(1,t,2):
            maxx = -1
            temp =[]
            for j in range(n):
                if maxx<summ[j][i]:
                    temp =[]
                    maxx = summ[j][i]
                    temp.append(j)    
                elif maxx==summ[j][i]:
                     temp.append(j)
            res.append(temp)         
        #for storing final ans count
        ans =[0]*n 
        for x in res:
            for y in x:
                ans[y]+=1 
                
        maximum = max(ans)
        print(ans.index(maximum)+1)
        