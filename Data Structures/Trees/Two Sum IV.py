'''

Problem 653 | Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dfs = []
        def inorder(node):
            if node:
                inorder(node.left)
                dfs.append(node.val)
                inorder(node.right)
        inorder(root)
        
        first, last = 0, len(dfs) - 1
        while first < last:
            total = dfs[first] + dfs[last]
            if total == k:
                return True
            elif total < k:
                first += 1
            else:
                last -= 1
        return False
        
