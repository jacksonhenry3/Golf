from itertools import accumulate as a
def f(l):
 s=a([(c=="(")-(c==")")for c in l])
 for i,e in enumerate(s):
  if e<0:return i
  if e==0:c=i+1
 if s[-1]==0:c=-1
 return c
        
lisp = "()()()(((()())))(()))"
    
print(f(lisp))
