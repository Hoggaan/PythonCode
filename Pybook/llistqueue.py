# Implementation of Queue ADT using a linked List 
class Queue:
    # Creates an Empty Queue
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0
    
    # Returns None if the Queue is Empty
    def isEmpty(self):
        return self._qhead is None
    
    # Returns the number of items in the queue 
    def __len__(self):
        return self._count
    
    # Adds the given item to the queue
    def enqueue(self, item):
        node = _QueueNode(item)
        if self._qhead is None:
            self._qhead = node
        else:
            self._qtail.next = node
        
        self._qtail = node
        self._count += 1
    
    # Removes and Return the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), 'Cannot dequeue from an Empty queue.'
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count += 1
        return 



# Private Storage class for creating the linkedList Nodes
class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None