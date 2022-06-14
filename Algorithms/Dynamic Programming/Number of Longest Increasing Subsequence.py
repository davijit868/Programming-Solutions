'''

Problem 673 | Number of Longest Increasing Subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        len_list = 0
        res = 0
        
        for i in range(len(nums) - 1, -1, -1):
            max_len, max_count = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > max_len:
                        max_len, max_count = length + 1, count
                    elif length + 1 == max_len: 
                        max_count += count
            if max_len > len_list:
                len_list, res = max_len, max_count
            elif max_len == len_list:
                res += max_count
                
            dp[i] = [max_len, max_count]
                
        return res
      
