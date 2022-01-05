import itertools
for i in range(1,6):
 for p in itertools.permutations('123456'[:i]):print(*p,sep='')