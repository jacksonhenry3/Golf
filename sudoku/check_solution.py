import sys,os
import numpy as np

solFile = sys.argv[1]

# --- Reference Sudoku solver ---

# board: A 9 line string where each line contains 9 digits, and each line ends with \n
def boardStr2List(boardStr):return [int(i) for i in boardStr.replace('\n','')]

def boardList2Str(boardList):
	return '\n'.join([''.join(c) for c in np.array([str(i) for i in boardList]).reshape((9,9))])

def solveSudokuList(l):
    try:
        n=l.index(0)
        for i in range(1,10):
            if sum([l[m]==i and sum([(n%9==m%9),(n//9==m//9),(n//27==m//27)*((n//3)%3==(m//3)%3)])for m in range(81)]):continue
            L=solveSudokuList(l[:n]+[i]+l[n+1:])
            if L:return L
    except:return l
    return 0

# --- Solution evaluator ---

boards = []
currBoard = ''
for idx,line in enumerate(open('sudoku_inputs.txt').readlines()):
	if idx%10!=0: currBoard += line
	if (idx+1)%10==0:
		boards.append(currBoard)
		currBoard = ''

numTestBoards = 10
boardIdxOrder = np.random.choice(len(boards), numTestBoards, replace=False)
failed = False
for idx, boardIdx in enumerate(boardIdxOrder):
	print(idx+1, '| Board idx', boardIdx, '...', end=' ')
	board = boards[boardIdx]
	cmd = 'python %s <<EOF\n%sEOF'%(solFile, board)
	stream = os.popen(cmd)
	output = stream.read().strip()
	expected = boardList2Str(solveSudokuList(boardStr2List(board)))
	if output != expected:
		print('failed!')
		print('Expected:')
		print(expected)
		print('Output:')
		print(output)
		failed = True
		break
	print('passed')

if not failed: print('%i/%i tests passed' % (numTestBoards,numTestBoards))
