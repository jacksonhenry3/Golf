import itertools
r=range(1,6)
[print(*p,sep='')for i in r for p in itertools.permutations(r[:i])]