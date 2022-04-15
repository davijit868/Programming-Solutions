'''

Problem 55 | Jump Game | Naive
https://leetcode.com/problems/jump-game/

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums))]
        dp[0] = True
        for i in range(len(nums)):
            jump = nums[i]
            if dp[i]:
                for j in range(i, min(i + jump + 1, len(nums))):
                    dp[j] = True
        return dp[-1]
      
