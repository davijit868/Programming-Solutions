'''

Problem 973 | K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(point):
            return math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
        distance = []
        for point in points:
            distance.append(euclidean_distance(point))
        l = [i for i, _ in sorted(zip(points, distance), key = lambda x: x[1])]
        return l[:k]
        
