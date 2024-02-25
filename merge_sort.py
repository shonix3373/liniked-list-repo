def merge_sort(list):
    """
    divide: find midpoint of the list and divide into sublists
    conqeur: recursively sort the sublists created in previous step
    combine: merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    mid_point = len(list)//2
    left = list[:mid_point]
    right = list[mid_point:]
    return (left, right)

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left(i))
            i += 1
        else:
            l.append(right(j))
            j += 1

    if i < len(left):
        l.append(left(i))
    if j < len(right):
        l.append(right(j))
