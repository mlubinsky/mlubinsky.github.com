import java.util.*;

class TreeNode {
   int val;
   TreeNode left;
   TreeNode right;
   TreeNode(int x) { val = x; }
}

public class Tree {
   static int size(TreeNode root){
      if (null == root) return 0;
      return 1+size(root.left)+size(root.right);
   }

   public int getHeight(TreeNode root) {
		if (root == null) return 0;
		int left = getHeight(root.left);
		int right = getHeight(root.right);
		if (left == -1 || right == -1) return -1;
		if (Math.abs(left - right) > 1)  return -1;
		return Math.max(left, right) + 1;
   }

   public static void inOrder(TreeNode root){
       if (null == root) return;
       inOrder(root.left);
       System.out.print(root.val+" ");
       inOrder(root.right);
   }
   public static void postOrder(TreeNode root){
        if (null == root) return;
        postOrder(root.left);
        postOrder(root.right);
        System.out.print(root.val+" ");
   }

   public static void preOrder(TreeNode root){
         if (null == root) return;
         System.out.println(root.val+" ");
         preOrder(root.left);
         preOrder(root.right);

   }
   public static void LevelOrder(TreeNode root){   //breth first
       if (null == root) return;
       Queue<TreeNode> queue = new LinkedList<>();
       queue.add(root);
       while(!queue.isEmpty()){
           TreeNode node =queue.poll();
           if (node.left != null)  queue.add(node.left);
           if (node.right != null) queue.add(node.right);
           System.out.print(node.val+" ");
       }
   }

   public static ArrayList<Integer> preorderNoRecursion(TreeNode root) {  //parent node processed first!
      ArrayList<Integer> returnList = new ArrayList<Integer>();
      if(root == null)
         return returnList;
      Stack<TreeNode> stack = new Stack<TreeNode>();
      stack.push(root);
      while(!stack.empty()){
         TreeNode n = stack.pop();
         returnList.add(n.val);
         if(n.right != null){  //push right childer first, so it processed after left
            stack.push(n.right);
         }
         if(n.left != null){
            stack.push(n.left);
         }
   }
      return returnList;
   }
//-------------

public static ArrayList<Integer> inorderNoRecursion(TreeNode root) {   // left child - parent - right child
    ArrayList<Integer> lst = new ArrayList<Integer>();
      if(root == null)
         return lst;

      Stack<TreeNode> stack = new Stack<TreeNode>();
//      stack.push(root);

      TreeNode p = root;
      while(!stack.empty() || p != null){
         if(p != null){
            stack.push(p);
            p = p.left;
         }else{
            TreeNode t = stack.pop();
            lst.add(t.val);
            p = t.right;
        }
     }

/*
   while(!stack.isEmpty()){
      TreeNode top = stack.peek();
      if(top.left!=null){
         stack.push(top.left);
         top.left=null;
      }else{
         lst.add(top.val);
         stack.pop();
         if(top.right!=null){
            stack.push(top.right);
         }
      }
   }
*/
   return lst;
}
//------------
public static ArrayList<Integer> postorderNoRecursion(TreeNode root) {
      ArrayList<Integer> lst = new ArrayList<Integer>();
      if(root == null)
         return lst;

      Stack<TreeNode> stack = new Stack<TreeNode>();
      stack.push(root);
/*
      while(!stack.isEmpty()) {
           TreeNode temp = stack.peek();
           if(temp.left==null && temp.right==null) {
               TreeNode pop = stack.pop();
               lst.add(pop.val);
            } else {
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
return lst;
*/
      TreeNode prev = null;
      while(!stack.empty()){
         TreeNode curr = stack.peek();
         // go down the tree.
         //check if current node is leaf, if so, process it and pop stack,
         //otherwise, keep going down
         if(prev == null || prev.left == curr || prev.right == curr){
            //prev == null is the situation for the root node
            if(curr.left != null){
               stack.push(curr.left);
            }else if(curr.right != null){
               stack.push(curr.right);
            }else{
               stack.pop();
               lst.add(curr.val);
            }
            // go up the tree from left node  to check if there is a right child
            // if yes, push it to stack otherwise, process parent and pop stack
         } else if(curr.left == prev){
            if(curr.right != null){
               stack.push(curr.right);
            }else{
               stack.pop();
               lst.add(curr.val);
            }
         //go up the tree from right node
         //after coming back from right node, process parent node and pop stack.
         }else if(curr.right == prev){
            stack.pop();
            lst.add(curr.val);
         }
         prev = curr;
      }
      return lst;


}
//------------
public static boolean isValidBST(TreeNode root) {
    return validate(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
}
  public static boolean validate(TreeNode root, int min, int max) {
    if (root == null) {
       return true;
    }
    // not in range
    if (root.val <= min || root.val >= max) {
       return false;
    }
      // left subtree must be < root.val && right subtree must be > root.val
    return validate(root.left, min, root.val) && validate(root.right,  root.val, max);

}

public static int maxDepth(TreeNode root) {
   if(root==null)
      return 0;
   int leftDepth = maxDepth(root.left);
   int rightDepth = maxDepth(root.right);
   int bigger = Math.max(leftDepth, rightDepth);
   return bigger+1;
}
//------------------------------------------------------
public static List<String> binaryTreePaths(TreeNode root) {
   ArrayList<String> finalResult = new ArrayList<String>();
   if(root==null)
      return finalResult;
   ArrayList<String> curr = new ArrayList<String>();
   ArrayList<ArrayList<String>> results = new ArrayList<ArrayList<String>>();
   dfs(root, results, curr);
   for(ArrayList<String> al : results){
      StringBuilder sb = new StringBuilder();
      sb.append(al.get(0));
      for(int i=1; i<al.size();i++){
         sb.append("->"+al.get(i));
      }
      finalResult.add(sb.toString());
   }
   return finalResult;
}

public static void dfs(TreeNode root, ArrayList<ArrayList<String>> list, ArrayList<String> curr){
   curr.add(String.valueOf(root.val));
   if(root.left==null && root.right==null){
      list.add(curr);
      return;
   }
   if(root.left!=null){
      ArrayList<String> temp = new ArrayList<String>(curr);
      dfs(root.left, list, temp);
   }
   if(root.right!=null){
      ArrayList<String> temp = new ArrayList<String>(curr);
      dfs(root.right, list, temp);
   }
}
//--------------------
public static TreeNode LCA_BST(TreeNode root, TreeNode p, TreeNode q){
    TreeNode m = root;
    if (root == null) return root;

    if(m.val > p.val && m.val < q.val){
        return m;
    }else if(m.val>p.val && m.val > q.val){
        return LCA_BST(root.left, p, q);
    }else if(m.val<p.val && m.val < q.val){
        return LCA_BST(root.right, p, q);
    }
    return root;
}
//-------------------------
public static TreeNode LCA(TreeNode root, TreeNode p, TreeNode q) {

    if( root ==null || root==p || root==q)
        return root;

    TreeNode l = LCA(root.left, p, q);
    TreeNode r = LCA(root.right, p, q);

    return l == null ? r:l;
}
//-------------------------------------
   public static void main(String[] args) {
      TreeNode t1= new TreeNode(1);
      TreeNode t2= new TreeNode(2);
      TreeNode t3= new TreeNode(3);
      TreeNode t4= new TreeNode(4);
      TreeNode t5= new TreeNode(5);
      t1.left=t2;
      t1.right=t3;
      t2.left=t4;
      t2.right=t5;


      System.out.println("LEVEL ORDER");
      LevelOrder(t1);

      System.out.println("\nTree size="+size(t1));
      System.out.println("\nPREORDER");
      ArrayList<Integer> preorderList = preorderNoRecursion(t1);
      for (Integer c : preorderList) {
         System.out.print(c);
      }

      System.out.println("\nTree size="+size(t1));
      System.out.println("\nPREORDER");
      preorderList = preorderNoRecursion(t1);
      for (Integer c : preorderList) {
         System.out.print(c);
      }

      System.out.println("\nTree size="+size(t1));
      System.out.println("\nIN ORDER");
      ArrayList<Integer> inorderList = inorderNoRecursion(t1);
      for (Integer c : inorderList) {
         System.out.print(c);
      }
      System.out.println("\nTree size="+size(t1));

      System.out.println("\nIN ORDER");
      inorderList = inorderNoRecursion(t1);
      for (Integer c : inorderList) {
         System.out.print(c);
      }
      System.out.println("\nTree size="+size(t1));
      System.out.println("\nPOST ORDER");
      ArrayList<Integer> postorderList = postorderNoRecursion(t1);
      for (Integer c : postorderList) {
         System.out.print(c);
      }

      System.out.println("\nTree size="+size(t1));
      System.out.println("\nPOST ORDER");
      postorderList = postorderNoRecursion(t1);
      for (Integer c : postorderList) {
         System.out.print(c);
      }


      System.out.println("\nTree size="+size(t1));
      System.out.println("Max Tree depth="+maxDepth(t1));

      System.out.println("isValidBST="+isValidBST(t1));
      if (isValidBST(t1)){
          TreeNode lca= LCA_BST(t1,t3,t5);
          if (lca !=null)
               System.out.println("LCA_BST for t3 and t5 is " + lca.val);
      }
      TreeNode lca= LCA(t1,t3,t5);
      System.out.println("LCA for t3 and t5 is " + lca.val);

      System.out.println("\n All paths from root to nodes");
      List<String> all_paths = binaryTreePaths(t1);
      System.out.println(all_paths);
   }   //end of main
}
