if __name__=="__main__":
	#length of string
	n=int(input())
	#actual string
	s=input()
	
	l = [0]*len(s)
	d = dict()
	for i in range(len(s)):
		if s[i] not in d:
			d[s[i]] = i
		else:
			l[i] = l[d[s[i]]]+1
			d[s[i]] = i
	
	#taking and printing the result of each query
	for i in range(int(input())):
		p=int(input())
		print(l[p-1])      