'''

Problem 912 | Sort an Array
https://leetcode.com/problems/sort-an-array/

'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def insert(pre, num, post):
            if not len(pre) or pre[-1] < num:
                pre.append(num)
                return pre + post
            else:
                temp = pre[-1]
                post = [temp] + post
                return insert(pre[:-1], num, post)    
            
        def sort(arr, idx):
            if idx == 0:
                return [arr[0]]
            temp = sort(arr, idx - 1)
            return insert(temp, arr[idx], [])
            
  
        return sort(nums, len(nums) - 1)
        
            
