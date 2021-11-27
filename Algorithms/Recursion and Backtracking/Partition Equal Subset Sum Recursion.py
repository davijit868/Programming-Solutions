'''

Problem 416 | Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        first = []
        second = []
        def generate_pair(first, second, i):
            if len(first) + len(second) == len(nums):
                if sum(first) == sum(second):
                    return True
            while i < len(nums)-1:
                i = i+1
                first_result = generate_pair(first + [nums[i]], second, i)
                if first_result:
                    return True
                second_result = generate_pair(first, second + [nums[i]], i)
                if second_result:
                    return True
            return False
        return generate_pair(first, second, -1)
        
