### Tree
Breadth-first traversal (aka  level order traversal)  and Depth-first traversals

Breadth-first traversal: This involves traversing the tree level by level, visiting all the nodes at a given level before moving on to the next level.  
Breadth-first traversal is also known as level order traversal.
```python
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first_traversal(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
breadth_first_traversal(root) 
# Output: 1 2 3 4 5
```
In the above example, breadth_first_traversal function takes a root node of a tree, and using a queue, 
it visits all the nodes at a given level before moving on to the next level. 

The function uses a deque from the collections module, 
it appends the root to the queue and while the queue is not empty, it pops the leftmost element, prints it and appends its children to the queue. 
The example tree is a simple binary tree where each node has at most two children. 

It's worth noting that if the tree was a graph with unordered edges, you would have to keep track of the visited nodes to avoid infinite loop.


### Depth-first traversal: 3 possible ways:
 
#### In-order traversal: visits the left subtree, then the root, and then the right subtree.
```python
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)
```        
#### Pre-order traversal: visits the root, then the left subtree, and then the right subtree.
```python
def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)
```        
#### Post-order traversal: visits the left subtree, then the right subtree, and then the root.
```python
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')
```
### Autocompletion
 Program to demonstrate auto-complete feature using Trie data structure.
 This is a basic implementation of Trie and not the most optimized one.
```python
class TrieNode():
	def __init__(self):
		# Initialising one node for trie
		self.children = {}
		self.last = False


class Trie():
	def __init__(self):

		# Initialising the trie structure.
		self.root = TrieNode()

	def formTrie(self, keys):

		# Forms a trie structure with the given set of strings
		# if it does not exists already else it merges the key
		# into it by extending the structure as required
		for key in keys:
			self.insert(key) # inserting one key to the trie.

	def insert(self, key):

		# Inserts a key into trie if it does not exist already.
		# And if the key is a prefix of the trie node, just
		# marks it as leaf node.
		node = self.root

		for a in key:
			if not node.children.get(a):
				node.children[a] = TrieNode()

			node = node.children[a]

		node.last = True

	def suggestionsRec(self, node, word):

		# Method to recursively traverse the trie
		# and return a whole word.
		if node.last:
			print(word)

		for a, n in node.children.items():
			self.suggestionsRec(n, word + a)

	def printAutoSuggestions(self, key):

		# Returns all the words in the trie whose common
		# prefix is the given key thus listing out all
		# the suggestions for autocomplete.
		node = self.root

		for a in key:
			# no string in the Trie has this prefix
			if not node.children.get(a):
				return 0
			node = node.children[a]

		# If prefix is present as a word, but
		# there is no subtree below the last
		# matching node.
		if not node.children:
			return -1

		self.suggestionsRec(node, key)
		return 1


# Driver Code
keys = ["hello", "dog", "hell", "cat", "a",
		"hel", "help", "helps", "helping"] # keys to form the trie structure.
key = "h" # key for autocomplete suggestions.

# creating trie object
t = Trie()

# creating the trie structure with the
# given set of strings.
t.formTrie(keys)

# autocompleting the given key using
# our trie structure.
comp = t.printAutoSuggestions(key)

if comp == -1:
	print("No other strings found with this prefix\n")
elif comp == 0:
	print("No string found with this prefix\n")

# This code is contributed by amurdia and muhammedrijnas

```

### Find islands on 2D grid
```python
def num_islands(grid):
    # Function to perform DFS to mark all connected cells as visited
    def dfs(x, y):
        # Check if the current cell is within bounds and is a 1
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return

        # Mark the current cell as visited (change 1 to 0)
        grid[x][y] = 0

        # Visit all neighboring cells
        dfs(x + 1, y)  # Down
        dfs(x - 1, y)  # Up
        dfs(x, y + 1)  # Right
        dfs(x, y - 1)  # Left

    if not grid or not grid[0]:
        return 0

    num_islands = 0

    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell is a 1, it's part of an island
            if grid[i][j] == 1:
                num_islands += 1  # Increment the island count
                dfs(i, j)  # Perform DFS to mark the entire island as visited

    return num_islands

# Example usage
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

print("Number of islands:", num_islands(grid))

```

### Brackets matching
```python
class Solution:
    def isValid(self, s: str) -> bool:     
        stack = []
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in '([{':  #  if char in brackets.keys()
                stack.append(char)
            elif char in ')]}': #  if char in brackets.values()
                if len(stack) == 0 or brackets[char] != stack.pop():
                    return False

        return len(stack) == 0
```

```python
def longest_increasing_subsequence(nums):
    """
    Finds the longest strictly increasing subsequence in a list of numbers.

    Args:
        nums (list): A list of integers or floats.

    Returns:
        list: The longest strictly increasing subsequence.
    """
    if not nums:
        return []

    # Initialize variables to track sequences
    longest_seq = []
    current_seq = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_seq.append(nums[i])  # Continue the increasing sequence
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq  # Update the longest sequence
            current_seq = [nums[i]]  # Start a new sequence

    # Final check after the loop
    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq

    return longest_seq
```

### Longest increasing subsequence

https://llego.dev/posts/python-solving-longest-increasing-subsequence/

```python
def findLISLength(arr):

  LIS = [1 for _ in range(len(arr))]

  for i in range(1, len(arr)):
    for j in range(i):
      if arr[i] > arr[j]:
        LIS[i] = max(LIS[i], LIS[j] + 1)

  return max(LIS)

O(n**2)
```
#### Better solution:
 
Initialize with stack containing first array element  
For each subsequent element, try to append to existing stacks if order is maintained  
If no stack append is possible, make new stack with that element  
Track longest stack found to get LIS length  
This leverages Python’s deque to simulate the stacks in an efficient way.  
By greedily extending stacks that maintain order, we build up the LIS with just one array pass.  

The time complexity is O(n log n) due to the stack manipulations,   
making this a fast optimization over the dynamic programming approach.

```python
from collections import deque

def findLISLength(arr):

  stacks = [deque([arr[0]])]
  longest = 1

  for i in range(1, len(arr)):
    item = arr[i]

    for stack in stacks:
      if stack[-1] < item:
        stack.append(item)
        longest = max(longest, len(stack))
    else:
      stacks.append(deque([item]))

  return longest
```
### Length_of_longest_increasing_subsequence
```python
import bisect

def length_of_longest_increasing_subsequence(nums):
    increasing_lst = []
    for n in nums:
        pos = bisect.bisect_left(increasing_lst, n)
        if pos < len(increasing_lst):
            increasing_lst[pos] = n
        else:
            increasing_lst.append(n)

    return len(increasing_lst)

# Test:
nums = [11, 5, 2, 5, 3, 7, 101, 18]
print(length_of_longest_increasing_subsequence(nums))  # Answer: 4
```
### Find median of two sorted arrays 
The median value is the value that separates a dataset into two equal halves..
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
      
        m, n = len(nums1), len(nums2)
        total_length = m + n

        if total_length % 2 == 0:
            mid1 = mid2 = total_length // 2
        else:
            mid1 = mid2 = total_length // 2 + 1

        pointer1 = pointer2 = 0
        median1 = median2 = 0.0

        while pointer1 + pointer2 < mid2:
            if pointer1 < m and (pointer2 >= n or nums1[pointer1] <= nums2[pointer2]):
                median1 = nums1[pointer1]
                pointer1 += 1
            else:
                median1 = nums2[pointer2]
                pointer2 += 1

            if pointer1 + pointer2 >= mid1:
                median2 = median1
                break

        if total_length % 2 == 0:
            if pointer1 < m and (pointer2 >= n or nums1[pointer1] <= nums2[pointer2]):
                median2 = nums1[pointer1]
            else:
                median2 = nums2[pointer2]
            return (median1 + median2) / 2.0
        else:
            return median1

```

#### 3 sum problem

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers

```python
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
```

#### Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

https://www.pankajtanwar.in/code/count-number-of-pairs-with-absolute-difference-k
```python
class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        int list[201] = {0};
        int res = 0;
        
        for(auto val: nums) {
            res += (val-k >= 0 ? list[val-k] : 0) + list[val+k];
            list[val]++;
        }
        return res;
    }
}
```

#### For  binary tree find max depth and max wide

the breadth-first search algorithm would work best to find the max-width of the tree,
and the depth-first search algorithm would work best to find the max-depth. 
```python
class TreeNode(object):

      def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

      def maxDepth(self, root):
          return 0 if root is None else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
https://github.com/GEEGABYTE1/Width-Depth-Tree-Problems
