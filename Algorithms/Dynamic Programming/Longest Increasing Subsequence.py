'''

Problem 300 | Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for idx in range(len(nums) - 2, -1, -1):
            total = 0
            for i in range(idx + 1, len(nums)):
                if nums[idx] < nums[i]:
                    if dp[i] > total:
                        total = dp[i]
            dp[idx] = 1 + total
        
        return max(dp)
        
