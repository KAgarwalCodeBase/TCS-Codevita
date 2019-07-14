if __name__=="__main__":
	#Integer
	n = int(input())
	#size of array
	arr = list([0]*(2*n) for i in range(n))
	#initial value
	f = 10
	#initial half value filling 
	for i in range(n):
		k = i*2
		for j in range(k):
			arr[i][j]='*'
		for j in range(k,k+n-i):
			arr[i][j] = str(f) 
			f+=10 
	
	#odd value printing variable
	k=1
	#second half value printing loop
	for i in range(n-1,-1,-1):
		c =1
		for j in range(i,n):
			if c==k:
				arr[i][n+j] = str(f)[:-1]
			else:
				arr[i][n+j] = str(f)
			f+=10
			c+=1 
		k+=1    
	#final answer submission	
	for i in range(n):
		print(*arr[i],sep='')    