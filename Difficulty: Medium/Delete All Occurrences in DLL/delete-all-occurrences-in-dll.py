"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    def deleteAllOccurOfX(self, head, x):
        # code here
        temp = head 

        while temp is not None:
            if temp.data == x:
                if temp == head:
                    head = temp.next

                    if head:
                        head.prev = None
                else:
                    temp.prev.next = temp.next

                    if temp.next:
                        temp.next.prev = temp.prev

            temp =temp.next

        return head
