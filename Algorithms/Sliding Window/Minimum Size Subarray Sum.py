'''

Problem 209 | Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: 
        left = 0
        right = 0
        total = nums[right]
        res = len(nums)
        flag = False
        while right < len(nums) and left <= right:
            if total < target:
                right += 1
                if right < len(nums):
                    total += nums[right]
            else:
                res = min(res, right - left + 1)
                flag = True
                total -= nums[left]
                left += 1
        if flag:
            return res
        else:
            return 0
        
