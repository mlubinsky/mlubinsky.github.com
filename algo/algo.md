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




#### Top K numbers

To have top k largest numbers in the heap. We will use a min-heap for this;
Time Complexity: O(N log K).
```python
from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for i in range(k):
            heappush(min_heap, nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
            
        return min_heap[0]
```	

###  Given a string s, find the longest palindromic subsequence’s length in s. 

https://emre.me/coding-patterns/palindromes/

##### Top-down Dynamic Programming with Memoization 
```
start and end are two changing values of our recursive function in the Brute Force Solution.
So, we can store the results of all subsequences in a two-dimensional array to memoize them.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.longestPalindromeSubseq_recursive(memo, s, 0, len(s) - 1)

    def longestPalindromeSubseq_recursive(self, memo, s, start, end):
        if start > end:
            return 0

        # every sequence with one element is a palindrome of length 1
        if start == end:
            return 1

        if memo[start][end] == -1:
            # case 1: elements at the beginning and the end are the same
            if s[start] == s[end]:
                memo[start][end] = 2 + self.longestPalindromeSubseq_recursive(memo, s, start + 1, end - 1)
            else:
                # case 2: skip one element either from the beginning or the end
                subseq1 = self.longestPalindromeSubseq_recursive(memo, s, start + 1, end)
                subseq2 = self.longestPalindromeSubseq_recursive(memo, s, start, end - 1)
                memo[start][end] = max(subseq1, subseq2)

        return memo[start][end]

Time Complexity: O(N2) because memoization array, memo[len(s)][len(s)].
 We will not have more than N*N subsequences.

Space Complexity: O(N2 + N) == O(N2) because we used N2 for memoization array and N for recursive stack.
```
#### Bottom-up Dynamic Programming with Tabulation 
```
We can build our two-dimensional memoization array in a bottom-up fashion, adding one element at a time.

if the element at the start and the end is matching,
the length of Longest Palindromic Substring (LPS) is 2 plus the length of LPS till start+1 and end-1.
if the element at the start does not match the element at the end,
 we will take the max of LPS by either skipping the element at start or end
So the overall algorith will be;

if s[start] == s[end]:
    memo[start][end] = 2 + memo[start + 1][end - 1]
else:
    memo[start][end] = max(memo[start + 1][end], memo[start][end - 1])
and the solution;

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # every sequence with one element is a palindrome of length 1
        for i in range(len(s)):
            memo[i][i] = 1

        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s)):
                # case 1: elements at the beginning and the end are the same
                if s[start] == s[end]:
                    memo[start][end] = 2 + memo[start + 1][end - 1]
                else:  # case 2: skip one element either from the beginning or the end
                    memo[start][end] = max(memo[start + 1][end], memo[start][end - 1])

        return memo[0][len(s) - 1]

Time Complexity: O(N2)
Space Complexity: O(N2) where N is the input sequence.
```

###  Longest common substr

https://emre.me/coding-patterns/longest-common-substring-subsequence/
 
#### Top-down Dynamic Programming with Memoization
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.longestCommonSubsequence_recursive(memo, text1, text2, 0, 0)

    def longestCommonSubsequence_recursive(self, memo, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if memo[i][j] == -1:
            if text1[i] == text2[j]:
                memo[i][j] = 1 + self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j + 1)
            else:
                memo[i][j] = max(self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j),
                                 self.longestCommonSubsequence_recursive(memo, text1, text2, i, j + 1))
        return memo[i][j]
```

#### Bottom-up Dynamic Programming with Tabulation 
```
Lets create our two dimensional array in a bottom-up fashion.

if the characters text1[i] matches text2[j], the length of the common subsequence would be one plus the length of the common subsequence until the i-1 and j-1 indexes.
if the characters text1[i] and text2[j] does not match, we take the longest sequence by skipping one character either from ith string or jth character from respective strings.
Our overall algorithm is;

if text1[i] == text2[j]:
    memo[i][j] = 1 + memo[i - 1][j - 1]
else:
    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
and the solution is;

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        max_length = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

                max_length = max(max_length, memo[i][j])
        return max_length
Time Complexity: O(N * M) where N and M are the lengths of two input strings.

Space Complexity: O(N * M)


```

#### Reverse linked list


https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        previous, current, next = None, head, None
        while current is not None:
            next = current.next  # temporarily store the next node
            current.next = previous  # reverse the current node
            previous = current  # point previous to the current node
            current = next  # move on
        return previous

```
https://medium.com/outco/reversing-a-linked-list-easy-as-1-2-3-560fbffe2088

```python
function reverse(head) {
// Step 1
  let previous = null
  let current = head
  let following = head
}
// Step 2
  while(current !== null) {
    following = following.next
    current.next = previous
    previous = current          
    current = following
  }
  // Step 3  
  return previous
}

```
#### All elements in array are present twice, but 1 element is unique - find it

```python
return 2*sum(set(arr)) - sum(arr)
```

#### Find the two non-repeating elements in an array of repeating elements

```python
def find_non_repeating_numbers(arr):
    xor = arr[0]

    for i in range(1, len(arr)):
        xor ^= arr[i]

    right_set_bit = xor & ~(xor-1)
    first = 0
    second = 0
    for i in arr:
        if i & right_set_bit:
            first ^= i
        else:
            second ^= i

    return first, second


arr = [2, 3, 7, 9, 11, 2, 3, 11]
print(find_non_repeating_numbers(arr))

```

####  Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.   Note: all the input strings are already lowercase.

# Approach 1
```python

def solution(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] +=1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1

print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

print('###')

#  Approach 2:  using collection 

import collections

def solution(s):
    # build hash map : character and how often it appears
    count = collections.Counter(s) # <-- gives back a dictionary with words occurrence count 
                                         #Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1

print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

```





#### Longest substr without repeating char O(n) complexity

https://ekamperi.github.io/programming/2021/04/14/longest-non-repeating-substring.html
 
https://github.com/StBogdan/PythonWork/blob/master/Leetcode/3.py

```python
def lengthOfLongestSubstring(s) :
        if not s:
            return 0

        len_max = 1
        elem_seen = set()
        start = 0
        for i, ltr in enumerate(s):
            if ltr in elem_seen:
                len_max = max(i - start, len_max)
                while start < i and ltr in elem_seen:
                    elem_seen.remove(s[start])
                    start += 1
            elem_seen.add(ltr)

        len_max = max(len(s) - start, len_max)
        return len_max
```


```python
def longest(s):
    m={}
    left=right=ans=0
    n=len(s)
    while left <n and right < n:
        el=s[right]
	   if el in m:
	       left = max(left, m(el)+1)
	       
	    m[el]=right
	    ans=max(ans, right-left+1)
	    right +=1
	    
    return ans 	    
```

#### Group anagrams
```python
def findHash(s):
   return ''.join(sorted(s))
   
def groupAnagrams(strs):
   answers=[]
   m={}
   for s in strs:
      hashed=findshash(s)
      if hashed not in m:
           m[hashed]=[]
	   
      m[hashed].append(s)
      
   for p in m.values():
      answers.append(p)
      
   return answers   
```

##### Max sum array of fixed length
```python
def maxSum(arr, window):
   arrSize=len(arr)
   if arrSize <= window: return None
   
   window_sum = sum([arr[i] for i in range(window)])
   max_sum = window_sum
   
   for i in range(arrSize - window):
      window_sum = window_sum -arr[i] + arr[i+window]
      max_sum = max(window_sum, max_sum)
      
   return max_sum   
```

#### max avg subarray og given N
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = []
        _sum, start = 0, 0
        for end in range(len(nums)):
            _sum += nums[end]  # add the next element

            if end >= k - 1:
                average.append(_sum / k)  # calculate the average
                _sum -= nums[start]  # subtract the element going out
                start += 1  # slide the window

        return max(average)
```

#### Max sum array of any length

  Time complexity: O(n*n)
```python  
def maximum_sum_dynamic(arr):
	'''Calculating maximum sum increasing subsequence using dynamic programming'''
	soln = [-sys.maxint] * len(arr)

	for i in range(len(arr)):
		soln[i] = arr[i]

	for i in range(1, len(arr)):
		for j in range(i):
			if arr[j] < arr[i] and soln[j] + arr[i] > soln[i]:
				soln[i] = soln[j] + arr[i]


	return max(soln)
```

#### Longest increasing subsequence

https://github.com/StBogdan/PythonWork/blob/master/Leetcode/300.py

  Method: Compressed DP, previous largest subsequence  
 Time: O(n\*log(n))  
 Space: O(n)  

```python


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seq = [nums[0]]
        for i in range(1, len(nums)):
            insert_poz = self.bisect(seq, nums[i])
            if insert_poz == len(seq):
                seq.append(nums[i])
            else:
                seq[insert_poz] = nums[i]

        return len(seq)

    @staticmethod
    def bisect(arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if target > arr[mid]:
                low = mid + 1
            elif target < arr[mid]:
                high = mid - 1
            else:
                return mid

        return low

```

Another approach:   Time Complexity: O(n * n)
```python

def longest_increasing_subsequence_dynamic(array, length):
	'''Using dynamic programming to find the length of longest increasing subsequence'''
	lis = [1] * length

	for i in range(1, length):
		for j in range(i):
			if (array[j] < array[i] and lis[i] < lis[j] + 1):
				lis[i] = lis[j] + 1
	
	return max(lis)
```	

#### find the continuous subarray  which has the largest sum and return its sum.
 
```python
input=[-2,1,-3,4,-1,2,1,-5,4]

def array_num(input):
    max_so_far=input[0]
    sum=0
    for index in range(1,len(input)):
        if input[index]>max_so_far:
            sum=input[index]
        else:
            sum+=input[index]
        if sum>max_so_far:
            max_so_far=sum
    return(max_so_far)

print(array_num(input))
```

#### Largest continuous sum

```
def largest_continous_sum_two(arr):
    if len(arr) == 0: # handle an edge case
        return None
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum=max(current_sum+num, num)
        max_sum=max(current_sum, max_sum)
    return max_sum
```


#### max product subarray
```
It is similar to maximum sum subarray problem. But the input can have both
positive and negative number. Only store the local maximum number is not
enough.
we can use DP to solve this problem. Let maxDP[i] denote the maximum
product in subarray [0,...,i], and minDP[i] indicates the min product in subarray
[0,..,i]
So, the DP transformation function is:
maxDP[i] = max(maxDP[i-1] * nums[i], minDP[i-1]* nums[i], nums[i
]);
minDP[i] = min(minDP[i-1]* nums[i], maxDP[i-1]*nums[i], nums[i])



def maxProduct( nums)
  
 n = nums.size();
 maxDP = [0]*n
 minDP = [0]*n
 maxDP[0] = nums[0];
 minDP[0] = nums[0];
 result = nums[0];
	
 for  i  in range (len(nums))
     maxDP[i] = max(max(maxDP[i - 1] * nums[i], 
	          nums[i]), 
	          minDP[i - 1] * nums[i]);
     minDP[i] = min(min(minDP[i - 1] * nums[i], 
	          nums[i]),
	          maxDP[i - 1] * nums[i]);
	
  result = max(result, maxDP[i]);

return result;
```

#### Is number prime?
```
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in  range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
```

### Merging 2 sorted arrays
into 1st array where 1st array has the capacity for both
```
private void merge(int[] a, int n, int[] b, int m) {
	int i = n - 1;
	int j = m - 1;
	int k = n + m - 1;
	
	while (j >= 0) {
		if (i>=0 && a[i] > b[j])
			a[k--] = a[i--];
		else
			a[k--] = b[j--];
	}
}
```

###   determine if two trees are identical 
  
  binary tree node has data, pointer to left child and a pointer to right child 
```  
class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
      
def identicalTrees(a, b): 
      
    # 1. Both empty 
    if a is None and b is None: 
        return True 
  
    # 2. Both non-empty -> Compare them 
    if a is not None and b is not None: 
        return ((a.data == b.data) and 
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right)) 
      
    # 3. one empty, one not -- false 
    return False
  
# Driver program to test identicalTress function 
root1 = Node(1) 
root2 = Node(1) 
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5) 
  
if identicalTrees(root1, root2): 
    print "Both trees are identical"
else: 
    print "Trees are not identical"

```




<https://rcoh.me/posts/linear-time-median-finding/>.      MEDIAN finding 

```
### This is O (nlogn)
 
def nlogn_median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) / 2]
    else:
        return 0.5 * (l[len(l) / 2 - 1] + l[len(l) / 2])
```	
#### quick select algo
```
It’s a recursive algorithm that can find any element (not just the median).

1. Pick an index in the list. The element at this index is called the pivot.
2. Split the list into 2 groups:
     a) Elements less than or equal to the pivot, lesser_els
     b) Elements strictly greater than the pivot, great_els
We know that one of these groups contains the median. Suppose we’re looking for the kth element:
If there are k or more elements in lesser_els, recurse on list lesser_els, searching for the kth element.
If there are fewer than k elements in lesser_els, recurse on list greater_els. Instead of searching for k, we search for k-len(lesser_els).


import random
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)
```
Inverting a binary tree:
The root is still the root, but everything else is just flipped:
https://leetcode.com/problems/invert-binary-tree/
```

  TreeNode* invertTree(TreeNode* root) {
    if (root) {
      invertTree(root->left);
      invertTree(root->right);
      std::swap(root->left, root->right);
    }
    return root;
  }


 invert(tree):
      if(tree not null):
        temp := tree.left
        tree.left <- tree.right
        tree.right <- temp
        invert(tree.left)
        invert(tree.right)
        
 ```       
 
 
 
### Find 1st element in rotated sorted array

 ```
    def bs(lst, start, end):
       print ("start=",start, "end=", end)
       if start == end:  return start
       m = (start+end)//2
       print ("middle=",m, lst[m])

       if m < end and lst[m+1] < lst[m]:
          return m+1
       if m > start and lst[m] < lst[m-1]:
          return m

       if lst[end] > lst[m]:
          return bs(lst, start, m -1)
       else:
          return  bs(lst, m+1, end)

    def find(l):
      start=0
      end=len(l)-1
      i= bs(l, start, end)
      return i

    if __name__ =="__main__":
      print ("main")
      l1=[5,10,20, 1,2,3,4]
      print(l1)
      i=find(l1)
      print ("index=",i)

      l2=[20, 1,2,3,4]
      print(l2)
      i=find(l2)
      print ("index=",i)
```

Brackets:
```
def isProperlyNested(S):
    stack = []
    for s in S:
        if s == '{' or s == '(' or s == '[':
            stack.append(s)
        elif s =='}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s)
        elif s ==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
        else:
            pass
                
    # non-empty stack, NOT properly nested 
    if stack:
        return S, stack, False
    
    # properly nested
    else:
        return S, stack, True
        
S = "(()(())())"
print(isProperlyNested(S))

S =  "())"
print(isProperlyNested(S))

S = "(()){}[]"
print(isProperlyNested(S))

S = ")("
print(isProperlyNested(S))

S = "+)(+()"
print(isProperlyNested(S))

S = "(12)(34)"
print(isProperlyNested(S))

S = ""
print(isProperlyNested(S))
```
