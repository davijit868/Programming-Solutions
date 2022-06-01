'''

Problem 210 | Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c : [] for c in range(numCourses)}
        
        for pr in prerequisites:
            prereq[pr[0]].append(pr[1])
        
        output = []
        
        def find_loop(node, visited):
            if not prereq[node] and node not in output:
                output.append(node)
                return False
            for i in prereq[node]:
                if i in visited:
                    return True
                if i not in output: 
                    if find_loop(i, visited + [i]):
                        return True
                    elif i not in output:
                        output.append(i)
            if node not in output: 
                output.append(node)
            
        for i in range(numCourses):
            if i not in output:
                if find_loop(i, [i]):
                    return []
        return output
        
