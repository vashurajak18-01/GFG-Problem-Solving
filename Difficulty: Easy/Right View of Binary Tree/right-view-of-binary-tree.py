'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def rightView(self, root):
        # code here
        ans = []
        def reverse_postOrder(node, level, ans : list):
            if node is None:
                return
            if len(ans) == level:
                ans.append(node.data)
            if node.right:
                reverse_postOrder(node.right, level + 1, ans)
            if node.left :
                reverse_postOrder(node.left, level + 1, ans)


        reverse_postOrder(root, 0 , ans)
        return ans
