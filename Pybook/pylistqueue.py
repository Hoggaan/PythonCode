# Implementation of Queue ADT using python list.
class Queue:
    # Create empty Queue
    def __init__(self):
        self._qList = list()
    
    # Returns True if the Queue is empty
    def isEmpty(self):
        return len(self) == 0
    
    # Returns the number of elements in the Queue
    def __len__(self):
        return len(self._qList)
    
    # Adds the given item to the queue
    def enqueue(self, item):
        self._qList.append(item)
    
    # Removes and returns the first item in the queue
    def dequeue(self):
        return self._qList.pop(0)
    
    