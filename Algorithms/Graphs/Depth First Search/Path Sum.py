'''

Problem 112 | Path Sum
https://leetcode.com/problems/path-sum/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
            if not node.left and not node.right:
                if total == targetSum:
                    return True
                else:
                    return False
            elif node.left and node.right:
                return dfs(node.left, total + node.left.val) or dfs(node.right, total + node.right.val)
            elif node.left:
                return dfs(node.left, total + node.left.val)
            elif node.right:
                return dfs(node.right, total + node.right.val)
        if root:
            return dfs(root, root.val)
        else:
            return False
          
