'''

Problem 704 | Binary Search
https://leetcode.com/problems/binary-search/

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return answer
       
