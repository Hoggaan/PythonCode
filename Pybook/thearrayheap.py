# Array based implementation of the Maxheap
from numpy import array
class MaxHeap:
    def __init__(self, maxSize):
        self._elements  = array(maxSize)
        self._count = 0
    
    # Return the number of items in the heap
    def __len__(self):
        return self._count
    
    # Return the maximum capacity of the heap
    def capacity(self):
        return len(self._elements)
    
    # Add new value to the heap
    def add(self, value):
        assert self._count < self.capacity(), " Cannot add to a full heap"
        # Add the new value to the end of the list
        self._elements[self._count] = value 
        self._count += 1
        # Sift the new value up the tree
        self._siftUp(self._count-1)
    
    # Extract the new maximum value from the heap
    def extract(self):
        assert self._count > 0, 'Cannot Extract from an empty heap'
        # Save the root value and copy the last heap value to the root
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        # Sift the root value down the treee
        self._siftDown(0)

    # Sift the value at the ndx element up the tree
    def _siftUp(self, ndx):
        if ndx > 0:
            parrent = ndx // 2
            if self._elements[ndx] > self._elements[parrent]:
                tmp = self._elements[parrent]
                self._elements[parrent] = self._elements[ndx]
                self._elements[ndx] = tmp
                self._siftUp(parrent)

    # Sift the value at the ndx value down the tree
    def _siftDown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # Determine which node contains the largest value.
        largest = ndx
        if left < self._count and self._elements[left] >= largest:
            largest = left
        elif right < self._count and self._elements[right] >= largest:
            largest = right
        # Swap
        self.swap(self._elements[ndx], self._elements[largest])
        self._siftDown(largest)
