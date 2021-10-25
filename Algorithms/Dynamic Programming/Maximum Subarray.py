'''

https://leetcode.com/problems/maximum-subarray/

'''

class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
