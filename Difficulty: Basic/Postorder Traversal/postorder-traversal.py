''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        result = []
        def postorder(node):
            if node is None:
                return None

            
            postorder(node.left)
            postorder(node.right)
            result.append(node.data)
            
        postorder(root)
        return result
        