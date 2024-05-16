def merge_2_sorted_lists(left, right):
    result = []
    i1=0
    i2=0
    l1=len(left)
    l2=len(right)


    while i1 < l1 and i2<l2:
        if left[i1] > right[i2]:
            result.append(right[i2])
            i2=i2+1
        else:
            result.append(left[i1])
            i1=i1+1

    if i1 < l1:
        result.extend(left[i1:])
    if i2 < l2:
        result.extend(right[i2:])

    return result
##########    
## Test:
#########
a=[1, 3,30]
b=[2, 10, 20,40]
print(merge_2_sorted_lists(a,b))



from collections import deque

import heapq

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



 

###   merge any numbers of lists

#return a new sorted merged list from K sorted lists, each with size N.
#Initialize the heap. In Python this this is just a list.
# We need K tuples.
#     one for the index for which list among the list of lists the element lives;
#     one for the element index which is where the element lives; and the value of the element.
# Since we want the key of the heap to be based on the value of the element, we should put that first in the tuple.
# The time complexity for this would be O(KN log K), since we remove and append to the heap K * N times.

# while the heap is not empty we need to:
#  extract the minimum element from the heap: (value, list index, element index)
# if the element index is not at the last index, add the next tuple in the list index.


def merge(lists):
    merged_list = []
    # pass to heap the tuples (1st element of every list, list index, element index)
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

l1=[1,3,5]
l2=[2,4,6]
#l3=merge_sorted_lists(l1, l2)
#print l3
#l4=merge_sorted_lists(l1, l2)
#print l4
all_lists=[]
all_lists.append(l1)
all_lists.append(l2)
print all_lists

all_lists_sorted=merge(all_lists)
print all_lists_sorted
