'''

Problem 198 | House Robber
https://leetcode.com/problems/house-robber/

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(nums)):
            curr = max(nums[i] + first, second)
            first = second
            second = curr
        return second
        
