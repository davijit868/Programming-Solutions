'''

https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1/?track=md-tree&batchId=144
https://ide.geeksforgeeks.org/pKRWZo58Td

'''

from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None

def build_tree(s):
    if len(s) == 0 or s[0] == 'N':
        return None
    
    ip = list(map(str, s.split()))
    print(ip)
    
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    
    q.append(root)
    size += 1
    print(q)
    
    i = 1
    while size > 0 and i < len(ip):
        curr_node = q[0]
        q.popleft()
        size -= 1
        curr_val = ip[i]
        if curr_val != 'N':
            curr_node.left = Node(int(curr_val))
            q.append(curr_node.left)
            size += 1
        i += 1
        if i > len(ip):
            break
        curr_val = ip[i]
        if curr_val != 'N':
            curr_node.right = Node(int(curr_val))
            q.append(curr_node.right)
            size += 1
        i += 1
        print(q)
    
    return root

def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(s)
        root = build_tree(s)
        print(height(root))
