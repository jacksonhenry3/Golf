r=range
def s(l):
	if'0'not in l:return l
	n=l.index('0')
	for i in r(9):
		x=str(i+1)
		if sum([l[m]==x and (n%9==m%9)+(n//9==m//9)+(n//27==m//27)*((n//3)%3==(m//3)%3)for m in r(81)])==0:
			L=s(l[:n]+[x]+l[n+1:])
			if L:return L
	return 0
l=[]
for i in[1]*9:l+=input()
print('\n'.join([''.join(s(l)[9*i:9*(i+1)])for i in r(9)]))