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

### Binary tree
https://towardsdatascience.com/4-types-of-tree-traversal-algorithms-d56328450846

### Tree traversal
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




