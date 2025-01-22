###

<https://www.algoexpert.io/systems/product>

<https://techiedelight.quora.com/500-Data-Structures-and-Algorithms-interview-questions-and-their-solutions>

https://llego.dev/tags/technical-coding-interview/

https://www.linkedin.com/my-items/saved-posts/

https://vurt.org/articles/twelve-rules/

https://techiedelight.quora.com/500-Data-Structures-and-Algorithms-interview-questions-and-their-solutions

https://blog.chay.dev/things-that-make-your-application-stand-out/

https://github.com/alex/what-happens-when when you press button on keyboard

https://habr.com/ru/articles/840116/   How internet works

https://habr.com/ru/companies/bothub/articles/812265/  System design interview

https://habr.com/ru/companies/yandex_praktikum/articles/834230/ System design interview

https://habr.com/ru/companies/ods/articles/828772/

https://www.youtube.com/watch?v=_keHRxzx7as   Глеб Михайлов Новые задачи на LeetCode | Ща порешаем! #99  
https://www.youtube.com/watch?v=JtMuXmmDl9s    Саша Лукин  
https://www.youtube.com/watch?v=csCtjoDmByA   Squares of a Sorted Array. 
```
Google Advanced Data Analytics Professional Certificate | Coursera
Microsoft Certified: Power BI Data Analyst Associate - Certifications | Microsoft Learn
AWS Certified Machine Learning - Specialty Certification | AWS Certification | AWS (amazon.com)
Microsoft Certified: Azure Data Scientist Associate
```

### Advices
https://habr.com/ru/articles/817031/ 
https://habr.com/ru/articles/817029/  Как найти работу мечты в США 1 
https://habr.com/ru/articles/817031/ Как найти работу мечты в США 2 


https://relational.ai/careers/ JOB

https://habr.com/ru/articles/794556/

https://habr.com/ru/articles/797837/

Competitive coding:  leetcode.com, geeksforgeeks.org

https://uproger.com/bolshaya-shpargalka-po-algoritmam-s-sobesedovanij/

Mock interviews, salary negotiation consulting:  interviewing.io, interviewkickstart.com

https://news.ycombinator.com/item?id=37111256

https://medium.com/the-weekly-readme/resources-that-got-me-into-amazon-microsoft-and-google-029d7daf3965

https://medium.com/@ricbedin/how-i-landed-4-staff-l6-software-engineering-offers-amazon-meta-stripe-and-braze-cfeed8d3e5a9

### How to build resume:

https://cloudirregular.substack.com/p/the-greatest-resume-ive-ever-seen

https://news.ycombinator.com/item?id=36901303


```
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


### Problems

https://allaboutalgorithms.com/finding-closest-points-faster-than-o-n%C2%B2-ea5d005bc911

https://machine-learning-made-simple.medium.com/coding-interviews-problem-12-group-shifted-strings-meta-82b6499eb5bd

https://www.techbeamers.com/python-tricky-coding-exercises/#google_vignette

https://www.leetsolve.com/

https://leetsolve.com/48-rotate-image

https://www.guru99.com/longest-common-subsequence.html

Median from data stream
https://python.plainenglish.io/median-from-data-stream-8323faee348

Intervals:
https://faun.pub/intervals-coding-pattern-efa438dede8a

Priority queue
https://faun.pub/priority-queue-using-heapq-9d8fccc49d51


Prefix SUM
https://blog.devgenius.io/array-coding-pattern-prefix-sum-a83d313c7e5a

Longest common prefix; https://python.plainenglish.io/longest-common-prefix-2d237c52e11d

Matrix in python: 
 https://blog.devgenius.io/working-with-matrix-in-python-cheatsheet-2654835d9dc7
 

Yandex interview: 
https://www.youtube.com/watch?v=0yxjWwoZtLw

https://www.youtube.com/watch?v=zU-LndSG5RE

https://www.youtube.com/watch?v=krDfPEYVVvk

Algorithms: 
https://github.com/heineman

https://www.youtube.com/@Power_Couple/videos

FAANG interview questions
https://media.licdn.com/dms/document/media/D4D1FAQH_q662e7ciYg/feedshare-document-pdf-analyzed/0/1686549764622?e=1687392000&v=beta&t=t3ZlZ6w4CMjYMfIDEg8DKA15ecgVSqrX5XNwo2pcBd0

URL shortener: https://habr.com/ru/articles/746602/

https://www.youtube.com/watch?v=rPp46idEvnM  Hash table from Lukin (ru)

 https://habr.com/ru/articles/756394/

https://habr.com/ru/articles/743514/

All permutations of string
https://www.techbeamers.com/permutation-of-a-string-in-python/

### Brackets matching
```
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
### Longest increasing subsequence
https://llego.dev/posts/python-solving-longest-increasing-subsequence/

```
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
```
Initialize with stack containing first array element
For each subsequent element, try to append to existing stacks if order is maintained
If no stack append is possible, make new stack with that element
Track longest stack found to get LIS length
This leverages Python’s deque to simulate the stacks in an efficient way.
By greedily extending stacks that maintain order, we build up the LIS with just one array pass.

The time complexity is O(n log n) due to the stack manipulations, making this a fast optimization over the dynamic programming approach.

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
```
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

https://gaultier.github.io/blog/kahns_algorithm.html

https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers 

https://habr.com/ru/articles/729944/

https://github.com/nkwade/nkwade-lc-solutions

https://github.com/klaus19/LeetcodeinPython

https://stepik.org/course/217    Алгоритмы: теория и практика. Методы

https://stepik.org/course/1547  Алгоритмы: теория и практика. Структуры данных

https://stepik.org/course/102772 Ace Your Next Coding Interview by Learning Algorithms


https://medium.com/@tudorache.a.bogdan/day-5-arrays-median-of-two-sorted-arrays-17c9349e21ca

### Find median of two sorted arrays 
The median value is the value that separates a dataset into two equal halves..
```
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

https://stepik.org/lesson/41233/step/1?unit=19817 

https://stepik.org/course/126012/promo Interview prep (russian)

https://www.linkedin.com/feed/update/urn:li:activity:7001201153686269952/

https://alignedclarity.substack.com/p/streamline-your-resume-and-increase

https://docs.google.com/document/d/19fr_36WOzKlq_zyGP2RdxMEsdNQMZdUqn1Vahncr2pY/edit#heading=h.xg3o3psx1mah

https://grow.google/certificates/interview-warmup/

https://github.com/prabhupant/python-ds

https://habr.com/ru/company/getmatch/blog/678742/

https://habr.com/ru/post/684756/ binary search

https://habr.com/ru/post/679008/ process big file

Вы стоите на поверхности Земли. 
Затем вы начинаете идти: проходите один километр на юг, 
один на запад и один на север. В итоге вы оказываетесь в начальной точке.
Где вы стоите?
https://habr.com/ru/post/678254/

https://florian.github.io//xor-trick/ XOR trick

https://www.youtube.com/watch?v=Peq4GCPNC5c&t=1s . 10 common interview questions - solved

https://habr.com/ru/post/661577/ Обход графа в ширину (BFS) и глубину (DFS)

https://www.youtube.com/watch?v=JtMuXmmDl9s

https://towardsdatascience.com/how-to-find-all-solutions-to-the-subset-sum-problem-597f77677e45

https://habr.com/ru/post/653617/

https://habr.com/ru/post/646319/ amazon interview

https://malisper.me/an-algorithm-for-passing-programming-interviews/

https://news.ycombinator.com/item?id=29775023

https://github.com/NIteshx2/AdvancedSQL_Interview

https://www.youtube.com/watch?v=fAAZixBzIAI . Binary Tree

https://www.facebookcareers.com/DE-prep-onsite/

https://www.youtube.com/watch?v=SgaN-4po_cA How I Got a Job at DeepMind as a Research Engineer


https://github.com/prius/learning

https://github.com/prabhupant/python-ds

https://habr.com/ru/company/otus/blog/599309/

https://medium.com/@pv.safronov/graph-traversal-python-patterns-that-help-you-think-less-and-code-faster-66f76e1ab820

https://www.amazon.com/Algorithm-Design-Manual-Computer-Science-dp-3030542556/dp/3030542556 The Algorithm Design Manual by Skiena

https://www.algorithm-archive.org/

https://www.educative.io/path/ace-python-coding-interview

https://www.algoexpert.io/

https://www.chrislaux.com/

https://habr.com/ru/post/587348/

https://medium.com/javarevisited/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0

https://mlengineer.io/how-i-prepare-for-amazon-applied-scientist-l5-2020-30e080cb5dbe

https://towardsdatascience.com/how-i-doubled-my-salary-in-4-months-e8c5b2b9f5bc

https://mlengineer.io/how-i-got-facebook-mle-offer-us-4-2020-by-practicing-2-lc-questions-per-day-ce3b27abfc

https://mlengineer.io/how-i-failed-amazon-interview-mle-9def3c91b886

https://github.com/yangshun/tech-interview-handbook

https://www.youtube.com/watch?v=tWVWeAqZ0WU . Graph Algo

https://github.com/kdn251/interviews

https://cp-algorithms.com/index.html

https://habr.com/ru/company/geekfactor/blog/585352/ 7 платформ для подготовки к техническому интервью

https://www.youtube.com/watch?v=3QA4Yg4leGQ&list=RDCMUCNc-Wa_ZNBAGzFkYbAHw9eg&start_radio=1

https://liuzhenglaichn.gitbook.io/algorithm/

https://www.techiedelight.com

https://towardsdatascience.com/intro-to-data-structures-2615eadc343d

https://www.java67.com/2018/05/top-75-programming-interview-questions-answers.html

https://www.youtube.com/watch?v=vs4aFU3DiXY  interview for ML

https://emre.me/

https://www.pankajtanwar.in/coding-diary


https://www.java67.com/2018/04/21-string-programming-and-coding-interview-questions-answers.html

https://www.educative.io/courses/grokking-the-coding-interview?affiliate_id=5073518643380224

https://emre.me/coding-patterns/merge-intervals/ . Merge intervals

https://www.interviewbit.com/coding-interview-questions/


https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27


https://github.com/thundergolfer/interview-with-python/tree/master/solutions/python

https://redquark.org/blogs


### Interview

<https://www.quora.com/How-do-I-start-learning-or-strengthen-my-knowledge-of-data-structures-and-algorithms?redirected_qid=2804253>

<https://www.dailycodingproblem.com/subscribe?email=mlubinsky%40hotmail.com>

<https://www.byte-by-byte.com>

<https://stratos.seas.harvard.edu/files/stratos/files/periodictabledatastructures.pdf>

<https://hackernoon.com/10-data-structure-algorithms-and-programming-courses-to-crack-any-coding-interview-e1c50b30b927>

<https://www.bitdegree.org/user/course/data-structures-and-algorithms>

#### 3 sum problem

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers

```
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
```
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

### Path from root to given node

https://www.devglan.com/datastructure/print-path-from-root-to-node-binary-tree

https://www.techiedelight.com/print-all-paths-from-root-to-leaf-nodes-binary-tree/

#### For  binary tree find max depth and max wide

the breadth-first search algorithm would work best to find the max-width of the tree,
and the depth-first search algorithm would work best to find the max-depth. 
```
class TreeNode(object):

      def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

      def maxDepth(self, root):
          return 0 if root is None else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
https://github.com/GEEGABYTE1/Width-Depth-Tree-Problems

#### 2 Heaps pattern Find ( Median from Data Stream)
https://emre.me/coding-patterns/two-heaps/
```
 we want to know the smallest element in one part and the biggest element in the other part.
 Two Heaps pattern uses two Heap data structure to solve these problems;
 
 a Min Heap to find the smallest element and a Max Heap to find the biggest element.
 
 Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
```

#### Topological sort

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0, 1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

```
The aim of topological sort is to provide a partial ordering among the vertices of the graph such that if there is an edge from U to V then U <= V, which means, U comes before V in the ordering.

Source: Any node that has no incoming edge and has only outgoing edges is called a source.
Sink: Any node that has only incoming edges and no outgoing edge is called a sink.
Topological ordering starts with one of the sources and ends at one of the sinks.
A topological ordering is possible only when the graph has no directed cycles, i.e. if the graph is a Directed Acyclic Graph (DAG). If the graph has a cycle, some vertices will have cyclic dependencies which makes it impossible to find a linear ordering among vertices.
To find the topological sort of a graph we can traverse the graph in a Breadth First Search (BFS) way.

a. Initialization

We will store the graph in Adjacency Lists, which means each parent vertex will have a list containing all of its children. We will do this using a Hash Table where the key will be the parent vertex number and the value will be a List containing children vertices.

To find the sources, we will keep a Hash Table to count the in-degrees (count of incoming edges of each vertex). Any vertex with 0 in-degree will be a source.

b. Build the graph and find in-degrees of all vertices

We will build the graph from the input and populate the in-degrees Hash Table.

c. Find all sources

All vertices with 0 in-degrees will be our sources and we will store them in a Queue.

d. Sort

For each source:

Add it to the sorted list.
Get all of its children from the graph.
Decrement the in-degree of each child by 1.
If a child’s in-degree becomes 0, add it to the sources Queue.
Repeat these steps, until the source Queue is empty.

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_list = []

        if numCourses <= 0:
            return False

        # a. Initialization
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph
        in_degree = {i: 0 for i in range(numCourses)}  # count of incoming edges

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)  # put the child into it's parent's list
            in_degree[child] += 1

        # c. Find all sources
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        # d. Sort
        while sources:
            vertex = sources.popleft()
            sorted_list.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        # if sorted_list does not contain all the courses, there is a cyclic dependency between courses
        # scheduling is not possible if there is a cyclic dependency
        return len(sorted_list) == numCourses
Time Complexity: O(V + E) where V is the total number of courses and E is the total number of prerequisites.

Space Complexity: O(V + E) since we are storing all of the prerequisites for each course in an adjacency list.
```
#### Top K numbers

To have top k largest numbers in the heap. We will use a min-heap for this;
Time Complexity: O(N log K).
```
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






```
Section		Score	Total

Inspect			
 
Did I explicilty state what the input was?		1
Did I clarify what the desired output was?		1
Did I construct a simple example that could be solved by hand?		2
Did I write out all Axioms?		1
Did I write out and derive all intelligent assumptions?		1
 
Strategy			
 
Did I brainstorm a simple solution?		2
Did I analyze the runtime?		2
Did I analyze the space requirement?		1
Did I ask if the input problem set would be small enough for this to suffice?
Was I able to come up with a better more sophisticated solution?		4
Did I analyze the time complexity of this solution?		2
Did I analyze the space complexity of this solution?		2
Did I compare it directly to my initial simple solution?		1
Was I confident when I started coding?		4
Did I think through all approaches that come to mind?		5
Did I explicitly write out my desired strategy?		4
Did I explicitly consider base cases?		2
How well did I handle getting stuck?		5

Code	

How cleanly was my code written?		2
Did I explicitly check for any off-by-one errors?		2
Was I able to predict what funtions I would end up implementing ?		1
Did my brainstormed strategy solve the problem?		3
How smooth was the coding process?		2
Was I able to talk through my code?		5
Did I leverage any interesting functions in my code?		2

Review			

Did I prove my runtime complexity?		2
Did I prove my spacetime complexity?		2
Did I write up different test cases and process them?		6
Did I go line by line, no matter how trivial?		2
DId I have to make any changes when reviewing my code?		2
 
```
How to use this rubric: https://3dtrends.substack.com/p/the-coding-interview-pt-1-inspect

Prepping for an interview in big tech and need some guidance? Join the discord: https://discord.gg/NgJXgkbgd6
 

#### Cousera

https://www.coursera.org/in-progress

### Udemy

https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews/. Udemy


https://www.udemy.com/course/leetcode-in-python-50-algorithms-coding-interview-questions/

https://github.com/BitPunchZ/Leetcode-in-python-50-Algorithms-Coding-Interview-Questions/


https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews


<https://www.udemy.com/11-essential-coding-interview-questions/?couponCode=AMAZON2>



#### Reverse linked list


https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/

```
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

```
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

```
return 2*sum(set(arr)) - sum(arr)
```

#### Find the two non-repeating elements in an array of repeating elements

```
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
#### All permutation of the string

https://github.com/thundergolfer/interview-with-python/blob/master/solutions/python/string-permutations.py

#### Given strings S and T find the min window in S which contains all chars in T

???
 


####  Given a string, find the first non-repeating character in it and return its index. 
```
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

#Approach 1
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

#Approach 2 using collection 

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

```
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


```
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
```
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
```
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
```
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
```  
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


```
# Method: Compressed DP, previous largest subsequence
# Time: O(n\*log(n))
# Space: O(n)

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

Another approach:
```
# Time Complexity: O(n * n)
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
 
```
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

### Github

https://github.com/lilianweng/LeetcodePython

<https://github.com/programmercave0/Algo-Data-Structure/blob/master/README.md>

<https://yangshun.github.io/tech-interview-handbook/>

<https://github.com/mission-peace/interview/tree/master/src/com/interview>

<https://github.com/donnemartin/interactive-coding-challenges>

<https://github.com/alexhagiopol/cracking-the-coding-interview>

<https://github.com/charulagrl/data-structures-and-algorithms>

<https://github.com/thundergolfer/interview-with-python/tree/master/solutions/python>

<https://github.com/anubhavshrimal/Data_Structures_Algorithms_In_Python>

<https://github.com/bt3gl/Python-and-Algorithms-and-Data-Structures/>

https://github.com/BitPunchZ/Leetcode-in-python-50-Algorithms-Coding-Interview-Questions/



https://github.com/StBogdan/CTCI_python Cracking code interview

https://github.com/StBogdan/PythonWork

<https://github.com/parineeth/tbboci-3rd-edition-python>

https://github.com/alexeygrigorev/data-science-interviews . 

https://github.com/labuladong/fucking-algorithm/tree/english. Leetcode guide

<https://github.com/30-seconds/30-seconds-of-python-code>

<https://github.com/TheAlgorithms/Python>


<https://github.com/devAmoghS/Practice-Problems>

<https://github.com/tayllan/awesome-algorithms>

<https://github.com/karan/Projects>



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



#### Merge an array of k linked-lists lists TODO)

http://www.cmsmagazine.ru/library/items/programming/80-problems-with-it-interviews/



https://habr.com/ru/company/skillfactory/blog/582450/

https://habr.com/ru/company/skillfactory/blog/539058/

https://habr.com/ru/company/ruvds/blog/515258/. Algorithms

https://habr.com/ru/company/skillfactory/blog/538536/ interview

https://medium.com/swlh/my-preparation-journey-for-google-interviews-f41e2dc3cdf9 interview

https://habr.com/ru/post/539166/ Algo

https://habr.com/ru/post/535216/ interview

https://habr.com/ru/post/550088/ interview

### String Algo

https://paddy3118.blogspot.com/2021/02/longest-common-substring-investigation.html. longest common substr


find the longest palindrome subsequence of a string optimally

https://alkeshghorpade.me/post/leetcode-longest-substring-without-repeating-characters



https://johnlekberg.com/blog/2020-08-01-task-order.html . topological sort

https://medium.com/javascript-in-plain-english/facebook-coding-interview-questions-9e40bdbbec35

https://akshayr.me/blog/articles/python-dictionaries

https://medium.com/better-programming/dynamic-programming-interview-questions-maximum-profit-in-job-scheduling-6c5ec15c4cc5

https://medium.com/better-programming/cracking-the-amazon-interview-cf6a6c5f954a

https://blog.pragmaticengineer.com/data-structures-and-algorithms-i-actually-used-day-to-day/


https://www.youtube.com/watch?v=2yWf3TrJ6Xs&feature=youtu.be

<https://habr.com/ru/post/499394/>

https://www.youtube.com/channel/UCZCFT11CWBi3MHNlGf019nw/videos

<https://www.algoexpert.io/systems/product>

<https://algorithmica.org/ru/>

<https://medium.com/@andreimargeloiu/how-to-prepare-for-competitive-programming-396d557e0c12>

<https://medium.com/swlh/binary-search-cheat-sheet-for-coding-interviews-9c5425af357e>

<https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46> Median of 2 sorted attays

<https://habr.com/ru/post/503602/>

<https://crunchskills.com/binary-tree-interview-questions-and-practice-problems/>

<https://crunchskills.com/google-interview-questions-for-software-engineering-roles/>


https://medium.com/dev-genius/15-binary-tree-coding-problems-from-faang-interview-2ba1ec67d077

https://medium.com/@srajaninnov/find-the-diameter-of-a-binary-tree-efc45b9129a7


<https://habr.com/ru/company/spice/blog/478250/>

<https://habr.com/ru/company/spice/blog/479320/>

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



<https://data-flair.training/blogs/python-programming-interview-questions/>

<https://data-flair.training/blogs/top-python-interview-questions-answer/>

<https://firstround.com/review/40-favorite-interview-questions-from-some-of-the-sharpest-folks-we-know/>

<https://news.ycombinator.com/item?id=20897510>

<https://medium.com/@alexgolec/google-interview-problems-ratio-finder-d7aa8bf201e3>

<https://habr.com/ru/post/467371/> Разбор задачи с собеседования Google: поиск соотношения

<https://www.youtube.com/watch?v=xYBKMV92YrM>



<https://classicproblems.com/>

<https://teachyourselfcs.com/>

<https://web.stanford.edu/class/cs9/>

<https://algodaily.com/challenges>

<https://news.ycombinator.com/item?id=20729252>

<https://habr.com/ru/company/skillbox/blog/462979/>





<https://www.youtube.com/watch?v=EuPSibuIKIg>


<https://www.youtube.com/channel/UCaYQbIciTyBFMTRE2Zp81tw>

<https://www.youtube.com/watch?v=2H_2UGsRmLE&list=PLuVT2Ug8ISOXYhtc-mSeAnJYMbI3WKY5o&index=5&t=0s>

<https://medium.com/@ratulsaha/preparing-for-programming-interview-as-a-phd-student-with-python-5f8af8b40d5f>

<https://www.youtube.com/watch?v=jM2dhDPYMQM>. Sliding window

<https://malisper.me/an-algorithm-for-passing-programming-interviews/>

### Facebook

https://levelup.gitconnected.com/cracking-the-top-40-facebook-coding-interview-questions-185bab32489f

https://daqo.medium.com/facebook-senior-software-engineer-interview-the-only-post-youll-need-to-read-e4604ff2336d

https://news.ycombinator.com/item?id=25658098

https://doisinkidney.com/posts/2019-06-04-solving-puzzles-without-your-brain.html

https://cp-algorithms.com/

https://tproger.ru/articles/problems/


https://www.pythonpool.com/knapsack-problem-python/






https://www.pythonforbeginners.com/queue/queue-in-python


https://www.youtube.com/watch?v=Dx5eiQdv4k8 Find 2 closest points on plain



https://kalkicode.com/data-structure/1500-most-common-data-structures-and-algorithms-solutions

https://stackoverflow.com/questions/67526076/what-is-the-most-efficient-way-of-getting-the-intersection-of-k-sorted-arrays



https://runestone.academy/runestone/books/published/pythonds/index.html#problem-solving-with-algorithms-and-data-structures-using-python

https://news.ycombinator.com/item?id=25519718 Interview advice that got me offers 

https://www.youtube.com/watch?v=kbx7xpSKBaI climbing stairs





https://habr.com/ru/company/otus/blog/565988/ . Median in the stream


https://betterprogramming.pub/top-5-hardest-coding-questions-from-recent-faang-interviews-d46bcb4dd8dc


https://www.pythonforbeginners.com/data-structures

https://mccme.ru/shen/progbook/7edition.pdf

https://habr.com/ru/post/576558/

https://habr.com/ru/post/579410/ interview for ML

## Print the outlier nodes in binary tree
<https://www.jeffcarp.com/posts/2018-how-to-solve-every-software-engineering-interview-question/> 


<https://habr.com/ru/post/457042/> . Tree traversal using 2 threads (Java)

## LCA
<https://en.wikipedia.org/wiki/Lowest_common_ancestor>
<https://sites.google.com/site/mytechnicalcollection/algorithms/trees/lca-of-binary-tree>
<https://stackoverflow.com/questions/1484473/how-to-find-the-lowest-common-ancestor-of-two-nodes-in-any-binary-tree>


<https://www.youtube.com/channel/UCcAWgbpROQrPok18E6UozWw/videos>

<https://www.facebook.com/tusharroy25/>



<https://blog.finxter.com/python-interview-questions/>

<https://stackoverflow.com/questions/11897088/diameter-of-binary-tree-better-design>

<http://www.interviewdruid.com/>

<https://www.amazon.com/dp/1983861189>

<https://www.algoexpert.io/product>

<https://www.hackerrank.com/>

<https://www.interviewbit.com/>

<https://www.quora.com/How-do-I-learn-algorithms-2>

<https://skillupper.com/>

### Hash

<https://moultano.wordpress.com/2018/11/08/minhashing-3kbzhsxyg4467-6/>

https://realpython.com/python-hash-table/

<https://habr.com/post/430788/>

<https://stackabuse.com/graph-data-structure-interview-questions/>

<http://www.java67.com/2018/05/top-75-programming-interview-questions-answers.html>

Hard Interview Questions in FAANG - 4 | Live Problem Solving | Interview Cracking Series

https://www.youtube.com/watch?v=8Uk2e7cCuyw



<https://techiedelight.quora.com/500-Data-Structures-and-Algorithms-interview-questions-and-their-solutions>

<https://blog.usejournal.com/i-interviewed-at-six-top-companies-in-silicon-valley-in-six-days-and-stumbled-into-six-job-offers-fe9cc7bbc996>

<https://www.businessinsider.fr/us/microsoft-new-developer-interview-process-2018-12>

<https://stackabuse.com/programming-interview-questions/>

<https://bradfieldcs.com/algos/>

<http://rachitiitr.blogspot.com/>

<https://www.youtube.com/watch?v=4NIb9l3imAo>

### disjoint set union (DSU) или Union-Find.

https://python.plainenglish.io/union-find-data-structure-in-python-8e55369e2a4f

<https://habr.com/ru/post/104772/>
создать быструю структуру, которая поддерживает следующие операции:

MakeSet(X) — внести в структуру новый элемент X, создать для него множество размера 1 из самого себя.
Find(X) — возвратить идентификатор множества, которому принадлежит элемент X. В качестве идентификатора мы будем выбирать один элемент из этого множества — представителя множества. Гарантируется, что для одного и того же множества представитель будет возвращаться один и тот же, иначе невозможно будет работать со структурой: не будет корректной даже проверка принадлежности двух элементов одному множеству if (Find(X) == Find(Y)).

Unite(X, Y) — объединить два множества, в которых лежат элементы X и Y, в одно новое.


<http://iolivia.me/posts/4-bloom-filter-part-3/> Bloom filter

<https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work>

<https://stackoverflow.com/questions/41515081/algorithm-find-all-permutations-of-string-a-in-string-b>

<https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/>

<http://www.java67.com/2018/05/top-75-programming-interview-questions-answers.html>

<http://www.algorithmsilluminated.org/>

<https://able.bio/daqo/landing-a-software-engineering-job-at-facebook--78k4a0s>

<https://habr.com/ru/company/digital-ecosystems/blog/473018/> Facebook 
 


<https://www.geeksforgeeks.org/union-find/> union-find (disjoint-set)

<https://habr.com/ru/company/edison/blog/481304/>

<http://blog.amynguyen.net/?p=853>

<https://news.ycombinator.com/item?id=18236396> .  Favorite algos

<https://aryaboudaie.com/interviews/python/technical/2017/11/06/python-for-interviews.html>

<https://algoexpert.io/rachit>  Use "rachit" as coupon code to get 30% off

<http://quiz.geeksforgeeks.org/amazons-most-frequently-asked-interview-questions-set-2/>

<https://www.geeksforgeeks.org/amazons-asked-interview-questions/>

<https://habr.com/ru/post/112222/> heap

<https://medium.com/educative/3-month-coding-interview-bootcamp-904422926ce8>

<https://habr.com/ru/post/437702/> Разбор задачи с собеседования в Google: синонимичные запросы

<http://algorithms.wtf/> 

<https://www.byte-by-byte.com/google-interview/>

<https://courses.csail.mit.edu/iap/interview/materials.php>


https://www.advancedalgorithms.com/ru. Advanced algo (ru)



<https://m.stopa.io/10-offers-100-days-the-journey-16a0407b8d95> interview
<https://habr.com/ru/post/454264/> . Inteview

<https://hackernoon.com/20-string-coding-interview-questions-for-programmers-6b6735b6d31c>

<https://medium.com/@fahimulhaq/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed>

<https://www.solutionfactory.in/posts/Floyd-Cycle-Detection-Algorithm-in-Java> Cycle detection

<https://docs.google.com/spreadsheets/d/1GOO4s1NcxCR8a44F0XnsErz5rYDxNbHAHznu4pJMRkw/edit#gid=0>

<https://www.youtube.com/watch?v=9clnwaqOU2E> string algo

<https://www.globalsoftwaresupport.com/most-common-programming-interview-questions-in-2019/>



<https://habr.com/ru/post/442352/> Бинарные деревья поиска

<https://www.youtube.com/watch?v=lpO_arK69vg> LCA


<https://www.youtube.com/watch?v=bBPHpH8aKjw> look fo links here!

##  Google interview
<https://habr.com/post/419945/>

<https://news.ycombinator.com/item?id=18374938>

<https://habr.com/company/google/blog/425279/> 

https://medium.com/@alexgolec/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029


<https://www.youtube.com/watch?v=5o-kdjv7FD0>

<https://interviewing.io/recordings>

<https://habr.com/post/419725/> Non-symmetric dime simulation

<http://www.cmsmagazine.ru/library/items/programming/80-problems-with-it-interviews/>

<https://saru.science/tech/2017/01/18/judy-arrays.html> Judy array

<https://www.reddit.com/r/cpp/comments/9afpq7/whats_your_favorite_data_structure/>

<https://habr.com/post/420605/>

<https://discuss.codechef.com/questions/48877/data-structures-and-algorithms>

<https://www.youtube.com/watch?v=1CxyVdA_654> Running mediam in stream

<https://www.youtube.com/watch?v=IHsX70r-fIQ> Max sub-sequence in string

<https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0>

<https://stackoverflow.com/questions/3260653/algorithm-to-find-top-10-search-terms/3260905#3260905>

<https://blog.datopia.io/2018/11/03/hitchhiker-tree/>



<http://yucoding.blogspot.com/2017/01/leetcode-question-range-sum-query.html>

<http://massivealgorithms.blogspot.com/>

<http://ruslanledesma.com/>

<http://algorithms.tutorialhorizon.com/>



## Fibonacci

https://habr.com/ru/post/261159/

<https://habr.com/ru/post/449616/> 

<https://habr.com/ru/post/450594/> 

<http://www.oranlooney.com/post/fibonacci/>

<https://news.ycombinator.com/item?id=19216356>

<https://www.reddit.com/r/programming/comments/d1tgmy/computing_fibonacci_numbers_in_olog_n_using/>  Computing Fibonacci Numbers In O(log n) using matrices and eigenvalues



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
