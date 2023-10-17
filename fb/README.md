https://engineering.fb.com/2023/06/27/developer-tools/meta-developer-tools-open-source/

https://www.youtube.com/watch?v=GLTR39VIAdc Datas Structures and Algo

https://habr.com/ru/companies/otus/articles/764680/  recommendation system

https://habr.com/ru/companies/otus/articles/764222/  recommendation system


### Binary tree
https://towardsdatascience.com/4-types-of-tree-traversal-algorithms-d56328450846

#### max depth
````
def maxDepth(root):
 
   if not root return 0
   return max(maxDepth(root.right),  maxDepth(root.left)) + 1

````
### diameter

https://www.youtube.com/watch?v=X7_5fYEVIIU&list=PLQZEzAa9dfpkv0kZkjomTj553gQyafNiB&index=16

### traversal
```
breadth-first = lever order

depth-first has 3 variations:

in-order:  left subtree, current node, right subtree  (for Binary Search Tree it gives nodes in sorted manner)
pre-order: current node, left subtree, right subtree
post-order: left subtree, right subtree, current node
```
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
### min # of removes to make string  with parenteses valid
 https://www.youtube.com/watch?v=PDO3vvly7eU
````
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
### System design 

https://habr.com/ru/companies/otus/articles/765014/

https://www.youtube.com/watch?v=mCM6QVHD08c

https://habr.com/ru/companies/otus/articles/764902/ Redis Memcahed

https://www.youtube.com/watch?v=o5n85GRKuzk Design Twitter - System Design Interview

https://systemdesign.one/system-design-interview-cheatsheet/

https://www.youtube.com/watch?v=_K-eupuDVEc  Google system design interview: Design Spotify

3sum a+b+c

all permutations of string without recursion


### Blind 75 LeetCode questions refer to a curated list of the 75 most frequently asked LeetCode algorithms questions. 

I bought it:
https://www.udemy.com/course/blind-75-leetcode-questions-ace-algorithms-coding-interview/learn/lecture/37964360#overview

https://www.youtube.com/watch?v=em4EP-IiKac

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




