'''

Problem 207 | Course Schedule
https://leetcode.com/problems/course-schedule/

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dependency = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            course_dependency[i[0]].append(i[1])
        
        visited = [0 for i in range(numCourses)]
        def dependency_dfs(node):
            if visited[node] == 1:
                return False
            if not course_dependency[node]:
                return True
            visited[node] = 1
            for i in course_dependency[node]:
                if not dependency_dfs(i): return False
            visited[node] = 0
            course_dependency[node] = []
            return True    
        
        for i in range(numCourses):
            if not dependency_dfs(i):
                return False
        return True
    
