'''

Problem 1337 | The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        idx = [i for i in range(len(mat))]
        for row in mat:
            ans.append(row.count(1))
        
        res = [i for _, i in sorted(zip(ans, idx), key = lambda pair: pair[0])]
        
        return res[:k]
        
        
        
