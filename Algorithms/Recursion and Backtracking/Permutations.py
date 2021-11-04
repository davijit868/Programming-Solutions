'''

https://leetcode.com/problems/permutations/

'''

class Solution:
    def back_track(self, result, nums, permutation, used):
        if len(permutation) == len(nums):
            result.append(permutation)
        for i in range(len(nums)):
            if used[i] == False:
                used[i] = True
                self.back_track(result, nums, permutation + [nums[i]], used)
                used[i] = False
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False for i in range(len(nums))]
        print(used)
        result = []
        permutation = []
        self.back_track(result, nums, permutation, used)
        return result
        
