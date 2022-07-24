'''

Problem 107 | Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        level = []
        if root:
            level.append(root)
        
        while level:
            temp = []
            for i in range(len(level)):
                curr = level.pop(0)
                temp.append(curr.val)
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
            ans.append(temp)
        
        return ans[::-1]
