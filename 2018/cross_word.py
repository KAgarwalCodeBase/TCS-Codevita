https://ide.geeksforgeeks.org/FpaECDZBlw
#incomplete fill function yet to define
from copy import deepcopy
#cross words

def printGrid(grid,n):
    for i in range(n):
        for j in range(n):
            print(grid[i][j],end=' ')
        print()    


def numbering(grid,m,n):
    number =[]
    for i in range(n):
        for j in range(n):
            flag=0
            if grid[i][j]=='$' :
                continue
            if (j+1)<n: #right block present
                #left block present
                if (j-1)>=0 and grid[i][j+1]!='$' and grid[i][j-1]=='$':
                    number.append([i,j,1,'A'])
                    flag=1
                #left block not present
                elif (j-1)<0 and grid[i][j+1]!='$':
                    number.append([i,j,1,'A'])
                    flag=1
            if (i+1)<n: #bottom block exist
                if (i-1)>=0 and grid[i-1][j]=='$' and grid[i+1][j]!='$':
                    if flag==1:
                        number[-1][2]=2
                        number[-1][3]='AD'
                    else:
                        number.append([i,j,1,'D'])
                elif (i-1)<0 and grid[i+1][j]!='$':
                        if flag==1:
                            number[-1][2]=2
                            number[-1][3]='AD'
                        else:
                            number.append([i,j,1,'D'])
    return number                



if __name__ == "__main__":
    n = int(input())
    inp =[0]*n
    for i in range(n):
        inp[i]=list(map(int,input().split(',')))
    
    m=int(input())
    sol =[0]*m
    for i in range(m):
        sol[i] = input()
        
    #making grid and coloring black box as  '$'
    grid =list([0]*n for i in range(n))    
    for i in range(n):
        x = inp[i]
        for j in range(0,len(x),2):
            start = x[j]-1
            no = x[j+1]
            for k in range(no):
                grid[i][start+k]='$'
    printGrid(grid,n)
    grid_ori = deepcopy(grid)
    
    #numbering the grid blank squares
    number  = numbering(grid,m,n)
    print(number)
    
    # fill(grid,number,n,m,sol)
