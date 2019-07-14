https://ide.geeksforgeeks.org/vIj9Yy83Ur
from collections import deque
def check(r,c,n):
    return r>=0 and r<n and c>=0 and c<n 

def feasible(sr,sc,grid,n):
    visited =[[False]*n for i in range(n)]
    visited[sr][sc] =True
    d = {'E':[0,1],'W':[0,-1],'S':[1,0],'N':[-1,0]}
    queue = deque()
    queue.append([sr,sc])
    while queue:
        curr = queue.popleft()
        if curr[0]==(n-1) and curr[1]==(n-1):
            return True
        string = grid[curr[0]][curr[1]]    
        for s in string:    
            r = curr[0]+d[s][0]
            c = curr[1]+d[s][1]
            if check(r,c,n) and grid[r][c]!='D' and visited[r][c]==False:
                visited[r][c]=True
                queue.append([r,c])
    return False            
    
    
n= int(input())
grid = [0]*n 
for i in range(n):
    grid[i]=list(input().split(','))
count=0
for i in range(n):
    if grid[0][i]!='D' and feasible(0,i,grid,n):
        count+=1 
    if i!=0 and grid[i][0]!='D' and feasible(i,0,grid,n):
        count+=1 
print(count)        