'''

Problem 1046 | Last Stone Weight
https://leetcode.com/problems/last-stone-weight/

'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        ans = 0
        
        while len(stones) > 1:
            l = - heapq.heappop(stones)
            heapq.heapify(stones)
            r = - heapq.heappop(stones)
            if l > r:
                temp = l - r
            elif r > l:
                temp = r - l
            if l != r:
                heapq.heappush(stones, -temp)
        
        if stones:
            return -stones[0]
        else:
            return 0
                
