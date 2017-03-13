import java.util.*;

class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
    next = null;
  }
 }
 public class ListTest {
 public static ListNode reverseOrder(ListNode head) {
    if (head == null || head.next == null) {
       return head;
    }
    ListNode pre = head;
    ListNode curr = head.next;
    while (curr != null) {
       ListNode temp = curr.next;
       curr.next = pre;
       pre = curr;
       curr = temp;
    }
    // set head node’s next
    head.next = null;
    return pre;
}

  public static void printList(ListNode n) {
    System.out.println("------");
    while (n != null) {
       System.out.print(n.val);
       n = n.next;
    }
    System.out.println();
  }

public static boolean hasCycle(ListNode head) {
      ListNode fast = head;
      ListNode slow = head;
      if(head == null)
         return false;
      if(head.next == null)
         return false;
      while(fast != null && fast.next != null){
         slow = slow.next;
         fast = fast.next.next;
         if(slow == fast)
            return true;
      }
      return false;
   }


public static void main(String[] args) {

      ListNode l1 = new ListNode(1);
      ListNode l2 = new ListNode(2);
      ListNode l3 = new ListNode(3);
      l1.next  = l2;
      l2.next  = l3;
      System.out.println(" List");
      printList(l1);
      System.out.println(" Reversed");
      printList(reverseOrder(l1));
      System.out.println(" has cycle="+hasCycle(l1));

 }
}