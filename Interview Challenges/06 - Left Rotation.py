#!/bin/python3
import os

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(0,d):
        a.extend([a[0]])
        del a[0]
    return a
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

