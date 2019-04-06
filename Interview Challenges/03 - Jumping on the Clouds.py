#!/bin/python3
import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps, pos = 0, 0
    while(pos < len(c)-1):
        if c[pos+1] == 0:
            if pos != len(c)-2:
                if c[pos+2] == 0:
                    pos += 2
                else:
                    pos += 1
            else:
                pos += 1
        else:
            pos += 2
        jumps += 1
    return(jumps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
