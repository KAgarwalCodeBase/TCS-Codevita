from math import pow
if __name__ == "__main__":
    p = int(input())
    y = int(input())
    summ=[0]*2
    for i in range(2):
        slab = int(input())
        for j in range(slab):
            year,rate = map(float,input().split())
            monthly_rate = rate/1200
            temp = 1+monthly_rate
            temp2 = pow(temp,year*12)
            emi  =  p*monthly_rate/(1-1/temp2)
            summ[i]+=emi*year*12
            
    if summ[0]<summ[1]:
        print('BANK A')
    else:
        print('BANK B')