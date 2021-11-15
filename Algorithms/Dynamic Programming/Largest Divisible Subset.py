'''

Problem 368 | Largest Divisible Subset
https://leetcode.com/problems/largest-divisible-subset/

'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        max_len = 1
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0, i):
                if (nums[i] % nums[j] == 0) and (dp[j] + 1 > dp[i]):
                    dp[i] = 1 + dp[j]
                    if dp[i] > max_len:
                        max_len = dp[i]
        answer = []
        val = max_len
        for i in range(len(nums)-1, -1, -1):
            if dp[i] == val:
                if (val == max_len) or (answer[-1] % nums[i] == 0):
                    answer.append(nums[i])
                    val -= 1
        return answer
                    
