https://ide.geeksforgeeks.org/CCIBYDPOiQ
import sys
import math
#colliding cannon
# d h 
# la,ls,ra,rs 
d,h = map(float,input().split())
la,ls,ra,rs=map(float,input().split(','))
#changing degree angle to radian 
flag=0
if la<0 and ra<0:
	flag=1
la = abs(la)
ra = abs(ra)
	
lar = math.radians(la)
rar = math.radians(ra)

b1 = round(3*h/math.tan(lar),2)
b2 = round(3*h/math.tan(rar),2)
if b1+b2<d:
    print('NO')
    sys.exit()
#distanc from left
#x=d*tan (x2)/(tan (x1) + tan (x2))
x = round(d*math.tan(rar)/(math.tan(rar)+math.tan(lar)),2)

#total height form x axis at which canons collide h= x*tan(x1)
height = round(math.tan(lar)*x,2)

time1 = round(height/(math.sin(lar)*ls),2)
time2 = round(height/(math.sin(rar)*rs),2)
if abs(time1-time2)>0.5:
    print('NO')
    sys.exit()
    
if height>h/2:
    height=round(h-height,2)
    
#if both the angles are opposite
if flag:
    height=-height 
    
distance = round(x-d/2,2) 
print('YES',',',distance,',',height,sep='')
