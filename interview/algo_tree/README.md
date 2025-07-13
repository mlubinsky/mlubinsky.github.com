### Tree algorithms
```python
#  determine if two trees are identical
# binary tree node has data, pointer to left child and a pointer to right child

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

### Check if binary tree is binary search tree
# --------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_binary_search_tree(root):
    def in_order_traversal(node, prev):
        if node is None:
            return True

        # Recursively check the left subtree
        if not in_order_traversal(node.left, prev):
            return False

        # Check if the current node's value is greater than the previous node's value
        if node.value <= prev[0]:
            return False

        prev[0] = node.value  # Update the previous value

        # Recursively check the right subtree
        return in_order_traversal(node.right, prev)

    prev = [float('-inf')]  # Initialize the previous value to negative infinity
    return in_order_traversal(root, prev)

# Example usage
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    if is_binary_search_tree(root):
        print("The binary tree is a Binary Search Tree (BST).")
    else:
        print("The binary tree is not a BST.")



### Post order without recursion using 2 stacks
# ---------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal(root):
    if root is None:
        return []

    result = []
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        result.append(node.value)

    return result

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = post_order_traversal(root)
    print("Post-order traversal:", result)



### In order traversal without recursion using stack
# ---------------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root is None:
        return []

    result = []
    stack = []

    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.value)
            current = current.right

    return result

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = in_order_traversal(root)
    print("In-order traversal:", result)



### Preorder traversal without recursion - using stack
#-----------------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_traversal(root):
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.value)

        # Push the right child first to ensure left child is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = depth_first_traversal(root)
    print("Depth-first traversal (pre-order):", result)


### Breadth first (LeVeL order) without recursion using queue
# -----------------------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = level_order_traversal(root)
    print("Level-order traversal:", result)

########################


### Diameter of binary tree
#----------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Result:
    def __init__(self):
        self.diameter = 0

def tree_diameter(root, result):
    if root is None:
        return 0

    left_height = tree_diameter(root.left, result)
    right_height = tree_diameter(root.right, result)

    # Calculate the diameter passing through the current node
    diameter_through_node = left_height + right_height

    # Update the maximum diameter found so far
    result.diameter = max(result.diameter, diameter_through_node)

    # Return the height of the subtree rooted at the current node
    return 1 + max(left_height, right_height)

def tree_max_diameter(root):
    result = Result()
    tree_diameter(root, result)
    return result.diameter

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    max_diameter = tree_max_diameter(root)
    print("Maximum distance between any two nodes (diameter) of the binary tree is:", max_diameter)



### Height of binary tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return -1  # Height of an empty tree is -1

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return 1 + max(left_height, right_height)

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    height = tree_height(root)
    print("Height of the binary tree is:", height)



## Least common accessor of 2 nodes (p,q) in binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findLCA(root, p, q):
    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left_lca = findLCA(root.left, p, q)
    right_lca = findLCA(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

# Helper function to check if a node with a given value exists in the tree
def nodeExists(root, value):
    if root is None:
        return False
    if root.val == value:
        return True
    return nodeExists(root.left, value) or nodeExists(root.right, value)

# Example usage
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = 5
    q = 1

    if nodeExists(root, p) and nodeExists(root, q):
        lca = findLCA(root, p, q)
        print("Least Common Ancestor of {} and {} is {}".format(p, q, lca.val))
    else:
        print("Nodes {} and/or {} do not exist in the tree.".format(p, q))
```
