'''

https://www.hackerrank.com/challenges/ctci-ransom-note/problem

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazineDict = {}
    flag = 0
    for i in magazine:
        if i not in magazineDict.keys():
            magazineDict[i] = 1
        else:
             magazineDict[i] += 1
    for i in note:
        if i in magazineDict.keys():
            magazineDict[i] -= 1
            if magazineDict[i] < 0:
                flag = 1
                print("No")
                break
        else:
            flag = 1
            print("No")
            break
    if flag == 0:
        print("Yes") 

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
