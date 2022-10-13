# Sorts a sequence in ascending order using the heapsort.
def heapsort(theSeq):
    n = len(theSeq)
    # Build a Max heap with in the same array
    for i in range(n):
        siftUp(theSeq, i)
    
    # Extract Each value and rebuild the heap
    for j in range(n-1, 0, -1):
        temp = theSeq[j]
        theSeq[j] = theSeq[0]
        theSeq[0] = temp
        siftDown(theSeq, j-1, 0)