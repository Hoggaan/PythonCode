def binSearchRec(lst, target, first, last):
    if first > last:
        return False
    else:
        mid = (first + last)//2
        if lst[mid] == target:
            return True
        elif first < lst[mid]:
            binSearchRec(lst, target, first, mid-1)
        else:
            binSearchRec(lst, target, mid+1, last)

lst = [1,3,4,5,6,7,8,9,10,20,30]
print(binSearchRec(lst, 0, 0, 11))


            