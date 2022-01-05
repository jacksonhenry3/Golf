S='1'
for i in[1]*20:
	print(S);a,b,m=S[0],1,''
	for c in S[1:]:z=a!=c;m+=z*(str(b)+a);b+=1-b*z;a=c
	S=m+str(b)+a