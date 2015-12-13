http://codereview.stackexchange.com/questions/48518/depth-first-search-breadth-first-search-implementation

Depth-first search:
-----------------------
Step 1: Push the root node in the Stack.  
Step 2: Loop until stack is empty. 
Step 3: Peek the node of the stack.  
Step 4: If the node has unvisited child nodes, get the unvisited child node, mark it as traversed and push it on stack.   
Step 5: If the node does not have any unvisited child nodes, pop the node from the stack.

Bread-first search:
-----------------------
Step 1: Push the root node in the Queue.

Step 2: Loop until the queue is empty.

Step 3: Remove the node from the Queue.

Step 4: If the removed node has unvisited child nodes, mark them as visited and insert the unvisited children in the queue.


http://opendatastructures.org/versions/edition-0.1e/ods-java/12_Graphs.html

http://www.geeksforgeeks.org/graph-and-its-representations/

http://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c

https://en.wikipedia.org/wiki/Adjacency_list

Adjacency matrix: 
-------------------------------------------------------------------
The advantages of representing the edges using adjacency matrix are: 
Simplicity in implementation as you need a 2-dimensional array 
Creating edges/removing edges is also easy as you need to update the Booleans 
The drawbacks of using the adjacency matrix are:  

Increased memory as you need to declare N*N matrix where N is the total number of nodes.
Redundancy of information, i.e. to represent an edge between A to B and B to A, it requires to set two Boolean flag in an adjacency matrix. 


