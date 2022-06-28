'''

Problem 1337 | The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        make_touple = lambda i, arr : (sum(arr), i)
        
        heap = []
        
        for i in range(len(mat)):
            heap.append(make_touple(i, mat[i]))
                    
        for i in range(k):
            heapq.heapify(heap)
            root = heapq.heappop(heap)
            ans.append(root[1])
        
        return ans
        
        
        
