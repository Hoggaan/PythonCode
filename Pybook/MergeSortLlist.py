from hashlib import new
from turtle import left
class ListNode:
    def __self__(self, data):
        self.data = data
        self.next = None

def llistMergeSort(theList):
    if theList is None:
        return None

    # Split the linkedList into two sublists of equal size
    rightList =  _splitLinkedList(theList)
    leftList = theList

    rightList = llistMergeSort(rightList)
    leftList = llistMergeSort(leftList)

    # Merge the two ordered Sublists
    theList = _mergeLinkedLists(leftList,rightList)

    return theList


def _splitLinkedList(subList):
    midpoint = subList
    curNode = midpoint.next

    while curNode.next is not None:
        curNode = curNode.next 

        if curNode is not None:
            midpoint = midpoint.next
            curNode.next
    
    rightList = midpoint.next
    midpoint.next = None

    return rightList

def _mergeLinkedLists(leftList,rightList):
    newList = ListNode(None)
    newTail = newList

    while leftList is None and rightList is not None:
        if leftList.data <= rightList.data:
            newTail.next = leftList
            leftList = leftList.next
        else:
            newTail = rightList
            rightList = rightList.next
        
        newTail = newTail.next 
        newTail.next = None
    
    if leftList is not None:
        newTail.next = leftList
    else:
        newTail.next = rightList
    
    return newList




    