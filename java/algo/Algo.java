import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;
import java.util.Queue;
import java.util.Stack;
import java.io.IOException;

//Tree
class Node {
 int value;
 Node left;
 Node right;
 Node(int value) {this.value = value;}
 Node(int value, Node left, Node right) {
    this.value = value; 
    this.left=left; 
    this.right=right;
 }
 void print(){
  System.out.println("current="+value);
  if (left != null) System.out.println("left="+left.value);
  if (right != null) System.out.println("right="+right.value);

 }
 
 static int size(Node root) {
    if (null == root) {return 0;}
    return 1 + size(root.left) + size(root.right);
 }

 static int size_iterative(Node root) {
   if (null == root) {return 0;}
   int count = 0;
   Queue<Node> q = new LinkedList<Node>();  //bread first
   q.add(root);
   while (!q.isEmpty()) {
     Node front = q.poll();
     count++;
     if (null != front.left) {q.add(front.left);}
     if (null != front.right) {q.add(front.right);}
   }
   return count;
 }

 
 static int depth(Node root) { 
     if (null == root) {return 0;}
     return 1 + Math.max(depth(root.left),
     depth(root.right));
 }

 static int depth_iterative(Node root) {
    if (null == root) {return 0;}
    int max_depth = 0;
    Set<Node> visited = new HashSet<Node>();
    Stack<Node> s = new Stack<Node>();
    s.push(root);
    while (!s.isEmpty()) {
      Node top = s.peek();
      if (null != top.left && !visited.contains(top.left)) {
         s.push(top.left);
      } else if (null != top.right && !visited.contains(top.right)) {
         s.push(top.right);
      } else {
        visited.add(top);
        max_depth = Math.max(max_depth, s.size());
        s.pop();
      }
    } //end of while
    return max_depth;
 }

 Node insert_bst(Node root, int val) {
    if (null == root) {    return new Node(val);}
    if (val < root.value) {
      root.left = insert_bst(root.left, val);
    } else {
     root.right = insert_bst(root.right, val);
    }
    return root;
 }


 Node find_bst(Node root, int val) {
  if (null == root || root.value == val) {return root;}
  if (val < root.value) {return find_bst(root.left, val);}
  return find_bst(root.right, val);
 }

// is tree balanced?
 boolean is_balanced_recursive(Node root) {
   if (null == root) {return true;}
   if (!is_balanced_recursive(root.left) || !is_balanced_recursive(root.right)) {return false;}
   int left_depth = depth(root.left);
   int right_depth = depth(root.right);
   return Math.abs(right_depth - left_depth) <= 1;
 }

 //linear complexity
 static boolean balanced_depth(Node root, int[] depth) {
   if (null == root) {
     depth[0] = 0;
     return true;
   }
   int[] left = new int[1];
   int[] right = new int[1];
   if (!balanced_depth(root.left, left)) {
     return false;
   }
   if (!balanced_depth(root.right, right)) {
    return false;
   }
   depth[0] = 1 + Math.max(left[0], right[0]);
   if (Math.abs(left[0] - right[0]) > 1) {
     return false;
   }
   return true;
 }


 static boolean is_balanced(Node root) {
     int[] depth = new int[1];
     return balanced_depth(root, depth);
 }

 boolean find_path(Node root,Node target, List<Node> path) {
    if (target == null) {return true;}
    while (null != root && (path.isEmpty() || path.get(path.size() - 1) != target)) {
       path.add(root);
       if (target.value < root.value) { 
  	     root = root.left;
       } else {
         root = root.right;
       }
     }

     if (path.get(path.size() - 1) == target) {
       return true;
     } else {
       path.clear();
       return false;
     }
  } //end of find path

  // there are 3 ways to traverse tree in depth-first order:
  public static void preOrder( Node root) { 
      
     if (root == null) { return; }; 
     System.out.println( root.value); 
     preOrder( root.left); 
     preOrder( root.right); 
  }

  public static void inOrder( Node root) { 
      
 	   if (root == null) { return; }; 
 	   inOrder( root.left); 
 	   System.out.println( root.value); 
 	   inOrder( root.right); 
  }

  public static void postOrder( Node root) {
    //System.out.println("postOrder recursive void");  
 	  if (root == null) { return; }; 

 	  postOrder( root.left); 
 	  postOrder( root.right);
    System.out.println( root.value);
  }

static List<Integer> inOrderStack(Node root) {
    System.out.println("inorderStack - returns List<>");
    List<Integer> result = new ArrayList<Integer>();
    if(root==null)
        return result;

    Stack<Node> stack = new Stack<Node>();
    stack.push(root);
  
    while(!stack.isEmpty()){
        Node top = stack.peek();
        if(top.left!=null){
            stack.push(top.left);
            top.left=null;
        }else{
            //System.out.println("Inorder right :"+top.value);
            result.add(top.value);
            stack.pop();
             if(top.right!=null){
                stack.push(top.right);
             }
        }
    }
     
    return result;
  }

  public static List<Integer> postOrderStack(Node root) {
    System.out.println("postorderStack - returns List<Integer>");
    List<Integer> res = new ArrayList<Integer>();
 
    if(root==null) {
        return res;
    }
 
    Stack<Node> stack = new Stack<Node>();
    stack.push(root);
 
    while(!stack.isEmpty()) {
        Node temp = stack.peek();
        if(temp.left==null && temp.right==null) {
            Node pop = stack.pop();
            res.add(pop.value);
        }
        else {
            if(temp.right!=null) {
                stack.push(temp.right);
                temp.right = null;
            }
 
            if(temp.left!=null) {
                stack.push(temp.left);
                temp.left = null;
            }
        }
    }
 
    return res;
 } // end of postorder stack
  
 static void postOrderStack2(Node root)   {
        System.out.println("-----void postOrderStack2 stack ----"); 
        if (root == null)
            return;
 
        final Stack<Node> stack = new Stack<Node>();
        Node node = root;
 
        while (!stack.isEmpty() || node != null)
        {
            while (node != null)
            {
                if (node.right != null)
                     stack.add(node.right);
                stack.add(node);
                node = node.left;
            }
 
            node = stack.pop();
 
            if (node.right != null && !stack.isEmpty()
                    && node.right == stack.peek())
            {
                Node nodeRight = stack.pop();
                stack.push(node);
                node = nodeRight;
            } else
            {
                System.out.print(node.value + " ");
                node = null;
            }
        }
        System.out.println('\n');
 }

 public static ArrayList<Integer> preOrderStack(Node root) {
        System.out.println("preorderStack");
        ArrayList<Integer> returnList = new ArrayList<Integer>();
 
        if(root == null)
            return returnList;
 
        Stack<Node> stack = new Stack<Node>();
        stack.push(root);
 
        while(!stack.empty()){
            Node n = stack.pop();
            returnList.add(n.value);
 
            if(n.right != null){
                stack.push(n.right);
            }
            if(n.left != null){
                stack.push(n.left);
            }
 
        }
        return returnList;
    } //end of preoprderstack

}; //END_OF_CLASS

//==========================
// Double Linked List
class DllNode {
  DllNode prev;
  DllNode next;
  int data;
  DllNode(int data) { this(null, null, data);}  
  // Node(int value) {this.value = value;}
  DllNode( DllNode prev, DllNode next, int data) {
    this.prev = prev; 
    this.next=next; 
    this.data=data;
 }    

  DllNode insert(DllNode head, int data) {
    if (null == head) {   return new DllNode(data);}
    DllNode insertion = new DllNode(head.prev, head, data);
    insertion.prev.next = insertion;
    insertion.next.prev = insertion;
    return insertion;
  }

  DllNode find(DllNode head, int value) {
    DllNode current = head;
    while (null != current && current.data != value) {
      current = current.next;
      if (current.data == head.data) {return null;}
    }
    return current;
  }

  DllNode remove(DllNode head, DllNode target) {

    if (head != null&& head.next == head && head == target) {return null;}
    target.prev.next = target.next;
    target.next.prev = target.prev;
    if (head == target) {head = target.next;}
    return head;
  }

  DllNode reverse(DllNode head) {
    if (null == head) {return null;}
    if (head.next == head.prev) {return head;}
    DllNode tail = head;
    do {
       DllNode temp = tail.next;
       tail.next = tail.prev;
       tail.prev = temp;
       tail = temp;
    } while (tail.data != head.data);
    return head.next;
  }

  boolean is_palindrome(DllNode head) {
     if (null == head || head.data == head.next.data) {return true;}
     DllNode tail = head.prev;
     do {
        if (head.data != tail.data) {return false;}
        head = head.next;
        tail = tail.prev;
     } while (head.data != tail.data && head.data != tail.next.data);
     return true;
  }

} // end of class DllNode

//============= Single Linked List
class LNode {
   LNode next;
   int data;
   LNode(int data) { this(null, data);}
   LNode(LNode head, int data) {
      this.next = head;
      this.data = data;
   }
   void print(){
     LNode l = this;
     do{
       System.out.print(l.data+ " - ");
       l = l.next;
      } while (l != null) ;
      System.out.println('\t'); 
   }
   
   LNode insert(LNode head, int data) {
     return new LNode(head, data);
   }
 
   LNode find(LNode head, int value) {
      while (null != head && head.data != value) {
        head = head.next;
      }
      return head;
   }

  LNode remove(LNode head, LNode target) {
   while (head != null && head == target) {head = head.next;}
   if (null == head) {return null;}
   LNode current = head;
   while (null != current.next) {
       if (current.next == target) { current.next = current.next.next;}
       current = current.next;
   }
   return head;
  }

  LNode middle(LNode head) {
   LNode trailing = head;
   while (null != head) {
       head = head.next;
       if (null != head) {
           head = head.next;
           trailing = trailing.next;
       }
   }
   return trailing;
  }
/*
Node kth_from_end(Node head, int k) {
   Node trailing = head;
   while (k— > 0 && null != head) {
      head = head.next;
   }
   while (null != head && null != head.next) {
      head = head.next;
      trailing = trailing.next;
   }
   return trailing;
}
*/
  LNode remove_values(LNode head, int value) {
     while (head != null && head.data == value) {head = head.next;}
     if (null == head) {return null;}
      LNode current = head;
      while (null != current.next) {
         if (current.next.data == value) {current.next = current.next.next;}
         current = current.next;
      }
      return head;
  }

  static LNode reverse(LNode head) {
    System.out.println("reverse linked list");
    LNode prev = null;
    while (null != head) {
       LNode temp = head.next;
       head.next = prev;
       prev = head;
       head = temp;
    }
    return prev;
  }

  static boolean is_palindrome(LNode head) {  // ERROR
     LNode temp = head;
     Stack<LNode> s = new Stack<LNode>();
     while (null != temp) {
        System.out.println("push to stack ="+temp.data); 
        s.push(temp);
        temp = temp.next;
     }
     while (!s.empty()) {
        System.out.println("head ="+head.data);
        System.out.println("s.peek ="+s.peek().data);
        if (head.data != s.peek().data) {return false;}
        s.pop();
        head = head.next;
     }
     return true;
  }
  
  static boolean is_loop(LNode head) {
    if (null == head) {return false;}
    LNode trailing = head;
    LNode leading = head;
    while (null != leading) {
        leading = leading.next;
        if (trailing == leading) {return true;}
        trailing = trailing.next;
        if (null != leading) {leading = leading.next;}
    }
    return false;
  }

}  //end of class Node

public class Algo{
 
    public static void main(String args[]) throws IOException {
        System.out.println("***** Algorithms - linked list *****");
        LNode  l1_tail=new LNode(1);
        LNode  l2=new LNode(l1_tail,2);
        LNode  l3=new LNode(l2,3);
        l3.print();
        LNode reversed = LNode.reverse(l3);
        reversed.print();
        System.out.println("is_loop="+LNode.is_loop(reversed));
        System.out.println("is_palindrome="+LNode.is_palindrome(reversed));
        //--------------------------
        System.out.println("***** Algorithms - Binary Tree  ******");
        Node n1=new Node(1);
        Node n2=new Node(2);
        Node n3=new Node(3,n1,n2);
        n3.print();
        System.out.println("Binary tree depth recursive=" +Node.depth(n3));  
        System.out.println("Binary tree depth iterative=" +Node.depth_iterative(n3)); 
        System.out.println("Binary tree size recursive=" +Node.size(n3));
        System.out.println("Binary tree size iterative=" +Node.size_iterative(n3));
        System.out.println("Binary is_Balanced=" +Node.is_balanced(n3));
        
        System.out.println("Binary tree recursine inOrder");
        Node.inOrder(n3);
        System.out.println("Binary tree recursine inOrder");
        Node.inOrder(n3);
        
        System.out.println("Binary tree recursive preOrder");
        Node.preOrder(n3); 
        System.out.println("Binary tree recursive preOrder");
        Node.preOrder(n3); 

  
        System.out.println("Binary tree recursive postOrder");
        Node.postOrder(n3); 
        System.out.println("Binary tree recursive postOrder");
        Node.postOrder(n3); 

        //System.out.println("Binary tree size recursive before stack=" +Node.size(n3));
        //n3.print();
        //List<Integer> lst1 = Node.inOrderStack(n3);
        //System.out.println(lst1);
        //n3.print();
        //System.out.println("Binary tree size recursive after stack=" +Node.size(n3));

        //List<Integer> lst2 = Node.inOrderStack(n3);
        //System.out.println(lst2);        
        //System.out.println("Binary tree size recursive=" +Node.size(n3));
        
        //List<Integer> l_3 = Node.postOrderStack(n3);
        //System.out.println(l_3);
        
        //List<Integer> l4 = Node.postOrderStack(n3);
        //System.out.println(l4);
      
        //List<Integer> l5 = Node.preOrderStack(n3);  ERROR
        //System.out.println(l5);
              
        Node.postOrderStack2(n3); 
         
    }
}    