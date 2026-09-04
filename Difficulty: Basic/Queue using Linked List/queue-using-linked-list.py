# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Queue class template
class myQueue:
    def __init__(self):
        # Initialize your data members
        self.front = None
        self.rear = None

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.front is None
        
    def enqueue(self, x):
        # Add element x to the rear
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):
        # Remove the front element
        if self.front is None:
            return -1
        popped = self.front.data
        self.front = self.front.next
      
        if self.front is None:
            self.rear = None
        return popped
        
    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.front is None:
            return -1
        return self.front.data

    def size(self):
        # Return current size
        count = 0 
        curr = self.front

        while curr is not None:
            count += 1
            curr = curr.next

        return count

