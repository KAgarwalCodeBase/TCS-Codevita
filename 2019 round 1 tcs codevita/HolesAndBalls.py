if __name__ == "__main__":
    n = int(input())
    #from bottom to top
    dia = list(map(int,input().split()))
    m = int(input())
    #from order of release
    balls= list(map(int,input().split()))
    
    #reverse the order of dia 
    # dia = dia[::-1]
    capacity = [0]*n
    res = [0]*m
    
    for i in range(m):
        flag = 0
        for j in range(n-1,-1,-1):
            if capacity[j]==(j+1):
                continue
            elif capacity[j]<(j+1) and dia[j]>=balls[i]:
                capacity[j]+=1 
                res[i] = j+1 
                flag = 1 
                break
        if flag==0:
            res[i] = 0
    # print(capacity)        
    print(*res)        
            
                
                