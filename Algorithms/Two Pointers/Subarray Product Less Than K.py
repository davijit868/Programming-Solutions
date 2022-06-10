'''

Problem 713 | Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/

'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and l <= r:
                product /= nums[l]
                l += 1

            res += r - l + 1

        return res
            
            
