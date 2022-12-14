class _23TreeNode:
    def __init__(self, key, data):
        self.key1 = key
        self.key2 = None
        self.data1 = data
        self.data2 = None
        self.left = None
        self.middle = None
        self.right = None
    
    # Is this a leaf node
    def isAleaf(self):
        return self.left is None and self.right is None and self.middle is None
    
    #Are there two keys in this node..
    def isFull(self):
        return self.key2 is not None
    
    # Dose the node contain the given target key
    def haskey(self, target):
        if (target == self.key1) or \
            (self.key2 is not None and target == self.key2):
            return True
        else:
            return False
    
    # Returns the data associated with the target key or None
    def getData(self, target):
        if target == self.key1:
            return self.data1
        elif self.key2 is not None and target == self.key2:
            return self.data2
        else:
            return None

    # Choose the appropriate branch of the given target key
    def getBranch(self, target):
        if target < self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif target < self.key2:
            return self.middle
        else:
            return self.right
    
    



