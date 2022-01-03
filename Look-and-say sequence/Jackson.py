from itertools import groupby
s='1'
for _ in[1]*20:
 print(s);s=''.join([str(len(list(g)))+c for c,g in groupby(s)])