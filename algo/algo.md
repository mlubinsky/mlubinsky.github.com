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
