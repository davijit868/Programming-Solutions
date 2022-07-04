'''

Problem 496 | Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/

'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            flag = False
            while len(stack):
                if stack[-1] < nums2[i]:
                    stack.pop(-1)
                else:
                    ans.append(stack[-1])
                    flag = True
                    break
            if not flag:
                ans.append(-1)
            stack.append(nums2[i])
      
        ans = ans[::-1]
        res = []
        for i in nums1:
            idx = nums2.index(i)
            res.append(ans[idx])
        return res
                
            
