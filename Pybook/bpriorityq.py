""" 
Implementation of bounded Priority Queue ADT using an array of queues in which the queues are implemented using
linked List
"""
import array
from contextlib import nullcontext
from Pybook.llistqueue import Queue

class BPriorityQueue:
    # Creates an empty bounded priority queue.
    def __init__(self, numLevels):
        self._qSize = 0
        self._qLevels = array(numLevels)
        for i in range(numLevels):
            self._qLevels[i] = Queue()
        
    # Return True if the queue is Empty
    def isEmpty(self):
        return len(self) == 0

    # Ads the given item in to the queue
    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self._qLevels), 'Invalid Priority Level'
        self._qLevels[priority].enqueue(item)
    
    # Removes and Returns the next item in the queue
    def dequeue(self):
        # Make sure that queue is not Empty
        assert not self.isEmpty(), 'Cannot Dequeue from an empty Queue'
        # Find the first non empty queue
        i = 0
        p = len(self._qLevels)
        while i < p and not self._qLevels[i].isEmpty():
            i += 1
        return self._qLevels[i].dequeue()

def main():
    obj = BPriorityQueue(5)
    obj.isEmpty()




if "__name__" == '__main__()':
    main()


class Bpritorityq:
    def __init(self, numL):
        self.size = 0
        self.qlevels = array(numL)
        for i in range(numL):
            self.qlevels[i] = Queue()
    
    def isEmpty(self):
        return len(self) == 0
    
    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self.qlevels), 'Invalid Priority Index'
        self.qlevels[priority].enqueue(item)
    
    def dequeue(self):
        assert not self.isEmpty, 'Cannot dequeue from an empty queue'
        i = 0 
        p = len(self.qlevels)
        while i < p and not self.qlevels.isEmpty():
            i + 1
        return self.qlevels[i].dequeue()
    
    



