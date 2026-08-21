# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
        curr = headRef
        while curr is not None:
            if curr.prev is not None and curr.prev.data == curr.data:
                if curr.prev == headRef:
                    curr.prev = None
                    headRef = curr
                else:
                    curr.prev.prev.next = curr
                    curr.prev = curr.prev.prev

            curr = curr.next
        return headRef
       