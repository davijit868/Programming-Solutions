'''

Problem 986 | Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        max_len = max(firstList[-1][-1], secondList[-1][-1])
        first_lookup = [0 for i in range(max_len+1)]
        second_lookup = [0 for i in range(max_len+1)]
        for i in firstList:
            for j in range(i[0],i[1]+1):
                first_lookup[j] = 1
        for i in secondList:
            for j in range(i[0],i[1]+1):
                second_lookup[j] = 1
        output = []
        flag = False
        ends = []
        for i in firstList:
            ends.append(i[1])
        for i in secondList:
            ends.append(i[1])
        for i in range(max_len+1):
            if first_lookup[i] and second_lookup[i]:
                if flag == False:
                    start = i
                    flag = True
                if flag == True and (i in ends):
                    end = i
                    flag = False
                    output.append([start, end])
            elif first_lookup[i] == 0 or second_lookup[i] == 0:
                if flag == True:
                    flag = False
                    end = i - 1
                    if output[-1][-1] != end:
                        output.append([start, end])
        return output
        
