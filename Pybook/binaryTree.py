
from queue import Queue

class _BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def preoderTrav(subTree):
    if subTree is not None:
        print(subTree.data)
        preoderTrav(subTree.left)
        preoderTrav(subTree.right)

def inorderTrav(subTree):
    if subTree is not None:
        inorderTrav(subTree.left)
        print(subTree.data)
        inorderTrav(subTree.right)

def postorderTrav(subTree):
    if subTree is not None:
        postorderTrav(subTree.left)
        postorderTrav(subTree.right)
        print(subTree.Data)

def breadthFirstSearch(binThree):
    queue = Queue
    queue.enqueue(binThree)

    while not queue.isEmpty():
        # Remove the next node from it and visit
        node = queue.dequeue()
        print(node.data)

        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
