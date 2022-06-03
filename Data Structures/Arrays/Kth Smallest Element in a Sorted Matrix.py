'''

Problem 378 | Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = []
        for i in matrix:
            flat.extend(i)
        flat.sort()
        return flat[k-1]
      
