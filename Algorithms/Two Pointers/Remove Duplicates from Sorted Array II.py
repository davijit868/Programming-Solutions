'''

Problem 80 | Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = False
        ans = 0
        l, r = 1, 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                if not flag:
                    flag = True
                    nums[l] = nums[r]
                    l += 1
                else:
                    ans += 1
            else:
                nums[l] = nums[r]
                flag = False
                l += 1
            r += 1
        return len(nums) - ans
            
