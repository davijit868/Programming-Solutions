'''

Problem 236 | Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        def path_to_node(node, path, target):
            if node.val == target:
                ans.append(path)
                return True
            l = r = False
            if node.left:
                l = path_to_node(node.left, path + [node.left], target)
            if node.right:
                r = path_to_node(node.right, path + [node.right], target)
                
            if l or r:
                return True 
        
        path_to_node(root, [root], p.val)
        path_to_node(root, [root], q.val)
       
        max_val = root
        l = min(len(ans[0]), len(ans[1]))
        for i in range(l-1, -1, -1):
            if ans[0][i].val == ans[1][i].val:
                max_val = ans[0][i]
                break
        
        return max_val
            
