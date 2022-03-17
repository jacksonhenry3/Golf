def f(s):
	i=0
	for j in s:
		if j=="(":
			i+=1
		elif j==")":
			i-=1
		if i<0:return i==0
	return i==0
