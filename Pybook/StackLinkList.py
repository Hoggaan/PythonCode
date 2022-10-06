class _stackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an Empty Stack"
        return self._top.item

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an Empty Stack"
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item
    
    def push(self, item):
        self._top = _stackNode(item, self._top)
        self._size += 1

def isValidSource(srcfile):
    s = Stack()
    for line in srcfile:
        for token in line:
            if token in '({[':
                s.push(token)
            elif token in ')}]':
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (token == '}' and left != "}") or \
                        (token == ']' and left != ']') or \
                        (token == ')' and left != ')'):
                            return False
                            
    return s.isEmpty()





    
