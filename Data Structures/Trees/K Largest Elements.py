'''

Problem K Largest Elements
https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1/#

'''

import heapq

class Solution:

    def kLargest(self, arr, n, k):
        ans = []
        arr = [-i for i in arr]
        
        for i in range(k):
            heapq.heapify(arr)
            temp = heapq.heappop(arr)
            ans.append(-temp)
        
        return ans

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1
