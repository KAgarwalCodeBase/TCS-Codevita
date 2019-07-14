if __name__=="__main__":
    n,p,q = map(int,input().split(','))
    arr =[0]*n
    for i in range(n):
        arr[i] = list(input().split(';'))
    row,col = map(int,input().split(','))
    row,col=row-1,col-1
    total_move=p*q
    for i in range(total_move):
        ind = arr[row][col]
        row,col = map(int,ind.split(','))
        row,col=row-1,col-1
    print(ind)    
    