'''

Problem 986 | Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        output = []
        while i < len(firstList) and j < len(secondList):
            if secondList[j][0] <= firstList[i][1] and firstList[i][0] <= secondList[j][1]:
                output.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return output
      
