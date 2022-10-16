from re import sub


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
    
    



        
    
# Storage class for the binary tree nodes of the map
class _BTSMapNode:
    def __init__(self,key, value):
        self.key = key
        self.value = value 
        self.left = None
        self.right = None

