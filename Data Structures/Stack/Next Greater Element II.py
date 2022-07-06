'''

Problem 503 | Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/

'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [] 
        l = len(nums)
        stack = nums[::-1]
        double_nums = nums + nums
        for i in range(l-1, -1, -1):
            flag = False
            while len(stack):
                if stack[-1] <= nums[i]:
                    stack.pop(-1)
                else:
                    flag = True
                    ans.append(stack[-1])
                    break
            if not flag:
                ans.append(-1)
            stack.append(nums[i])
        return ans[::-1]
      
