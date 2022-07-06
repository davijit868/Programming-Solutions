'''

Problem 503 | Next Greater Element II 
https://leetcode.com/problems/next-greater-element-ii/

'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            flag = False
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    ans.append(nums[j])
                    flag = True 
                    break
            if not flag:
                for k in range(i):
                    if nums[k] > nums[i]:
                        ans.append(nums[k])
                        flag = True 
                        break
            if not flag:
                ans.append(-1)
        return ans
        
