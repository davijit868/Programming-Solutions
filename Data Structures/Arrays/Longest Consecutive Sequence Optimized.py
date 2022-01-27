'''

Problem 128 | Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        max_len = 0
        for i in nums:
            if i - 1 not in lookup:
                cur_len = 1
                idx = 1
                while i + idx in lookup:
                    cur_len += 1
                    idx += 1
                max_len = max(max_len, cur_len)
        return max_len
        
