from collections import deque


def merge_sorted_lists(left, right):
    """
    Merge sort merging function.
    TODO: Improve, add examples."""
    result = deque()

    left = deque(left)
    right = deque(right)

    while left and right:
        if left[0] > right[0]:
            result.append(right.popleft())
        else:
            result.append(left.popleft())

    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result



def merge_2_sorted_lists(left, right):
    """
    Merge sort merging function.
    TODO: Improve, add examples."""
    result = []
    i1=0
    i2=0
    l1=len(left)
    l2=len(right)


    while i1 < l1 and l2<l2:
        if left[i1] > right[i2]:
            result.append(righ[i2])
            i2=i2+1
        else:
            result.append(left[i1])
            i1=i1+1

    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result



l1=[1,3,5]
l2=[2,4,6]
#l3=merge_sorted_lists(l1, l2)
#print l3
l4=merge_sorted_lists(l1, l2)
print l4