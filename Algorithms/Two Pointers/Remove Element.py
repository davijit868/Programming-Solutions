'''

Problem 27 | Remove Element
https://leetcode.com/problems/remove-element/

'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        ans = 0
        while r < len(nums):
            if nums[r] != val:
                ans += 1
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return ans
        
