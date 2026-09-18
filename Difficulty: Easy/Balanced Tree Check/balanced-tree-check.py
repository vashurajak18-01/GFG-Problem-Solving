''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        # code here
        def solve(node):
            if node is None:
                return 0
            leftHeight = solve(node.left)

            if leftHeight == -1:
                return -1

            rightHeight = solve(node.right)

            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        x = solve(root)

        if x == -1:
            return False
        else: 
            return True