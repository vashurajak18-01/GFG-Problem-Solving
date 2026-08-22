# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        right = head 
        while right.next is not None:
            right = right.next

        result = []
        left = head

        while left is not None and right is not None and left.data < right.data:
            sum = left.data + right.data
            if sum == target:
                result.append([left.data, right.data])
                left = left.next
                right = right.prev

            elif sum < target:
                left = left.next

            else:
                right = right.prev

        return result