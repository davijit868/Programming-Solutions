'''
https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.

l = [1,1,2,4]
def stepPerms(n):
    for i in range(3,n+1):
        #print(i, len(l),l)
        if i >= len(l):
            l.append(l[i-1] + l[i-2] + l[i-3])
    return l[n] %  100000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
