''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

# class Solution:
#     def height(self, root):
        # code here
        # def solve(node):
        #     if node == None:
        #         return -1
        #     left_height = solve(node.left)
        #     right_height = solve(node.right)

        #     return 1 + max(left_height, right_height)

        # return solve(root)


class Solution:
    def height(self, root):

        if root is None:
            return -1
        
        queue = deque()
        height = 0
        
        queue.append(root)

        while len(queue) != 0:
            level_size = len(queue)
            height += 1
            
            for _ in range(level_size):
                e = queue.popleft()
                
                if e.left is not None:
                    queue.append(e.left)
                    
                if e.right is not None:
                    queue.append(e.right)
                    
        return height - 1