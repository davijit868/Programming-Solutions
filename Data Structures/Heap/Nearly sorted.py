'''

Nearly sorted 
https://practice.geeksforgeeks.org/problems/nearly-sorted-1587115620/1/#

'''

class Solution:
    def nearlySorted(self, a, n ,k):
        arr = a[:k+1]
        ans = []
        heapq.heapify(arr)
        ans.append(heapq.heappop(arr))
        for i in range(k + 1, n):
            heapq.heappush(arr, a[i])
            ans.append(heapq.heappop(arr))
        while arr:
            ans.append(heapq.heappop(arr))
            
        return ans
      
import atexit
import io
import sys
import heapq
from collections import  defaultdict

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))
