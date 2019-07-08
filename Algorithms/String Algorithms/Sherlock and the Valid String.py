#!/bin/python3
'''
Problem URL: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

''' 
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d = dict()
    l = []
    for i in s:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    print(d)

    for key,val in d.items():
        l.append(val)
    count = 0
    print(l)
    l.sort(key = l.count, reverse = True)
    print(l)
    m = l[0]
    if len(set(l)) > 2:
        return "NO"
    else:
        for i in l:
            if i != m:
                count += abs(m-i)
                if count > 1 and l.count(i) != 1 :
                    return "NO"
       
        return "YES"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
