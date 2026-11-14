'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def insert(self, root: 'Node', key: int) -> 'Node':
        # code here
        if root is None:
            return Node(key)

        temp = root 

        while True:
            if key == temp.data:
                break
            if key < temp.data:
                if temp.left is None:
                    temp.left = Node(key)
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = Node(key)
                    break
                temp = temp.right

        return root