'''

Problem 128 | Longest Consecutive Sequence | Naive
https://leetcode.com/problems/longest-consecutive-sequence/

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            maximum = max(nums)
            minimum = min(nums)
            lookup = [0 for i in range(maximum - minimum + 1)]
            for i in nums:
                lookup[i - minimum] = 1
            max_len = 1
            flag = False
            cur_len = 0
            for i in lookup:
                if i == 1:
                    cur_len += 1
                    if flag == False:
                        flag = True
                else:
                    if flag:
                        flag = False
                        if cur_len > max_len:
                            max_len = cur_len
                        cur_len = 0
            if flag:
                if cur_len > max_len:
                    max_len = cur_len
                    cur_len = 0
            return max_len
        else:
            return 0
            
