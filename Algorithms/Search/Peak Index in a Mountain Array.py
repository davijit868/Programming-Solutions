'''

Problem 852 | Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            elif arr[mid - 1] < arr[mid] and arr[mid + 1] > arr[mid]:
                left = mid + 1
            elif arr[mid - 1] > arr[mid] and arr[mid + 1] < arr[mid]:
                right = mid - 1
                
        
