import java.util.Comparator;
import java.util.PriorityQueue;
public class PriorityQueueTest {

  static class PQsort implements Comparator<Integer> {
      public int compare(Integer one, Integer two) {  return two - one;  }
  }

  // find top K elements in stream - O (log(k) * n)  keep smallest elem in root
  static void find_top_k_(InputStream in, int k, PriorityQueue<Integer> heap) throws IOException{
    int val=0;
    while (heap.size()<k && (val=in.read()) !=-1){
        heap.add(val);
    }
    while (in.available()>0 && (val=in.read()) !=-1){
        if (val > heap.peak()){
            heap.poll();
            heap.add(val);
        }
        heap.add(val);
    }


  }

  public static void main(String[] args) {
    int[] ia = { 1, 10, 5, 3, 4, 7, 6, 9, 8 };
    PriorityQueue<Integer> pq1 = new PriorityQueue<Integer>();
    // use offer() method to add elements to the PriorityQueue pq1
    for (int x : ia) {
       pq1.offer(x);
    }
    System.out.println("pq1: " + pq1);
    PQsort pqs = new PQsort();
    PriorityQueue<Integer> pq2 = new PriorityQueue<Integer>(10, pqs);
    // In this particular case, we can simply use Collections.reverseOrder()
    // instead of self-defined comparator
    for (int x : ia) {
       pq2.offer(x);
    }
    System.out.println("pq2: " + pq2);
    // print size
    System.out.println("size: " + pq2.size());
    // return highest priority element in the queue without removing it
    System.out.println("peek: " + pq2.peek());
    // print size
    System.out.println("size: " + pq2.size());
    // return highest priority element and removes it from the queue
    System.out.println("poll: " + pq2.poll());
    // print size
    System.out.println("size: " + pq2.size());
    System.out.print("pq2: " + pq2);
  }
}