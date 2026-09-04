''' Structure of linked list Node
 class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 
'''

class myStack:

    def __init__(self):
        # Initialize your data members
        self.top = None
        

    def isEmpty(self):
        # Check if the stack is empty
            return self.top is None
        

    def push(self, x):
        # Adds element x to the top of the stack
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        

    def pop(self):
        # Removes an element from the top of the stack
        if self.top is None:
            return -1
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.top is None:
            return -1
        return self.top.data

    def size(self):
        # Returns the current size of the stack
        curr = self.top
        count = 0
        
        while curr is not None:
            count += 1
            curr = curr.next
        
        return count
        
        