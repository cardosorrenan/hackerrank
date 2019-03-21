#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl = 0
    vly = 0
    state = ''
    for i in range(0,len(s)):
        if s[i] == 'U': 
            lvl = lvl + 1
        else: 
            lvl = lvl - 1
          
        if lvl > 0: 
            state = 'above'
        elif lvl < 0:
            state = 'below'
        elif lvl == 0 and state == 'below':
           vly = vly + 1
           
    return vly 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
