https://ide.geeksforgeeks.org/qyvLDEs7Jg
from collections import deque
class Node:
    def __init__(self,x,y,dis):
        self.x   =  x
        self.y   =  y
        self.dis = dis


def printMaze(arr,m):
    for i in range(m):
        for j in range(m):
            print(arr[i][j],end=' ')
        print()
def check(r,c,m):
    return r>=0 and r<m and c>=0 and c<m

def findMin(arr,m):
    start = Node(0,1,1)
    end   = [m-1,m-2]
    visited = [[False]*m for i in range(m)]
    visited[0][1] = True
    queue = deque()
    queue.append(start)
    row = [1,-1,0,0]
    col = [0,0,1,-1]
    while queue:
        curr = queue.popleft()
        if curr.x==end[0] and curr.y==end[1]:
            return curr.dis
        for i in range(4):
            r = curr.x+row[i]
            c = curr.y+col[i]
            if check(r,c,m) and arr[r][c]==0 and visited[r][c]==False:
                visited[r][c]=True
                node = Node(r,c,curr.dis+1)
                queue.append(node)






#shortest path in maze
n,k = map(int,input().split(','))
wall=[0]*k
#inserting wall coordinate
for i in range(k):
    wall[i]=list(map(int,input().split(',')))

#new size of matrix
m=2*n+1

arr =[[0]*(2*n+1) for i in range(2*n+1)]

for i in range(m):
    for j in range(m):
        if i&1 and j&1:
            arr[i][j]=0

for i in range(k):
    x1,y1,x2,y2=wall[i]
    x1=2*x1;y1=2*n-2*y1;x2= 2*x2;y2=2*n-2*y2
    if x1==x2:
        for j in range(y1,y2+1):
            arr[j][x1] = 1
    if y1==y2:
        for j in range(x1,x2+1):
            arr[y1][j] = 1
for i in range(m):
    arr[i][0]=1
    arr[0][i]=1
    arr[i][m-1]=1
    arr[m-1][i]=1
#entry
arr[0][1]=0
#exit
arr[m-1][m-2]=0
minn=findMin(arr,m)
for i in range(1,m-1):
    for j in range(1,m-1):
        if arr[i][j]==1:
            flag=1
            arr[i][j]=0
            minn=min(minn,findMin(arr,m))
            arr[i][j]=1


print(minn//2)
