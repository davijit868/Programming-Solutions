'''

Problem 152 | Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_arr = [nums[0]]
        max_arr = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != 0:
                max_arr.append(max(min_arr[i-1]*nums[i], max_arr[i-1]*nums[i], nums[i]))
                min_arr.append(min(min_arr[i-1]*nums[i], max_arr[i-1]*nums[i], nums[i]))
            else:
                max_arr.append(nums[i])
                min_arr.append(nums[i])
        return max(max_arr)
      
