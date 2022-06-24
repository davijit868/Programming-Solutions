'''

Problem 1464 | Maximum Product of Two Elements in an Array
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0
        
        for number in nums:
            
            if number > first:
                first, second = number, first
                
            else:
                second = max( number, second)
        
        return (first - 1) * (second - 1)
        
