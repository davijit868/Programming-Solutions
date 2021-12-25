'''

Problem 56 | Merge Intervals
https://leetcode.com/problems/merge-intervals/

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        output = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                cur[1] = max(intervals[i][1], cur[1])
            else:
                output.append(cur)
                cur = intervals[i]
        output.append(cur)
        return output
        
