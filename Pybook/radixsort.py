from llistqueue import Queue
from array import array

def radixSort(intList, numDigit):
    binArray = array(10)
    for k in range(10):
        binArray[k] = Queue()
    
    column = 1
    for i in range(numDigit):
        for key in intList:
            digit = (key // column) % 10
            binArray[digit].enqueue(key)
    
        i = 0
        for bin in binArray:
            while not bin.isEmpty():
                intList[i] = bin.dequeue(key)
            i += 1
    
        column *= 10
        