'''

Problem 215 | Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap, result = [], None
        for num in nums:
            heapq.heappush(maxheap, -num)
        for _ in range(k):
            result = -heapq.heappop(maxheap)
        return result
          
