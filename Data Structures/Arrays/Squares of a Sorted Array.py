'''

Problem 977 | Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        if nums[0] >= 0:
            left, right = -1, 0    
        elif nums[-1] < 0:
            left, right = len(nums) - 1, len(nums)
        else:
            for i in range(1, len(nums)):
                if nums[i - 1] < 0 and nums[i] >= 0:
                    left = i - 1
                    right = i
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < nums[right]:
                ans.append(nums[left])
                left -= 1
            else:
                ans.append(nums[right])
                right += 1
        for i in range(left, -1, -1):
            ans.append(nums[i])
        for i in range(right, len(nums)):
            ans.append(nums[i])
        ans = [i*i for i in ans]
        return ans
        
