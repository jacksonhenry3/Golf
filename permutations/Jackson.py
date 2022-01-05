import itertools as I
r=range(1,6)
[print(*p,sep='')for i in r for p in I.permutations(r[:i])]