import bisect
if __name__=="__main__":
    s,r = map(int,input().split())
    arr  = list(map(int,input().split()))
    arr.sort()
    for i in range(r):
        lower,upper = map(int,input().split())
        indl= bisect.bisect_left(arr,lower)
        if indl==len(arr):
            print(0)
            continue
        indu = bisect.bisect_right(arr,upper)
        if indu==0:
            print(0)
            continue
        print(indu-indl)