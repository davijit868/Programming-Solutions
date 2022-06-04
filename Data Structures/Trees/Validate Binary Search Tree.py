'''

Problem 98 | Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inorder(node):
            if not node.left and not node.right:
                ans.append(node.val)
                return
            if node.left:
                inorder(node.left) 
            ans.append(node.val)
            if node.right:
                inorder(node.right) 
            
        inorder(root)
        for i in range(1, len(ans)):
            if ans[i] <= ans[i-1]:
                return False
        return True
       
