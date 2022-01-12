'''

Problem 1022 | Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        node = root
        ans = [] 
        
        def recursion(node, l):
            l.append(node.val)
            if not node.left and not node.right:  
                ans.append(l[:])
                return
            if node.left:
                recursion(node.left, l[:])
            if node.right:
                recursion(node.right, l[:])
            
        recursion(node, [])
        total = 0
        for i in ans:
            binary = "".join(list(map(str, i)))
            total += int(binary, 2)
        
        return total
      
