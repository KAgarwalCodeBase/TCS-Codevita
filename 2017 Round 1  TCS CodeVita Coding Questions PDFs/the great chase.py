if __name__ == "__main__":
    for _ in range(int(input())):
        I,D,Z = map(int,input().split())
        if D>=Z:
            print(-1)
            continue
        t=1
        while(1):
            val = (Z*t-I)/D
            if int(val)==val:
                break
            t+=1
        print(t)
       