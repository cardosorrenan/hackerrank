#!/bin/python3
import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl, vly, state = 0, 0, ''
    for i in range(0, n):
        if s[i] == 'U':
            lvl += 1
        else:
            lvl -= 1
        if lvl > 0:
            state = 'above'
        elif lvl < 0:
            state = 'below'
        elif lvl == 0 and state == 'below':
            vly += 1
    return vly

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
