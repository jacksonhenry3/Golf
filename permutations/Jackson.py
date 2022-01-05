import itertools
s='123456'
for i in range(1,6):
 for p in itertools.permutations(s[:i]):print(*p,sep='')