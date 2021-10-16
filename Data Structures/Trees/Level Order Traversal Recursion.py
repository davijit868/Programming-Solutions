'''

https://www.geeksforgeeks.org/level-order-tree-traversal/

'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def print_level_order(root):
    h = height(root)
    for i in range(1, h+1):
        print_current_level(root, i)
 
def print_current_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_current_level(root.left, level-1)
        print_current_level(root.right, level-1)
 
def height(node):
    if node is None:
        return 0
    else:
        l_height = height(node.left)
        r_height = height(node.right)
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is: ")
print_level_order(root)
