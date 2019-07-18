'''

https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1

'''
def countLeaves(root):
    if not root: return 0
    if not root.left and not root.right: return 1
    return countLeaves(root.left) + countLeaves(root.right)
        
