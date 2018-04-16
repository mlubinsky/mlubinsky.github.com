///https://www.programcreek.com/2013/02/leetcode-merge-k-sorted-lists-java/

import java.util.*;

public class MergeSortedLists {

 public static ListNode mergeSorted(List[] lists) {
    if(lists==null||lists.length==0)
        return null;
 
    PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(new Comparator<List>(){
        public int compare(List l1, List l2){
            return l1.val - l2.val;
        }
    });
 
    ListNode head = new ListNode(0);
    ListNode p = head;
 
    for(ListNode list: lists){
        if(list!=null)
            queue.offer(list);
    }    
 
    while(!queue.isEmpty()){
        ListNode n = queue.poll();
        p.next = n;
        p=p.next;
 
        if(n.next!=null)
            queue.offer(n.next);
    }    
 
    return head.next;
 
}

 
 
  public static void main(String[] args) {
    
     List<Integer> l1 = new ArrayList<>();
     for (int i=0; i<5; i++){
        l1.add(i, i);  
     }
     System.out.println(l1); 
     List<Integer> l1 = new ArrayList<>();

     List<Integer> l2 = new ArrayList<>();
     for (int i=0; i<5; i++){
        l2.add(i, i-2);  
     }
     System.out.println(l2); 
     
     List result = mergeSorted(new List[] { l1, l2 });
     System.out.println(result));
  }
 } // end of class
