## Dynamic programming

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


####  Maximum Sum Increasing subsequence

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

####    Min Cost Path on grid 

```  
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
 ``` 
    cost = [[1, 2, 3], 
            [4, 8, 2], 
            [1, 5, 3]] 
    print(minCost(cost, 2, 2)) 
```


### Min cost path - another version

https://github.com/charulagrl/data-structures-and-algorithms/blob/master/algorithm-questions/dynamic_programming/min_cost_path.py

  Time-complexity: O(m*n) where m, n are dimensions of the matrix

```
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
``` 
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
``` 
if __name__ =="__main__":    
    n = 5
    m = 5
    print(countPaths(n, m)) 
```   
 
### Coin exchange problem

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

Number of ways to get total n with coin[n] equals:
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
#### Egg drop
<https://habr.com/post/423679/>

<http://declanoller.com/2018/09/03/the-egg-drop-puzzle-brute-force-dynamic-programming-and-markov-decision-processes/>

