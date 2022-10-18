class BTSMap:
    def __init__(self):
        self._root = None
        self._size = 0
    
    # Return the number of entries in the map
    def  __len__(self):
        return self._size
    
    # Return an iterator for traversing the keys in the map
    def __iter__(self):
        return _BTSMapIterator(self.root)
    # Determine if the map contains the given key
    def __contains__(self, key):
        return self._bstSearch(self._root, key) is not None
    
    # Returns the value associated with the key
    def valueOf(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, 'invalid key'
        return node.value
    
    # Helper method that recursively searchs the tree for the target key
    def _bstSearch(self, subtree, target):
        if subtree is None: # Basecase
            return None
        elif target < subtree:
            return self._bstSearch(subtree.left, target)
        elif target > subtree:
            return self._bstSearch(subtree.right, target)
        else: # Basecase
            return subtree 

    # Helper method for finding the node with the minimum key
    def _bstMinimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum(subtree.left)
    
    # Adds new entry to the map or replaces the value of existing entry
    def add(self, key, value):
        # Find the node containing the key, if it exists
        node = self._bstSearch(key)
        if node is not None:
            node.value = value
            return False
        else:
            self._root = self.bstInsert(self._root, key, value)
            self._size += 1
            return True
    
    def _bstInsert(self, subtree, key, value):
        if subtree is None:
            subtree = _BTSMapNode(key, value)
        elif subtree < subtree.key:
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif subtree > subtree.right:
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree
    
    #Delete a key from binary search tree
    def remove(self, key):
        assert key in self, 'Invalid map key'
        self._root = self._bstRemove(self._root, key)
        self._size -= 1

    # Helper method that removes an existing item recursively
    def _bstRemove(self, subtree, target):
        # Search for the item in the tree
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bstRemove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._bstRemove(subtree.right, target)
            return subtree
        # We found the node with the key
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._bstMinimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._bstRemove(subtree.right, successor.key)
                return subtree





        

# Storage class for the binary tree nodes of the map
class _BTSMapNode:
    def __init__(self,key, value):
        self.key = key
        self.value = value 
        self.left = None
        self.right = None

