import math

class Solution:
    def quadraticRoots(self, a, b, c):
        # code here
        d = b*b - (4 * a * c)
        
        if d < 0:
            return [-1]
        
        root1 = math.floor((-b + math.sqrt(d)) / (2 * a))
        root2 = math.floor((-b - math.sqrt(d)) / (2 * a))
        
        return [max(root1, root2), min( root1, root2)]