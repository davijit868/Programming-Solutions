'''

Problem 47 | Permutations II
https://leetcode.com/problems/permutations-ii/

'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False for i in range(len(nums))]
        perm, answer = [], []
        
        def permute(perm, used):
            if len(perm) == len(nums) and perm[:] not in answer:
                answer.append(perm[:])
            for i in range(len(nums)):
                if used[i] == False:
                    used[i] = True
                    permute(perm + [nums[i]], used)
                    used[i] = False
            
        permute(perm, used)
        return answer
        
