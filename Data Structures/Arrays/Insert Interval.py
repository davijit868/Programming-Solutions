'''

Problem 57 | Insert Interval
https://leetcode.com/problems/insert-interval/

'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        ans = []
        inserted = False
        for interval in intervals:
            if not inserted:
                if start > interval[1]:
                    ans.append(interval)
                elif start >= interval[0]:
                    start = interval[0]
                if end < interval[0]:
                    ans.append([start, end])
                    inserted = True
                    ans.append(interval)
                elif end <= interval[1]:
                    end = interval[1]
                    ans.append([start, end])
                    inserted = True
            else:
                ans.append(interval)
        if not inserted:
            ans.append([start, end])
    
        return ans
        
