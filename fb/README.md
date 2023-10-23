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
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0
        for price in prices:
            if price < low:
                low = price
            res = max(res, price - low)
        return res
        



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




