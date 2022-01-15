'''

Problem 213 | House Robber II
https://leetcode.com/problems/house-robber-ii/

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(l):
            first, second = 0, 0
            for i in range(len(l)):
                temp = max(first + l[i], second)
                first = second
                second = temp
                print(temp)
            return second
        
        return max(nums[0], house_robber(nums[:-1]), house_robber(nums[1:]))
        
