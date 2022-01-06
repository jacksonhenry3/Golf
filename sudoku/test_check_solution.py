import numpy as np

board=[int(i) for l in [input() for i in range(9)] for i in l]

def solveSudokuList(l):
    try:
        n=l.index(0)
        for i in range(1,10):
            if sum([l[m]==i and sum([(n%9==m%9),(n//9==m//9),(n//27==m//27)*((n//3)%3==(m//3)%3)])for m in range(81)]):continue
            L=solveSudokuList(l[:n]+[i]+l[n+1:])
            if L:return L
    except:return l
    return 0

def boardList2Str(boardList):
	return '\n'.join([''.join(c) for c in np.array([str(i) for i in boardList]).reshape((9,9))])

print(boardList2Str(solveSudokuList(board)))