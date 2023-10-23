### System design 

https://habr.com/ru/articles/769018/ event driving arc

https://github.com/ByteByteGoHq/system-design-101

https://habr.com/ru/companies/otus/articles/765014/

https://www.youtube.com/watch?v=mCM6QVHD08c

https://habr.com/ru/companies/otus/articles/764902/ Redis Memcahed

https://www.youtube.com/watch?v=o5n85GRKuzk Design Twitter - System Design Interview

https://systemdesign.one/system-design-interview-cheatsheet/

https://www.youtube.com/watch?v=_K-eupuDVEc  Google system design interview: Design Spotify


https://engineering.fb.com/2023/06/27/developer-tools/meta-developer-tools-open-source/

https://www.youtube.com/watch?v=GLTR39VIAdc Datas Structures and Algo

https://habr.com/ru/companies/otus/articles/764680/  recommendation system

https://habr.com/ru/companies/otus/articles/764222/  recommendation system


### Leetcode
https://walkccc.me/LeetCode/ Solutions

https://dxmahata.gitbooks.io/leetcode-python-solutions/content/

https://github.com/ChenglongChen/LeetCode-3/tree/master/Python

https://www.algoexpert.io/ I bought it!

### Find all triplets with 0 sum

```
def findTriplets(arr, n):
 
    found = False
 
    # sort array elements
    arr.sort()
 
    for i in range(0, n-1):
 
        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
 
            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True
 
            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l += 1
 
            # if sum is greater than zero then
            # decrement in right side
            else:
                r -= 1
 
    if (found == False):
        print(" No Triplet Found")
 
 
# Driven source
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)
```

### Search in rotated array

```
def binary_search(arr, start, end, key):
  # assuming all the keys are unique.
  
  if (start > end):
    return -1;

  mid = int(start + (end - start) / 2)

  if arr[mid] == key:
    return mid
    
  if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
    return binary_search(arr, start, mid - 1, key)
  
  elif arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]: 
    return binary_search(arr, mid + 1, end, key)

  elif arr[end] <= arr[mid]:
    return binary_search(arr, mid + 1, end, key)

  elif arr[start] >= arr[mid]:
    return binary_search(arr, start, mid - 1, key)

  return -1;

def binary_search_rotated(arr, key):
  return binary_search(arr, 0, len(arr)-1, key)

v1 = [6, 7, 1, 2, 3, 4, 5];
  
print("Key(3) found at: " + str(binary_search_rotated(v1, 3)))
print("Key(6) found at: " + str(binary_search_rotated(v1, 6)))
  
v2 = [4, 5, 6, 1, 2, 3];
  
print("Key(3) found at: " + str(binary_search_rotated(v2, 3)))
print("Key(6) found at: " + str(binary_search_rotated(v2, 6)))
```

### Find the high and low index in sorted array with duplicates
```
def find_low_index(arr, key):
  
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:

    mid_elem = arr[mid]

    if mid_elem < key:
      low = mid + 1
    else:
      high = mid - 1

    mid = low + int((high - low) / 2)

  if low < len(arr) and arr[low] == key:
    return low

  return -1

def find_high_index(arr, key):
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:
    mid_elem = arr[mid]

    if mid_elem <= key:
      low = mid + 1
    else:
      high = mid - 1

    mid = low + int((high - low) / 2);
  
  if high == -1:
    return high

  if high < len(arr) and arr[high] == key:
    return high

  return -1


array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 5
low = find_low_index(array, key)
high = find_high_index(array, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))

key = -2
low = find_low_index(array, key)
high = find_high_index(array, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))
```

### Find all possible subsets (2**n)
```
n = size of given integer set
subsets_count = 2^n
for i = 0 to subsets_count
    form a subset using the value of 'i' as following:
        bits in number 'i' represent index of elements to choose from original set,
        if a specific bit is 1 choose that number from original set and add it to current subset,
        e.g. if i = 6 i.e 110 in binary means that 1st and 2nd elements in original array need to be picked.
    add current subset to list of all subsets


def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
      return 0
    return 1
        
def get_all_subsets(v, sets):
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
      st = set([])
      for j in range(0, len(v)):
         if get_bit(i, j) == 1:
            st.add(v[j])
      sets.append(st)
      
def main():
    v = [8,13,3,22,17,39,87,45,36]
    subsets = []
    get_all_subsets(v, subsets);
    print("****Total*****" + str(len(subsets)))
    for i in range(0, len(subsets)):
        print("{", end = "")
        print(subsets[i], end = "")
        print("}")
    print("****Total*****" + str(len(subsets)))

main()  

```

### Graphs: Clone a directed graph
```
from directed_graph import *

def clone_rec(root, graph, nodes_completed):
  # Base case when there is no node
  if not root:
    return None

  # Creating new vertex/node
  pNew = Node(root.data)

  # Using hashmap to keep track of visited nodes
  nodes_completed[root] = pNew

  # Adding new vertex in the graph
  graph.add_vertex_in_nodes(pNew)

  # Iterate over each neighbor of the current vertex/node
  for p in root.neighbors:
    x = nodes_completed.get(p)
    if not x:
      # If node is not visited call recursive function to create vertex/node
      pNew.neighbors.append(clone_rec(p, graph, nodes_completed))
    else:
      # If node is visited just add it to the neighbors of current vertex/node
      pNew.neighbors.append(x)
  return pNew

def clone(graph):
  # Hashmap to keep record of visited nodes
  nodes_completed = {}
  
  # Creating new graph
  clone_graph = DirectedGraph()
  
  # clone_rec function call
  # Passing first node as root node
  
  if not graph.nodes:
    return None
  else:
    clone_rec(graph.nodes[0], clone_graph, nodes_completed)

  # Return deep copied graph
  return clone_graph

def main():
  # Main start from here
  g1 = DirectedGraph()

  print("------------   EXAMPLE # 1    -----------")
  # Adding verteces/nodes
  g1.add_vertex(0)
  g1.add_vertex(1)
  g1.add_vertex(2)
  g1.add_vertex(3)
  g1.add_vertex(4)

  # Adding edges of vertex/node 0
  g1.add_edge(0, 2)
  g1.add_edge(0, 3)
  g1.add_edge(0, 4)

  # Adding edges of vertex/node 1
  g1.add_edge(1, 2)

  # Adding edges of vertex/node 2
  g1.add_edge(2, 0)

  # Adding edges of vertex/node 3
  g1.add_edge(3, 2)

  # Adding edges of vertex/node 4
  g1.add_edge(4, 1)
  g1.add_edge(4, 3)
  g1.add_edge(4, 0)

  # Printing graph

  print("Original graph (before copy): ")
  print(g1)

  g1_copy = clone(g1)
  print("Cloned graph (after copy):")
  print(g1_copy)

  print("\nOriginal graph (after deleting an edge [0->2]):")
  g1.delete_edge(0, 2)
  print(g1)

  print("\nCloned graph (after deleting an edge [0->2] from original the graph): ")
  print(g1_copy)

  g2 = DirectedGraph()

  # Adding verteces/nodes

  print("\n\n------------   EXAMPLE # 2    -----------")
  g2.add_vertex("v1")
  g2.add_vertex("v2")
  g2.add_vertex("v3")
  g2.add_vertex("v4")
  g2.add_vertex("v5")

  g2.add_edge("v1", "v2")
  g2.add_edge("v1", "v3")
  g2.add_edge("v1", "v4")

  g2.add_edge("v2", "v1")
  g2.add_edge("v2", "v3")
  g2.add_edge("v2", "v4")

  g2.add_edge("v3", "v1")
  g2.add_edge("v3", "v2")
  g2.add_edge("v3", "v4")
  g2.add_edge("v3", "v5")

  g2.add_edge("v4", "v1")
  g2.add_edge("v4", "v2")
  g2.add_edge("v4", "v3")
  g2.add_edge("v4", "v5")

  g2.add_edge("v5", "v3")

  print("Original graph (before copy):")
  print(g2)

  g2_copy = clone(g2)
  print("\nCloned graph (after copy):")
  print(g2_copy)


  print("\nOriginal graph (after deleting an edge [v5->v3]):")
  g2.delete_edge("v5", "v3")
  print(g2)

  print("\nCloned graph (after deleting an edge [v5->v3] from original the graph): ")
  print(g2_copy)

if __name__ == '__main__':
  main()
```

### String segmentation
Given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary. 

 ```
def can_segment_string(s, dictionary):
  for i in range(1, len(s) + 1):
    first = s[0:i]
    if first in dictionary:
      second = s[i:]
      if not second or second in dictionary or can_segment_string(second, dictionary):
        return True
  return False
  
s = "hellonow";
dictionary= set(["hello","hell","on","now"])
if can_segment_string(s, dictionary):
  print("String Can be Segmented")
else:
  print("String Can NOT be Segmented")
```

### Reverse words in sentense
Reverse the order of words in a given sentence (an array of characters).

```
def str_rev(str, start, end):
  if str == None or len(str) < 2:
    return

  while start < end:
    temp = str[start]
    str[start] = str[end]
    str[end] = temp

    start += 1
    end -= 1


def reverse_words(sentence):

  # Here sentence is a null-terminated string ending with char '\0'.

  if sentence == None or len(sentence) == 0:
    return

  #  To reverse all words in the string, we will first reverse
  #  the string. Now all the words are in the desired location, but
  #  in reverse order: "Hello World" -> "dlroW olleH".

  str_len = len(sentence)
  str_rev(sentence, 0, str_len - 1)

  # Now, let's iterate the sentence and reverse each word in place.
  # "dlroW olleH" -> "World Hello"

  start = 0
  end = 0

  while True:

  # find the  start index of a word while skipping spaces.
    while start < len(sentence) and sentence[start] == ' ':
      start += 1

    if start == str_len:
      break

  # find the end index of the word.
    end = start + 1
    while end < str_len and sentence[end] != ' ':
      end += 1

  # let's reverse the word in-place.
    str_rev(sentence, start, end - 1)
    start = end


def get_array(t):
  s = array('u', t)
  return s


def print_array(s):
  i = 0
  while i != len(s):
    stdout.write(s[i])
    i += 1
  print ()


s = get_array('Hello World!')
print_array(s)
reverse_words(s)
print_array(s)
```

### Move zeros to left in place  
https://www.educative.io/blog/cracking-top-facebook-coding-interview-questions
```
Keep two markers: read_index and write_index and point them to the end of the array.  

While moving read_index towards the start of the array:

If read_index points to 0, skip.
If read_index points to a non-zero value, write the value at read_index to write_index and decrement write_index.
Assign zeros to all the values before the write_index and to the current position of write_index as well.

def move_zeros_to_left(A):
  if len(A) < 1:
    return

  lengthA = len(A)
  write_index = lengthA - 1
  read_index = lengthA - 1

  while(read_index >= 0):
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      write_index -= 1

    read_index -= 1

  while(write_index >= 0):
    A[write_index]=0;
    write_index-=1
    
v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)
```
### Merge overlapping intervals

```
class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second

def merge_intervals(v):
  if v == None or len(v) == 0 :
    return None

  result = []
  result.append(Pair(v[0].first, v[0].second))

  for i in range(1, len(v)):
    x1 = v[i].first
    y1 = v[i].second
    x2 = result[len(result) - 1].first
    y2 = result[len(result) - 1].second

    if y2 >= x1:
      result[len(result) - 1].second = max(y1, y2)
    else:
      result.append(Pair(x1, y1))

  return result;

v = [Pair(1, 5), Pair(3, 1), Pair(4, 6), 
     Pair(6, 8), Pair(10, 12), Pair(11, 15)]

result = merge_intervals(v)

for i in range(len(result)):
  print("[" + str(result[i].first) + ", " + str(result[i].second) + "]", end =" ")

```

### Binary tree
https://towardsdatascience.com/4-types-of-tree-traversal-algorithms-d56328450846

### Serialize/desiarilize binary tree

We’ll use a pre-order traversal here. We’ll also serialize some markers to represent a null pointer to help deserialize the tree.
```
from binary_tree import *
from binary_tree_node import *

# Initializing our marker as the max possible int value
MARKER = float('inf')

def serialize_rec(node, stream):
    # Adding marker to stream if the node is None
    if (node == None):
        stream.append(MARKER)
        return
   
    # Adding node to stream
    stream.append(node.data)

    # Doing a pre-order tree traversal for serialization
    serialize_rec(node.left, stream)
    serialize_rec(node.right, stream)

# Function to serialize tree into list of integer.
def serialize(root):
    stream = []
    serialize_rec(root, stream)
    return stream

# Function to deserialize integer list into a binary tree.
def deserialize(stream):
    # dequeue first element form list
    val = stream.pop(0)

    # Return None when a marker is encountered
    if (val == MARKER):
        return None

    # Creating new Binary Tree Node from current value from stream
    node = BinaryTreeNode(val)

    # Doing a pre-order tree traversal for serialization
    node.left = deserialize(stream)
    node.right = deserialize(stream)

    # Return node if it exists
    return node

def main():
    input1 = [100, 50, 200, 25, 75, 350]
    tree1 = BinaryTree(input1)
    orgTree1 = tree1.get_tree_deep_copy()

    tree2 = BinaryTree(100)
    tree2.insert_bt(200)
    tree2.insert_bt(75)
    tree2.insert_bt(50)
    tree2.insert_bt(25)
    tree2.insert_bt(350)
    orgTree2 = tree2.get_tree_deep_copy()


    tree3 = BinaryTree(200)
    tree3.insert_bt(350)
    tree3.insert_bt(100)
    tmp = tree3.find_in_BT(350)
    tmp.right = BinaryTreeNode(75)
    tmp.right.right = BinaryTreeNode(50)
    tmp = tree3.find_in_BT(100)
    tmp.left = BinaryTreeNode(25)
    orgTree3 = tree3.get_tree_deep_copy()

    
    input4 = [100, 50, 200, 25, 75, 350]
    input4.sort()
    tree4 = BinaryTree(input4)
    orgTree4 = tree4.get_tree_deep_copy()
    

    input5 = reversed(input4)
    tree5 = BinaryTree(input5)
    orgTree5 = tree5.get_tree_deep_copy()
    

    tree6 = BinaryTree(100)
    orgTree6 = tree6.get_tree_deep_copy()

    # Defining test cases
    inputs = [tree1.root, tree2.root, tree3.root,
                       tree4.root, tree5.root, tree6.root, None]

    original_trees =[orgTree1, orgTree2, orgTree3, orgTree4, orgTree5, orgTree6, None]

    for i in range(len(inputs)):
        if (i > 0):
            print("\n")
        
        print(str(i + 1) + ".\tBinary tree:")
        if (original_trees[i] == None):
            display_tree(None)
        else:
            display_tree(original_trees[i].root)
        
        print("\n\tMarker used for NULL nodes in serialization/deserialization: " + str(MARKER))
        
        # Serialization
        ostream = serialize(inputs[i])
        print("\n\tSerialized integer list:")
        print("\t" + str(ostream))

        # Deserialization
        deserialized_root = deserialize(ostream)
        print("\n\tDeserialized binary tree:")
        display_tree(deserialized_root)
        print("----------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    main()
```

### Convert binary tree to double linked list 
```
from binary_tree import *
from binary_tree_node import *

# Initializing the first and the last nodes
first = None
last = None


def convert_to_linked_list_rec(curr_node):
    global first
    global last

    # Return if the current node is None
    if not curr_node:
        return
    else:
        # Performing in-order tree traversal
        convert_to_linked_list_rec(curr_node.left)

        if last:
            # Connecting the last and current nodes
            last.right = curr_node
            curr_node.left = last
        else:
            # Initializing the first node
            first = curr_node

        # Updating the current node
        last = curr_node
        convert_to_linked_list_rec(curr_node.right)


def convert_to_linked_list(root):
    global first
    global last

    if not root:
        # Return null if the root doesn't exist
        return None
    else:
        first = None
        last = None
        convert_to_linked_list_rec(root)

        # Closing the linked list
        last.right = None
        first.left = None
        return first


def main():
    input1 = [100, 50, 200, 25, 75, 125, 350]
    tree1 = BinaryTree(input1)

    tree2 = BinaryTree(100)
    tree2.insert(50)
    tree2.insert(200)
    tree2.insert(25)
    # Add a node at an incorrect position
    tree2.insert_bt(110)
    tree2.insert(125)
    tree2.insert(350)

    tree3 = BinaryTree(100)
    tree3.insert(50)
    tree3.insert(200)
    tree3.insert(25)
    tree3.insert(75)
    # Add a node at an incorrect position
    tree3.insert_bt(90)
    tree3.insert(350)

    input4 = [100, 50, 200, 25, 75, 125, 350]
    input4.sort()
    tree4 = BinaryTree(input4)

    input5 = reversed(input4)
    tree5 = BinaryTree(input5)

    tree6 = BinaryTree(100)

    # Defining test cases
    test_case_roots = [tree1.root, tree2.root, tree3.root,
                       tree4.root, tree5.root, tree6.root, None]

    for i in range(len(test_case_roots)):
        if i > 0:
            print()
        print(str(i + 1) + ".\tBinary tree:")
        display_tree(test_case_roots[i])

        print("\n\tDoubly Linked List:")
        get_dll_list(convert_to_linked_list(test_case_roots[i]))
        print("----------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
```

### 

### Tree level order traversal

Given the root of a binary tree, display the node values at each level. Node values for all levels should be displayed on separate lines. 
```
Here, you are using two queues: current_queue and next_queue. You push the nodes in both queues alternately based on the current level number. You’ll dequeue nodes from the current_queue, print the node’s data, and enqueue the node’s children to the next_queue.

Once the current_queue becomes empty, you have processed all nodes for the current level_number. To indicate the new level, print a line break (\n), swap the two queues, and continue with the above-mentioned logic.

After printing the leaf nodes from the current_queue, swap current_queue and next_queue. Since the current_queue would be empty, you can terminate the loop.
```

```
from collections import deque
from binary_tree import *
from binary_tree_node import *

# Using two queues
def level_order_traversal(root):
    #   We print None if the root is None
    if not root:
        print("None", end="")
    else:
        result = ""
        
        # Declaring an array of two queues
        queues = [deque(), deque()]

        # Initializing the current and next queues
        current_queue = queues[0]
        next_queue = queues[1]

        # Enqueuing the root node into the current queue and setting
        # level to zero   
        current_queue.append(root)
        level_number = 0

        # Printing nodes in level-order until the current queue remains
        # empty
        while current_queue:
            # Dequeuing and printing the first element of queue
            temp = current_queue.popleft()
            print(str(temp.data), end="")
            result += str(temp.data) + ""

            # Adding dequeued node's children to the next queue
            if temp.left:
                next_queue.append(temp.left)

            if temp.right:
                next_queue.append(temp.right)

            # When the current queue is empty, we increase the level, print a new line
            # and swap the current and next queues   
            if not current_queue:
                level_number += 1
                if next_queue:
                    print(" : ", end="")
                current_queue = queues[level_number % 2]
                next_queue = queues[(level_number + 1) % 2]
            else:
                print(", ", end="")

def main():
    # Creating a binary tree
    input1 = [100, 50, 200, 25, 75, 350]
    tree1 = BinaryTree(input1)

    # Creating a right degenerate binary tree
    input2 = sorted(input1)
    tree2 = BinaryTree(input2)

    # Creating a left degenerate binary tree
    input2.reverse()
    tree3 = BinaryTree(input2)

    # Creating a single node binary tree
    tree4 = BinaryTree(100)

    test_case_roots = [tree1.root, tree2.root, tree3.root, tree4.root, None]
    test_case_statements = ["Level-Order Traversal of a normal binary search tree: ",
            "Level-Order Traversal of a right degenerate binary search tree: ",
            "Level-Order Traversal of a left degenerate binary search tree: ",
            "Level-Order Traversal of a single node binary tree: ",
            "Level-Order Traversal of a null tree: "]

    for i in range(len(test_case_roots)):
        if (i > 0):
            print()
        print(str(i + 1) + ". Binary Tree:")
        display_tree(test_case_roots[i])
        print("\n   " + test_case_statements[i],end="\n   ")

        # Printing the in-order list using the method we just implemented
        level_order_traversal(test_case_roots[i])
        print("\n-------------------------------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    main()
```
### Yet another level order traversal
```
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = deque()
        d.append(root)
        res = []
        while d:
            level = []
            for i in range(len(d)):
                node = d.popleft()
                level.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(level)
        return res
```
 
#### breadth-first = lever order

#### depth-first has 3 variations:
```
in-order:  left subtree, current node, right subtree  (for Binary Search Tree it gives nodes in sorted manner)
pre-order: current node, left subtree, right subtree
post-order: left subtree, right subtree, current node
```
### Compare is 2 trees are the same
```
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
 ```       

#### max depth
```
def maxDepth(root):
 
   if not root return 0
   return max(maxDepth(root.right),  maxDepth(root.left)) + 1

```
### Binary tree diameter

https://www.youtube.com/watch?v=X7_5fYEVIIU&list=PLQZEzAa9dfpkv0kZkjomTj553gQyafNiB&index=16


### Invert binary tree
https://www.youtube.com/watch?v=4kRn1xlDJlY&list=PLQZEzAa9dfpkv0kZkjomTj553gQyafNiB&index=11
```
def helper(root):
  if not root: return None
  helper(root.left)
  helper(root.right)

  # current node:
  tmp = root.left
  root.left = root.right
  root.right = tmp



def invert(root):
    helper(root)
    return root
```

### Binary Tree Maximum Path Sum
https://github.com/hotsno/blind-75/blob/main/solutions
```
class Solution:
    res = float('-inf')
----------------------------
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res
---------------------
    def helper(self, root):
        if not root:
            return 0
        left, right = self.helper(root.left), self.helper(root.right)
        path_max = max(root.val, root.val + left, root.val + right)
        self.res = max(self.res, path_max, root.val + left + right)
        return path_max
```

### Brackets:
```
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in "([{":
                stack.append(c)
            if c in ")]}":
                if len(stack) == 0:
                    return False
                if d[c] != stack.pop():
                    return False
        return len(stack) == 0
```

### min # of removes to make string  with parenteses valid
 https://www.youtube.com/watch?v=PDO3vvly7eU
```
 def min_removes(s):
    incidesToRemove = set()
    stack=list()
    for i, c in enumerate(s):
       if c == '(':
          stack.append(c)
       elif c == ')':
          if stack: incidesToRemove.add(i)
          else: stack.pop()
     while stack:
          incidesToRemove.add(stack.pop())

     result = list() 
     for i in range(len(s)-1):
         if i not in ncidesToRemove:
         result.append(s[i])
     return result
       


```


3sum a+b+c

all permutations of string without recursion


### Buy /Sell Stock
```
def find_buy_sell_stock_prices(array):
  if array == None or len(array) < 2:
    return None

  current_buy = array[0]
  global_sell = array[1]
  global_profit = global_sell - current_buy

  current_profit = float('-inf')

  for i in range(1, len(array)):
    current_profit = array[i] - current_buy

    if current_profit > global_profit:
      global_profit = current_profit
      global_sell = array[i]

    if current_buy > array[i]:
      current_buy = array[i];

  result = global_sell - global_profit, global_sell                 
   
  return result

array = [1, 2, 3, 4, 3, 2, 1, 2, 5]  
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))

array = [8, 6, 5, 4, 3, 2, 1]
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))
```

Yet another solution 
```
    def maxProfit(self, prices):
        low = prices[0]
        res = 0
        for price in prices:
            if price < low:
                low = price
            res = max(res, price - low)
        return res
   ```     



### Return K most frequent elements in the list IN ANY ORDER

#####  Use the counter function to count the elements
```
from collections import Counter
def topKFrequent(self, nums, k):

      count = Counter(nums)  # builds the dict: item: frequency
      return [c[0] for c in count.most_common(k)]
```


#####   Use a max heap
```
from collections import Cunter

def topKFrequent(self, nums, k):
      count = Counter(nums)
      heap = []
      ans = []

      for i in count:
        heappush(heap, (-count[i], i))

      while k:
        ans.append(heappop(heap)[1])
        k -= 1

      return ans
```
### Blind 75 LeetCode questions refer to a curated list of the 75 most frequently asked LeetCode algorithms questions. 

 https://github.com/david-legend/python-algorithms/

 https://github.com/hotsno/blind-75/tree/main/solutions

https://github.com/abhimathore/Grind-75



https://github.com/redayzarra/leetcode

 


I bought it:
https://www.udemy.com/course/blind-75-leetcode-questions-ace-algorithms-coding-interview/learn/lecture/37964360#overview

https://www.youtube.com/watch?v=em4EP-IiKac

https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf blind-75 solutions


https://medium.com/codex/leetcode-167-two-sum-ii-input-array-is-sorted-python-solution-daa49d13215f

### Interview questions

https://www.youtube.com/playlist?list=PLQZEzAa9dfpkv0kZkjomTj553gQyafNiB  Solving All 150 NeetCode Problems

https://www.youtube.com/watch?v=GcW4mgmgSbw  Sliding windows

https://www.youtube.com/watch?v=EM8IgIIiOdY

https://www.youtube.com/watch?v=DDRo29ptFwE

https://www.youtube.com/watch?v=xF554Tlzo-c  I solved 541 Leetcode problems. But you need only 150.

https://www.youtube.com/watch?v=kp3fCihUXEg

https://www.youtube.com/watch?v=SVvr3ZjtjI8&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_

https://habr.com/ru/articles/764718/  leetcode


#### Compress string 1:

```
def rle_encode(data: str) -> str: 
    encoded = [] 
    i = 0 
    while i <= len(data)-1: 
        count = 1 
        ch = data[i] 
        j = i 
        while j < len(data) - 1: 
            if data[j] == data[j+1]: 
                count = count+1 
                j = j + 1
            else:
                break
        encoded.append(str(count) + ch)
        i = j + 1
    return "".join(encoded)
```
### Compress string 2:
```
from itertools import groupby

def rle_encode(data: str) -> str:
    return "".join(str(len(list(group_items))) + key
        for key, group_items in groupby(data))

```




