import sys, os
import numpy as np

def getTestInputs():
     return list(range(1,51)) + list(np.random.randint(10000, size=50))

def isPrimeMaster(n):
    if n==1: return False
    if n==2: return True
    searchSpace = [2]+list(range(3,int((n)**.5+2),2))
    return not np.any([n%d==0 for d in searchSpace])

def attemptCast2Number(s):
    try:
        return float(s)
    except Exception as e:
        return s

def checkSolution(solutionFilename):
    testInputs = getTestInputs()
    print('Test inputs:', ', '.join([str(ti) for ti in testInputs]))
    for idx,testInput in enumerate(testInputs):
        print('Testing input %i/%i (%i)          \r'%(idx+1, len(testInputs), testInput), end='')
        cmd = 'python %s %i' % (solutionFilename, testInput)

        stream = os.popen(cmd)
        output = stream.read().strip()
        if output in ['False', 'True']: outputProcessed = output=='True'
        else: outputProcessed = bool(attemptCast2Number(output))
        
        expected = isPrimeMaster(testInput)
        if outputProcessed!=expected:
            print()
            print('Failed on input "%i" (expected %s, got %s)' % (testInput, str(expected), str(outputProcessed)))
            return
    print()
    print('Passed on all inputs!')

solutionFilename = sys.argv[1]
checkSolution(solutionFilename)