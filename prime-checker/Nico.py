import sys
n=int(sys.argv[1])
print(n>1 and sum([n%i==0for i in range(2,n)])==0)