https://ide.geeksforgeeks.org/wygOfCTFPP
from collections import deque
#jurrasic park
#safety index = (no. of safe grassland)*100/total no of grassland
def check(i,j,R,C,park):
    c1 = ((i+1)<R and park[i+1][j]=='W') or ((i+1)==R) #down
    c2 = ((i-1)>=0 and park[i-1][j]=='W') or ((i-1)==-1) #up
    c3 = ((j+1)<C and park[i][j+1]=='W') or ((j+1)==C)   #right
    c4 = ((j-1)>=0 and park[i][j-1]=='W') or ((j-1)==-1)  #left
    # print(c1,c2,c3,c4,i,j)
    return c1 and c2 and c3 and c4
    
#To calculate minimum distance between cage and gate
#gr-> gate row index; gc-> gate column index;
#sr->smilodon row index; sc-> smilodon column index
class Node:
    def __init__(self,x,y,d):
        self.r=x 
        self.c=y  
        self.dt = d
        
def verify(r,c,R,C):
    return r>=0 and r<R and c>=0 and c<C

def disM(gr,gc,mr,mc,park,R,C):
    visited = list([False]*C for i in range(R))
    visited[mr][mc]=True
    row = [1,-1,0,0]
    col = [0,0,1,-1]
    queue=deque()
    start = Node(mr,mc,0)
    queue.append(start)
    while queue:
        curr = queue.popleft()
        if curr.r==gr and curr.c==gc:
            return curr.dt
        for i in range(4):
            r = curr.r+row[i]
            c = curr.c+col[i]
            if verify(r,c,R,C) and park[r][c]=='G' and visited[r][c]==False:
                visited[r][c]=True
                new_node=Node(r,c,curr.dt+1)
                queue.append(new_node)
    
    return False        
    
    
def disS(gr,gc,sr,sc,park,R,C):    
    visited=list([False]*C for i in range(R))
    visited[sr][sc]=True
    row = [1,-1,0,0]
    col = [0,0,1,-1]
    queue = deque()
    start = Node(sr,sc,0)
    queue.append(start)
    
    while queue:
        curr=queue.popleft()
        if curr.r==gr and curr.c==gc:
            return curr.dt
        for i in range(4):
            r = curr.r+row[i]
            c = curr.c+col[i]
            if verify(r,c,R,C) and park[r][c]!='W' and visited[r][c]==False:
                visited[r][c]=True
                new_node = Node(r,c,curr.dt+1)
                queue.append(new_node)
    return False            
                
        
        
def safe(i,j,park,arr,R,C,distance_S):
    cager = arr[-2]
    cagec = arr[-1]
    if check(i,j,R,C,park):
        return True
    if (i==arr[0] and j==arr[1]) or (i==arr[2] and j==arr[3]) or (i==arr[4] and j==arr[5]):
        return True
    distance_M = [0]*3    
    distance_M[0]= disM(arr[0],arr[1],i,j,park,R,C)
    distance_M[1]= disM(arr[2],arr[3],i,j,park,R,C)
    distance_M[2]= disM(arr[4],arr[5],i,j,park,R,C)
    if distance_M[0]!=False and distance_S[0]==False:
        return True
    if distance_M[1]!=False and distance_S[1]==False:
        return True
    if distance_M[2]!=False and distance_S[2]==False:
        return True
    if distance_M[0]!=False and distance_S[0]!=False and distance_M[0]<distance_S[0]:
        return True
    if distance_M[1]!=False and distance_S[1]!=False and distance_M[1]<distance_S[1]:
        return True
    if distance_M[2]!=False and distance_S[2]!=False and distance_M[2]<distance_S[2]:
        return True
    return False    
        
        



R,C = map(int,input().split())
arr=list(map(int,input().split()))
arr = [x-1 for x in arr]
park =[0]*R 
for i in range(R):
    park[i]=list(input().split())
count=0

# print(R,C,park)
#it stores distance of smildone from gates
distance_S=[0]*3
distance_S[0] = disS(arr[0],arr[1],arr[-2],arr[-1],park,R,C)    
distance_S[1] = disS(arr[2],arr[3],arr[-2],arr[-1],park,R,C)    
distance_S[2] = disS(arr[4],arr[5],arr[-2],arr[-1],park,R,C)    


totcount=0        
for i in range(R):
    for j in range(C):
        #location of cage
        if park[i][j]=='G':
            totcount+=1
        if i==arr[-2] and j==arr[-1]:
            continue
        #water bodies or mountains
        if park[i][j]=='W' or park[i][j]=='M':
            continue
        
        if safe(i,j,park,arr,R,C,distance_S):
            count+=1
      
ans = count*100/totcount
print("%0.2f" % (ans))

            
         
        
    