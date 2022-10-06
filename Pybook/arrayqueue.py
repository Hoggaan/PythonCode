# Implementation of Queue ADT using circular Array
from array import Array
from sys import maxsize
#from sys import maxsize
class Queue:
    def __init(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array(maxSize)
    
    # Returns True if the queue is empty
    def isEmpty(self):
        return self._count == 0
    
    # Returns True if the queue is full
    def isFull(self):
        return self._count == len(self._qArray)
    
    # Returns the number of items in the queue
    def __len__(self):
        return self._count
    
    # Adds the the given item to the queue
    def enqueue(self, item):
        assert not self.isFull, 'Cannot enqueue to a full queue'
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1
    
    # Removes and returns the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot Dequeue from an empty Queue"
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self.count -= 1
        return item
    

