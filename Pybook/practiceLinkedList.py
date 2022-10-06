from re import S

from sympy import nonlinsolve

class LinkedListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def length(self):
        si = 0
        current = self.head
        while current is not None:
            si += 1
            current = current.next
        return si
    
    def find(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def remove(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
            current = current.next
        return 'Not Found'
    
    def insert(self, data, index):
        new_node  = LinkedListNode(data)
        curr = 0
        current = self.head
        while current is not None:
            if curr == index:
                current.prev.next = new_node
                new_node.next = current
            current = current.next
            curr += 1
        return True

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end='-->')
            current = current.next
            
def main():
    mahuraan = linkedList()
    for i in range(0, 25, 2):
        mahuraan.append(i)

    print(mahuraan.find(10).data)
    print(mahuraan.remove(10))
    print(mahuraan.insert(11, 2))

    mahuraan.printList()

if __name__ == "__main__":
    main()

