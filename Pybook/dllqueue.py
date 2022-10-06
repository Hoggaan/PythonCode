class DListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DLList:
    def __init__(self):
        pass

    def revTraversal(self, tail):
        curNode = tail
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.prev
    
    


