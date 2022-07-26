'''

0 - 1 Knapsack Problem
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

'''

class Solution:
    def knapSack(self, w, wt, val, n):
        if n == 0 or w == 0:
            return 0
        if wt[n-1] <= w:
            return max(val[n-1] + self.knapSack(w-wt[n-1], wt, val, n-1), self.knapSack(w, wt, val, n-1))
        elif wt[n-1] > w:
            return self.knapSack(w, wt, val, n-1)


import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
