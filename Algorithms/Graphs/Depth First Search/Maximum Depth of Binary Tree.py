'''

Problem 104 | Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                return 1 + max(dfs(node.left), dfs(node.right))
            return 0
            
        return dfs(root)
      
