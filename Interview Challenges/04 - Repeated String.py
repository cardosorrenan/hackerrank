#!/bin/python3
import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_str = len(s)
    cnt_a = s.count('a') * (n // len_str)
    cnt_a += s[slice(n % len_str)].count('a')
    return(cnt_a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()

