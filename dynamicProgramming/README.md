## Dynamic programming

https://iagoleal.com/posts/dynamic-programming/

https://habr.com/ru/companies/otus/articles/819815/

https://qsantos.fr/2024/01/04/dynamic-programming-is-not-black-magic/

https://www.youtube.com/playlist?list=PLCiTDJays9rU7WmHIlEFZsXT_boyJ6oZu

https://medium.com/free-code-camp/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e

https://towardsdatascience.com/how-to-find-all-solutions-to-the-subset-sum-problem-597f77677e45

https://medium.com/@pv.safronov/dynamic-programming-is-simple-3-multi-root-recursion-c613dfcc15b4

https://betterprogramming.pub/a-systematic-approach-to-dynamic-programming-54902b6b0071

https://oddblogger.com/recursion-memoization-dynamic-programming-lcs-problem/

https://trekhleb.dev/blog/2018/dynamic-programming-vs-divide-and-conquer/

https://www.youtube.com/watch?v=BvwQe_9FUBQ (ru)

<https://skerritt.blog/dynamic-programming>

https://hiringfor.tech/2020/10/26/my-resources-for-dynamic-programming.html

<https://medium.freecodecamp.org/unmasking-bitmasked-dynamic-programming-25669312b77b>

https://github.com/charulagrl/data-structures-and-algorithms/tree/master/algorithm-questions/dynamic_programming

<https://habr.com/post/418867/> 

<https://habr.com/post/423939/>

<https://ngoldbaum.github.io/posts/dynamic-programming/>

<https://news.ycombinator.com/item?id=20285242>

<https://avikdas.com/2019/06/24/dynamic-programming-for-machine-learning-hidden-markov-models.html>

<https://avikdas.com/2019/04/15/a-graphical-introduction-to-dynamic-programming.html>

<https://medium.freecodecamp.org/unmasking-bitmasked-dynamic-programming-25669312b77b>

<https://blogarithms.github.io/articles/2019-03/cracking-dp-part-one>

<https://www.geeksforgeeks.org/min-cost-path-dp-6/>

<https://macnovicetomaster.wordpress.com/2019/06/05/dynamic-programming-practice-problems/>

<https://skerritt.blog/dynamic-programming/>

<https://hackernoon.com/dynamic-programming-for-brute-forcers-36f26c2466cf>

<https://medium.com/@codingfreak/top-50-dynamic-programming-practice-problems-4208fed71aa3>

<https://lukasmericle.github.io/dynprotut/

https://github.com/YaokaiYang-assaultmaster/LeetCode (Java)


https://jimmy-shen.medium.com/

#### Template for any substring problem

https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems

https://github.com/YaokaiYang-assaultmaster/LeetCode/blob/master/GeneralizedMethod/%5BImportant%5DA%20template%20that%20can%20solve%20most%20%22substring%22%20problems.md

https://liuzhenglaichn.gitbook.io/algorithm/array/sliding-window

####  Maximum Sum Increasing subsequence

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

#### Cut the rod

https://github.com/charulagrl/data-structures-and-algorithms/blob/master/algorithm-questions/dynamic_programming/cutting_a_rod.py

Given a rod of length n   and an array of prices that contains prices of all pieces of size smaller than n.

Determine the maximum value obtainable by cutting up the rod and selling the pieces.
```python
def cutting_a_rod_dynamic(values, length):
	
	soln = [0] * (length+1)

	for i in range(1, length+1):
		soln[i] = -sys.maxint
		for j in range(i):
			res = soln[i-j-1] + values[j]
			if res > soln[i]:
				soln[i] = res

	return soln[length]
```
Another solution from https://www.techiedelight.com/rod-cutting/

Function to find the best way to cut a rod of length `n`  
 where the rod of length `i` has a cost `price[i-1]`
```python
def rodCut(price, n):
 
    # `T[i]` stores the maximum profit achieved from a rod of length `i`
    T = [0] * (n + 1)
 
    # consider a rod of length `i`
    for i in range(1, n + 1):
        # divide the rod of length `i` into two rods of length `j`
        # and `i-j` each and take maximum
        for j in range(1, i + 1):
            T[i] = max(T[i], price[j - 1] + T[i - j])
 
    # `T[n]` stores the maximum profit achieved from a rod of length `n`
    return T[n]
 
 
if __name__ == '__main__':
 
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 4        # rod length
 
    print('Profit is', rodCut(price, n))
 ``` 

####    Min Cost Path on grid 
https://github.com/StBogdan/PythonWork/blob/master/Leetcode/64.py

```python
def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sm = [[0] * cols for _ in range(rows)]
        # print(sm)

        ts = 0
        for col in range(cols):
            ts += grid[0][col]
            sm[0][col] = ts

        ts = 0
        for row in range(rows):
            ts += grid[row][0]
            sm[row][0] = ts

        for row in range(1, rows):
            for col in range(1, cols):
                to_get_here = min(sm[row - 1][col], sm[row][col - 1])
                sm[row][col] = to_get_here + grid[row][col]

        # for row in sm:
        #     print(row)
        return sm[rows - 1][cols - 1]
```


Min Cost Path on grid: another solution
```python
def minCost(cost, m, n): 
  
    # Instead of following line, we can use int tc[m+1][n+1] or 
    # dynamically allocate memory to save space.  
    
    R = 3
    C = 3
    tc = [[0 for x in range(C)] for x in range(R)] 
  
    tc[0][0] = cost[0][0] 
  
    # Initialize first column of total cost(tc) array 
    for i in range(1, m+1): 
        tc[i][0] = tc[i-1][0] + cost[i][0] 
  
    # Initialize first row of tc array 
    for j in range(1, n+1): 
        tc[0][j] = tc[0][j-1] + cost[0][j] 
  
    # Construct rest of the tc array 
    for i in range(1, m+1): 
        for j in range(1, n+1): 
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] 
  
    return tc[m][n] 
 ``` 
  Driver program to test above functions 
 ```python
    cost = [[1, 2, 3], 
            [4, 8, 2], 
            [1, 5, 3]] 
    print(minCost(cost, 2, 2)) 
```


### Min cost path - another version

<https://github.com/charulagrl/data-structures-and-algorithms/blob/master/algorithm-questions/dynamic_programming/min_cost_path.py>

Time-complexity: O(m*n) where m, n are dimensions of the matrix

```python
import sys
def min_cost_dynamic(cell):
	 
	m = len(cell)
	n = len(cell[0])

	for i in range(m):
		for j in range(n):
			if i > 0 or j > 0:
				min_left = cell[i-1][j] if i-1 >=0 else sys.maxint
				min_top = cell[i][j-1] if j-1 >=0 else sys.maxint
				min_diagonal = cell[i-1][j-1] if j-1 >=0 and i-1 >=0 else sys.maxint

				cell[i][j] += min(min_left, min_top, min_diagonal)

	return cell[m-1][n-1]
```

### Count number of ways to reach   mat[m-1][n-1] from mat[0][0]   in a matrix mat[][] 

 Return    number of way from top-left to mat[m-1][n-1] 
```python 
def countPaths(m, n): 
  
    dp = [[0 for i in range(m + 1)]  
             for j in range(n + 1)] 
      
    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
            if (i == 1 or j == 1): 
                dp[i][j] = 1
            else: 
                dp[i][j] = (dp[i - 1][j] + 
                            dp[i][j - 1])              
      
    return dp[m][n] 
```

 Driver code 
```python
if __name__ =="__main__":    
    n = 5
    m = 5
    print(countPaths(n, m)) 
```   
 
### Coin exchange problem

https://github.com/donnemartin/interactive-coding-challenges/tree/master/recursion_dynamic

https://github.com/donnemartin/interactive-coding-challenges/tree/master/recursion_dynamic/coin_change_ways

https://github.com/charulagrl/data-structures-and-algorithms/blob/master/algorithm-questions/dynamic_programming/coin_change.py

Determine the total number of unique ways to make n cents, given coins of denominations less than n cents.
Example:
```
coins: [1, 2, 3], 
target= 5 -> 5
number of unique ways = 5

1+1+1+2=5
1+1+3=5
1+2+2=5
2+2+1=5
3+2=5
```

We'll use a bottom-up dynamic programming approach.

The rows (i) represent the coin values.
The columns (j) represent the totals.
```
  -------------------------
  | 0 | 1 | 2 | 3 | 4 | 5 |
  -------------------------
0 | 1 | 0 | 0 | 0 | 0 | 0 |
1 | 1 | 1 | 1 | 1 | 1 | 1 |
2 | 1 | 1 | 2 | 2 | 3 | 3 |
3 | 1 | 1 | 2 | 3 | 4 | 5 |
  -------------------------
```
Number of ways to get total n with coin[n] equals:
```
* Number of ways to get total n with coin[n - 1] plus
* Number of ways to get total n - coin[n]

if j == 0:
    T[i][j] = 1
if row == 0:
    T[i][j] = 0
if coins[i] >= j
    T[i][j] = T[i - 1][j] + T[i][j - coins[i]]
else:
    T[i][j] = T[i - 1][j]

The answer will be in the bottom right corner of the matrix.

Complexity:

Time: O(i * j)
Space: O(i * j)
```

```python
def coin_change_dynamic(coins, total):
	'''Return the number of ways to to make the change using dynamic approach'''
	result = [[0] * len(coins) for i in range(total+1)] 

	for i in range(total+1):
		for j, coin in enumerate(coins):
			if not i:
				result[i][j] = 1
			else:
				# When the coin is part of the solution
				x = result[i-coin][j] if i - coin >= 0 else 0
				# When coin is not part of the solution
				y = result[i][j-1] if j >= 1 else 0
				
				# total count
				result[i][j] = x + y

	return result[total][len(coins)-1]

```

#### best-time-to-buy-and-sell-stock 
```python
prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
result = 0
minSofar = prices[0]
for i in range(1, len(prices)):
    minSofar = min(minSofar, prices[i])
    result = max (result, prices[i] - minSofar)

print result
```

https://github.com/StBogdan/PythonWork/blob/master/Leetcode/188.py

Stock cell/buy 2 times
https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

https://stackoverflow.com/questions/44634395/maximum-profit-by-buying-and-selling-a-share-exactly-k-times


#### Egg drop
<https://habr.com/post/423679/>

<http://declanoller.com/2018/09/03/the-egg-drop-puzzle-brute-force-dynamic-programming-and-markov-decision-processes/>

