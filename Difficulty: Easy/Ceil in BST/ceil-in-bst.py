'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        ceil = -1
        while root is not None:
            if root.data == x:
                return root.data
            elif root.data < x:
                root = root.right
            else:
                ceil = root.data
                root = root.left
        return ceil