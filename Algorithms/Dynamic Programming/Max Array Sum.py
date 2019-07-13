'''

https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp = []
    for i in range(len(arr)):
        if i == 0:
            dp.append(max(0,arr[i]))
        elif i == 1:
            dp.append(max(dp[i-1],arr[i]))
        else:
            dp.append(max(dp[i-2],dp[i-1],dp[i-2]+arr[i]))
    return max(dp)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
