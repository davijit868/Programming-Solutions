'''

Problem 59 | Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/

'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        count = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)] 
        
        layers = (n+1)//2
        
        for layer in range(layers):
                 
            for i in range(layer,n-layer):
                matrix[layer][i] = count
                count+=1
                
            for i in range(layer+1,n-layer):
                matrix[i][n-layer-1] = count
                count+=1
                
            for i in range(n-layer-2,layer-1,-1):
                matrix[n-layer-1][i] = count
                count+=1
                
            for i in range(n-layer-2,layer,-1):
                matrix[i][layer] = count
                count+=1
                
        return matrix
