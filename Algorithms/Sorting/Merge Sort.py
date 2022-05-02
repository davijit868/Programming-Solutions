'''

Problem 912 | Sort an Array
https://leetcode.com/problems/sort-an-array/

'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                merge(left)
                right = arr[mid:]
                merge(right)
                l = r = k = 0
                while l < len(left) and r < len(right):
                    if left[l] <= right[r]:
                        arr[k] = left[l]
                        l += 1
                    else:
                        arr[k] = right[r]
                        r += 1
                    k += 1
                for i in range(l, len(left)):
                    arr[k] = left[i]
                    k += 1
                for i in range(r, len(right)):
                    arr[k] = right[i] 
                    k += 1

        merge(nums)
        return nums
