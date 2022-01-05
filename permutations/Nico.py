f=lambda n:1if n<2else n*f(n-1)
def g(s,n):a=len(s);b=n//f(a-1);return s[b]+g(s[:b]+s[b+1:],n%f(a-1))if a else''
[print(g(''.join([str(j) for j in range(1,i+1)]),n))for i in range(1,6)for n in range(f(i))]

# Above solution is 205 chars

# Expanded form of permutation function
def getPerm(s,permIdx):
	a = len(s)
	if a==0: return []
	currElIdx = permIdx//f(a-1)
	curr = s[currElIdx]
	rest = s[:currElIdx]+l[currElIdx+1:]
	nextPermIdx = permIdx%f(a-1)
	return [curr]+getPerm(rest, nextPermIdx)

