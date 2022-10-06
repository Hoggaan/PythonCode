class Stack:
    def __init__(self):
        self._theItems = list()
    
    def isEmpty(self):
        return len(self)
    
    def __len__(self):
        return len(self._theItems)
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an Empty stack"
        return self._theItems[-1]
    
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an Empty Stack"
        return self._theItems.pop()
    
    def push(self, item):
        return self._theItems.append(item)
    
    
