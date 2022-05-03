'''

Problem 209 | Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for r in range(len(nums)):
            start = 0
            while start + r < len(nums):
                total = 0
                for i in range(start, start + r + 1):
                    total += nums[i]
                if total >= target:
                    return r + 1
                start += 1
        return 0
        
