''' Structure of binary tree Node 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):
        # code here
        self.diameter = 0
        def solve(node):
            if node == None:
                return 0

            leftHeight = solve(node.left)
            rightHeight = solve(node.right)
            self.diameter = max(self.diameter, leftHeight+rightHeight) 
            return 1 + max(leftHeight, rightHeight)

        solve(root)
        return self.diameter
        