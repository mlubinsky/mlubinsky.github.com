import java.util.Map;
import java.util.List;
import java.util.Set;
import java.util.Queue;

import java.util.HashSet;
import java.util.TreeSet;

import java.util.Comparator;
import java.util.SortedSet;
import java.util.HashMap;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Map.Entry;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentLinkedQueue;

public class D {

   public static void main(String[] args)  throws InterruptedException {
      Map<String,Integer> entry = new HashMap<String, Integer>();   //maps entry name to capacity
      entry.put("a",2);
      entry.put("b",1);
      entry.put("c",3);
      entry.put("d",1);
      entry.put("e",0);
      entry.put("f",0);

    Graph.Edge[] connections = {
      new Graph.Edge("a", "b", 7),
      new Graph.Edge("a", "c", 9),
      new Graph.Edge("a", "d", 19),
      new Graph.Edge("a", "f", 14),
      new Graph.Edge("b", "c", 10),
      new Graph.Edge("b", "d", 15),
      new Graph.Edge("c", "d", 11),
      new Graph.Edge("c", "f", 2),
      new Graph.Edge("d", "e", 6),
      new Graph.Edge("e", "f", 9),
   };

      int feePerMinInCents=100; //$1
      Graph g = new Graph(entry, connections, feePerMinInCents);
      List<String> slots = new ArrayList<String>();
      int totalCapacity=g.getTotalCapacity();
      int totalEmpty=g.getTotalEmpty();
      System.out.println("Total capacity="+ totalCapacity);
      System.out.println("Total Empty="+ totalEmpty);

     // test:  to exceed total capacity by 1
     for (int i = 0; i <totalCapacity+1; i++){
         Ticket t = g.enterParking("a");
         if (t != null){
            t.show();
            slots.add(t.getSlot());
            totalEmpty=g.getTotalEmpty();
            System.out.println("Total Empty="+ totalEmpty);
         } else
           System.out.println("no empty slots");
     }

     // test:  to  release all slots occupied in previous cycle
     Thread.sleep(60000); // uncomment to get non-zero payment
     for (String slot : slots) {
       long cents = g.exitParking(slot);
       System.out.println("Slot " + slot + " payment in cents="+cents);
     }
     // negative test: attempt to release non-existing slot
     Long result = g.exitParking("XXX");
     if (result == null)
       System.out.println("No payment for slot XXX ");

   }
}
class Ticket {
  private String slot;
  private Calendar cal;
  private String direction;

  Ticket(String slot, Calendar enterDate, String direction){
    this.slot=slot;
    this.cal=enterDate;
    this.direction=direction;
  }
  public String  getSlot() {return slot;}

  public void show(){
    System.out.println("------  Ticket --------");
    System.out.println("slot: "+slot);
    System.out.println("Direction: "+direction);

    int year = cal.get(Calendar.YEAR);
    int month = cal.get(Calendar.MONTH);      // 0 to 11
    int day = cal.get(Calendar.DAY_OF_MONTH);
    int hour = cal.get(Calendar.HOUR_OF_DAY);
    int minute = cal.get(Calendar.MINUTE);
    int second = cal.get(Calendar.SECOND);

    System.out.printf("Entered at %4d/%02d/%02d %02d:%02d:%02d\n",  // Pad with zero
          year, month+1, day, hour, minute, second);
    System.out.println("-------------------");
   }

}

class Graph {
   private final Map<String, Vertex> graph; // mapping of vertex names to Vertex objects, built from a set of Edges
   private final int feePerMinuteInCents;
   private int totalCapacity;
   public int getTotalCapacity(){return totalCapacity;}

   public  synchronized int getTotalEmpty() {
       System.out.println("graphcsize="+graph.size());
       int nEmptySlots=0;

       for (Map.Entry<String,Vertex> v : graph.entrySet() ){
          nEmptySlots += v.getValue().emptySlots.size();
       }

       return nEmptySlots;
   }

   public static class Edge {   //representse connection between 2 entries
      public final String v1, v2;
      public final int dist;
      public Edge(String v1, String v2, int dist) {
         this.v1 = v1;
         this.v2 = v2;
         this.dist = dist;
      }
   }

   private static class Neighbour {
     int distance;
     Vertex vertex;
     Neighbour(Vertex v, int distance ){
        this.vertex=v;
        this.distance=distance;
     }
   }

   /**  vertex represents entrance; contains sorted by distance list of neighbours */
   public static class Vertex  {
      public final String name;  // entrance name
      public final int capacity; //# of slots close to this entrance; slots will be named as name-0, name-1

      private ConcurrentHashMap<String, Calendar> busySlots = new ConcurrentHashMap<String, Calendar>();   // occupied lots
      private ConcurrentLinkedQueue<String> emptySlots = new ConcurrentLinkedQueue<String>();

      public synchronized int getNumberOfEmptySlots() {return emptySlots.size();}

      private synchronized String getEmptySlot(Calendar now){
          if (emptySlots.isEmpty()){
             return null;
           } else {
             String slot = emptySlots.remove();
             busySlots.put(slot,now);
             return slot;
          }
      }

      private synchronized void  releaseEmptySlot(String slot){
         busySlots.remove(slot);
         emptySlots.add(slot);
      }

      Ticket  findParking(){
        Calendar now = Calendar.getInstance();
        String slot=getEmptySlot(now);
        if (slot == null){
          return null;
        } else{
         String direction = "Follow the sign towards to "+ name;
         Ticket t = new Ticket(slot, now, direction);
         return t;
       }
    }

      public SortedSet<Neighbour> sorted_neighbours =  new TreeSet<Neighbour>(new Comparator<Neighbour>(){
        public int compare(Neighbour n1, Neighbour n2){
          if (n1.distance > n2.distance)
             return 1;
          else if (n1.distance < n2.distance)
            return -1;
          else
            return 0;
         }
       }
      );

      public Vertex(String name, int capacity) {
         this.name = name;
         this.capacity = capacity;

         //slot name is composed from 2 parts: entry name and number: "a-0", "b-12",
         for (int i=0; i<capacity; i++){
           emptySlots.add(name+"-"+i);
         }
      }
   }

   /** Builds a graph from a set of edges */
   public Graph(Map<String,Integer> parkEntry, Edge[] edges, int feePerMinuteInCents) {
      this.graph = new HashMap<String,Vertex>(edges.length);
      this.feePerMinuteInCents = feePerMinuteInCents;
      //one pass to find all vertices
      for (Edge e : edges) {
         if (!parkEntry.containsKey(e.v1)) {
           System.err.printf("Parking doesn't contain an entry named \"%s\"\n", e.v1);
           System.exit(0);
         }
         if (!parkEntry.containsKey(e.v2)) {
           System.err.printf("Parking doesn't contain an entry named \"%s\"\n", e.v2);
           System.exit(0);
         }
         if (!graph.containsKey(e.v1)){
             int capacity=parkEntry.get(e.v1);
             graph.put(e.v1, new Vertex(e.v1, capacity));
         }
         if (!graph.containsKey(e.v2)) {
            int capacity=parkEntry.get(e.v2);
            graph.put(e.v2, new Vertex(e.v2, capacity));
         }
      }

      for (Edge e : edges) {
         graph.get(e.v1).sorted_neighbours.add(new Neighbour(graph.get(e.v2), e.dist));
         graph.get(e.v2).sorted_neighbours.add(new Neighbour(graph.get(e.v1), e.dist));
      }

      this.totalCapacity=0;
      for (int c : parkEntry.values()) {
         totalCapacity +=c;
      }
   }  //end of constructor

/** Returns amount of money to pay in cents
 *     input parameter: occupied slot
 *     if invalid slot is provided as an input then return null
*/
    Long exitParking(String slot)  {
            //parking slot name has 2 parts, entrance and number separated by - E.g.  "a-0", "a-1";
             int pos = slot.indexOf("-");
             if (pos < 1) return null;    //Invalid slot name
             String vertexName=slot.substring(0,pos);
             Vertex v = graph.get(vertexName);
             if (v == null) {
                return null;
             }
            //check what this slot exists
             Calendar cal= v.busySlots.get(slot);
             if (cal == null) {
                        return null;
              }
              long sec = (Calendar.getInstance().getTimeInMillis() - cal.getTimeInMillis()) /  1000;
              long cents = (sec*feePerMinuteInCents)/60;
              v.releaseEmptySlot(slot);
              return cents;
     }

   public Ticket enterParking(String startName) {   //bread-first search
      if (!graph.containsKey(startName)) {
         System.err.printf("Parking doesn't contain an entry named \"%s\"\n", startName);
         System.exit(0);
      }

      Set<String> visited = new HashSet<String>();
      Queue<Vertex> queue = new LinkedList<Vertex>();
      Vertex v = graph.get(startName);
      queue.add(v);

      Ticket t = v.findParking();
      if (t != null) return t;

      visited.add(startName);
      while (!queue.isEmpty()){
          v = queue.remove();
          Vertex child=null;
          for (Neighbour a : v.sorted_neighbours) {
               child = a.vertex; // neighbour
               if (visited.contains(child.name)){
                   continue;
               }
               visited.add(child.name);
               t = child.findParking();
               if (t != null) return t;
               queue.add(child);
           }
      }
      return null;

   }


}
