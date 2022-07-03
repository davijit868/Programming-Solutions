'''

K Closest Elements
https://practice.geeksforgeeks.org/problems/k-closest-elements3619/1/#

'''

import heapq

class Solution:
    def printKClosest(self, arr, n, k, x):
        if x in arr:
            arr.remove(x)

        max_heap = []
        ans = []
    
        for i in arr:
            heapq.heappush(max_heap, (-abs(i-x), i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        while max_heap:
            ans.append(heapq.heappop(max_heap)[1])
        return ans[::-1]

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1
