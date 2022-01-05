r,f=range,lambda n:1if n<2else n*f(n-1)
def g(s,n):a=len(s);b=f(a-1);c=n//b;return s[c]+g(s[:c]+s[c+1:],n%b)if a else''
[print(g(''.join([str(j+1)for j in r(i)]),n))for i in r(1,6)for n in r(f(i))]

# Above solution is 197 chars

# Expanded form of permutation function:
def getPerm(s,permIdx):
	a = len(s)
	if a==0: return ''
	currElIdx = permIdx//f(a-1)
	curr = s[currElIdx]
	rest = s[:currElIdx]+l[currElIdx+1:]
	nextPermIdx = permIdx%f(a-1)
	return curr + getPerm(rest, nextPermIdx)

