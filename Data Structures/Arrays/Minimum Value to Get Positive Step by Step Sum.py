'''

Problem 1413
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

'''

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 1
        total = 0
        for i in nums:
            total += i
            if (total + start) < 1:
                start += (1 - total - start)
        return start
      
