# Sorts an array or list using the recursive quick sort algorithm
def quickSort(theSeq):
    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)

# The recursive implementation using virtual segments
def recQuickSort(theSeq, first, last):
    # Check the basecase
    if first >= last:
        return
    else:
        # save the pivot 
        pivot = theSeq[first]

        # Partion the sequence and optain the pivot position
        pos = partionSeq(theSeq, first, last)

        # repeat the process on two subsequences
        recQuickSort(theSeq, first, pos-1)
        recQuickSort(theSeq, pos+1, last)

# Partion the subsequence using the first key as a pivot
def partionSeq(theSeq, first, last):
    # Save a copy of a pivot value
    pivot = theSeq[first]

    # Find the pivot position and move the elements arround the pivot
    left = first + 1 
    right = last 

    while left <= right:
        # Find the first key larger the pivot
        while left < right and theSeq[left] < pivot:
            left +=1 
        
        # Find the last key that is smaller than the pivot 
        while right >= left and theSeq[right] >= pivot:
            right -= 1
        
        # Swap the two keys if we have not completed this partion
        if left < right:
            tmp = theSeq[left]
            theSeq[left] = theSeq[right]
            theSeq[tmp]
        
        # Put the pivot in the proper position
        if right != first:
            theSeq[first] = theSeq[right]
            theSeq[right] = pivot
    # Return the positon of the pivot
    return right


