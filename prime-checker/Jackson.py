import sys
n=int(sys.argv[1])
print(all([n%i for i in range(2,n)])*(n!=1))