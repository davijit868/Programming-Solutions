'''

Problem 75 | Sort Colors
https://leetcode.com/problems/sort-colors/

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in nums:
            count[i] += 1
        
        for i in range(len(nums)):
            if i < count[0] and nums[i] != 0:
                nums[i] = 0
            elif i >= count[0] and i < count[0] + count[1] and nums[i] != 1:
                nums[i] = 1
            elif i >= count[0] + count[1] and nums[i] != 2:
                nums[i] = 2
                
