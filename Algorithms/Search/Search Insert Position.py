'''

Problem 35 | Search Insert Position
https://leetcode.com/problems/search-insert-position/

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
            
