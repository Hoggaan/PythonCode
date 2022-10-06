""" Implementation of the unpounded Priority Queue ADT using using a 
Python list with new items uppended to it's end. 
"""
from xml.etree.ElementTree import iselement


class PriorityQueue:
    # Create un empty unpounded priority queue
    def __init__(self ):
        self._qList = list()
    
    # Returns True if the queue is Empty
    def isEmpty(self):
        return len(self) == 0
    
    # Returns the number of items in the queue
    def __len__(self):
        return len(self._qList)
    
    # Adds the given item to the queue
    def enqueue(self, item, priority):
        entery = _PriorityQEntery(item, priority)
        self._qList.append(entery)
    
    # Removes and returns the first item in the queue
    def dequeue(self):
        assert self.isEmpty, 'Cannot dequeue from an Empty Queue'
        # Find the entry with the highest priority
        for i in range(len(self)):
            highest = self._qList[i].priority
            # See if the ith element contains a higher prioirity(smaller integer)
            if self._qList[i].priority < highest:
                highest = self._qList[i].priority 

        # Remove the item with the highest priority and return the item.
        entry = self._qList.pop(highest)



class _PriorityQEntery(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
    

obj = PriorityQueue()


obj.dequeue()

print(obj.__len__())