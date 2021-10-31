'''

https://leetcode.com/problems/find-all-duplicates-in-an-array/

'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate = {}
        for i in nums:
            if i not in duplicate.keys():
                duplicate[i] = 1
            else:
                duplicate[i] += 1
        result = []
        for key, value in duplicate.items():
            if value > 1:
                result.append(key)
        return result
