def msort(lst):
    if len(lst) <= 1:
        return lst
    else:
        halfway = len(lst) // 2
        lst1 = msort(lst[:halfway])
        lst2 = msort(lst[halfway:])
        new_list = merge(lst1, lst2)
    return new_list

def merge(lst1, lst2):
    new_lst = []
    lst1_tracker = 0
    lst2_tracker = 0
    while lst1_tracker < len(lst1) and lst2_tracker < len(lst2):
        if lst1[lst1_tracker] <= lst2[lst2_tracker]:
            new_lst.append(lst1[lst1_tracker])
            lst1_tracker += 1
        elif lst1[lst1_tracker] > lst2[lst2_tracker]:
            new_lst.append(lst2[lst2_tracker])
            lst2_tracker += 1
    
    while lst1_tracker < len(lst1):
        new_lst.append(lst1[lst1_tracker])
        lst1_tracker += 1
    while lst2_tracker < len(lst2):
        new_lst.append(lst2[lst2_tracker])
        lst2_tracker += 1
    return new_lst

ls = ''
lst = [42,34,3,15,32,8,84,5,6,46,98,44,24,65,73,83,4,43,34,83,43]
result =  msort(ls)
print(result)