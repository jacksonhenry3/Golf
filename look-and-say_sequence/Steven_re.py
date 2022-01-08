import re
r=re.compile("|".join(d + "+" for d in "1234567890"))
def f(s,x=""):
	while m:=r.match(s):e=m.end();x+=f"{e}{s[0]}";s=s[e:]
	return x

def g(s="1"):
	for i in range(20):s=f(s)
	return s
g()
