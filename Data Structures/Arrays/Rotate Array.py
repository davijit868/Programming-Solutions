'''

Problem 189 | Rotate Array
https://leetcode.com/problems/rotate-array/

'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        temp = nums[-k:]
        for i in range(l-k-1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]
        
