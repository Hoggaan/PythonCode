#Implementing the Map ADT using closed hashing and probe with double hashing
from email.headerregistry import UniqueSingleAddressHeader
from multiprocessing.dummy import Array

class HashMap:
    UNUSED = None
    EMPTY = _MapEntry(None, None)
    def __init__(self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - len(self._table)//2
    
    # Returns the number of entries in the map
    def __len__(self):
        return self._count
    
    # Determines if the map contains the given key
    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None
    
    # Adds new entry to the map if the key does not exist. Otherwise, 
    # the new value replaces the current value
    def add(self, key,value):
        if key in self:
            slot = self._findSlot(key, False)
            self._table[slot].value = value
            False

        else:
            slot = self._findSlot(key, True)
            self._table[slot] = _MapEntry(key,value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True
    
    # Returns the value associated with the key
    def valueOf(self,key):
        slot = self._findSlot(key,False)
        assert slot is not None, 'Invalid Map Key'
        return self._table[slot].value
    
    # Removes Entry associated with the key
    def remove(self, key):
        pass

    # Returns an iterator for traversing the keys in the map
    def __iter__(self):
        pass

    # Finds the slot containing the key or where the key can be added 
    # forInsert indicates if the search is for an insertion, which locates
    # the slot which the new key can be added
    def _findSlot(self,key,forInsert):
        #Compute the home slot and the step size
        slot = self._hash1(key)
        step = self._hash2(key)

        M = len(self._table)
        while self._table[slot] is not UNUSED:
            if forInsert and \
                (self._table[slot] is UNUSED or self._table[slot] is EMPTY):
                return slot

            elif not forInsert and \
                (self._table[slot] is not EMPTY and self._table[slot].key == key):
                return slot
            else:
                slot = (slot + step) % M

    # Rebuilds the HashTable
    def rehash(self):
        # Create New Larger Table
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)

        #Modify the size attributes
        self._count = 0
        self._maxCount = newSize - newSize // 3

        # Add the keys from the original array to the new table
        for entry in origTable :
            if entry is not UNUSED and entry is not EMPTY:
                slot = self._findSlot(key,  True)
                self._table[slot] = entry
                self._count += 1
        
    # The main hash function for mapping keys to main hash function
    def hash1(self, key):
        return abs(hash(key)) % len(self._table)
    
    # The second hash funtion with the double probs
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table)-2)
    
# Storage class for holding key/value pairs
class _mapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    




    
    
    