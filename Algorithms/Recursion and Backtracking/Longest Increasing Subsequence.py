'''

Problem 300 | Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        def recursion(arr, idx):
            if idx == len(nums):
                ans.append(arr[:])
                return
            if len(arr) and nums[idx] > arr[-1]:
                recursion(arr + [nums[idx]], idx + 1)
            elif not len(arr):
                recursion(arr + [nums[idx]], idx + 1)
            recursion(arr, idx + 1)
    
        recursion([], 0)
        return max(list(map(len, ans)))
        
