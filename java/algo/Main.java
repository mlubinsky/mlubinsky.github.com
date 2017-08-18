import java.util.*;
//object references occupy 4 bytes on 32 bits JVM
//http://java-performance.info/memory-consumption-of-java-data-types-1/
//each LinkedList node contains references to the previous and next elements as well as a reference to the data value
// Such node occupies 24 bytes (12 bytes header + 3*4 bytes for references), which is 6 times more than ArrayList in terms of per-node overhead.
// This structure is also CPU cache-unfriendly due to its spatial non-locality.
//http://www.slideshare.net/cnbailey/memory-efficient-java

// int value is 32 bits  but Int() object is 128 bits

class Dog implements Comparator<Dog>, Comparable<Dog>{
   private String name;
   private int age;
   Dog(){  }

   Dog(String n, int a){
      name = n;
      age = a;
   }

   public String getDogName(){
      return name;
   }

   public int getDogAge(){
      return age;
   }

   // Overriding the compareTo method

   //comparable interface
   @Override
   public int compareTo(Dog d){
      return (this.name).compareTo(d.name);
   }

 //  What if we wish to sort an array of Person by age in one scenario,
 //  and we wish to sort again by name on another scenario?
 //  The solution is to use a Comparator.

//comparator interface
   // Overriding the compare method to sort the age  COMPARATOR
   public int compare(Dog d, Dog d1){
      return d.age - d1.age;
   }

   public static Comparator<Dog> AGE_COMPARATOR = new Comparator<Dog>() {
      @Override
      public int compare(final Dog o1, final Dog o2) {
         return Integer.valueOf(o1.age).compareTo(o2.age);
      }
   };
   public static Comparator<Dog> NAME_COMPARATOR = new Comparator<Dog>() {
      @Override
      public int compare(final Dog o1, final Dog o2) {
         return o1.name.compareTo(o2.name);
      }
   };

   public String toString() {
      return "[name: " + name + ", age: " + age + "]";
   }
}


public class Main {
  String[] words = new String[]{ "hello", "foo", "bar" };



  //Main constructor
  {
  }

   public static void  string_manipulation(){
   	  System.out.println("\n---string_manipulation---!");
   	  String sampleString = "Apple Banana Carrot";
      String[] animals = sampleString.split(" ");
      int animalIndex = 1;
      for (String animal : animals) {
         System.out.println(animalIndex + ". " + animal);
         animalIndex++;
      }
   }

   public static void reverse_list() {
   	  System.out.println("----reverse_list----");
      List<String> list = Arrays.asList("one", "two", "three");
      List reversed = new ArrayList(list.size());
      for (int i = list.size() - 1; i >= 0; i--) {
        reversed.add(list.get(i));
      }
     for (int i = 0; i < reversed.size() ; i++) {
        System.out.println(reversed.get(i));
      }

    }

//Arrays.binarysearch() works for arrays which can be of primitive data type also.
//Collections.binarysearch() works for objects Collections like ArrayList and LinkedList.
   public static void obj_array_sort() {
   	//http://javadevnotes.com/java-initialize-array-examples
   	  System.out.println("\n---obj_array_sort---!");
      Integer[] myArray = { 5, 2, 7, 3, 9 };
      Arrays.sort(myArray, new Comparator<Integer>(){
         @Override
         public int compare(Integer arg0, Integer arg1) {
            return -1 * arg0.compareTo(arg1);
         }});
      System.out.println(Arrays.toString(myArray));
   }

  public static void int_array_example() {
  	int[] numbers = new int[] { 1, 14, 9, 16 };
    System.out.println("\n---int_array_example---!");

    System.out.println(Arrays.toString(numbers));
    Arrays.sort(numbers);
    System.out.println(Arrays.toString(numbers));
    int item=5;
    int index = Arrays.binarySearch(numbers, item);
    System.out.println("binary search  for 5 returned index="+index);
 }


 public static void obj_array_example() {
      System.out.println("\n---obj_array_example---!");
      List<Dog> list = new ArrayList<Dog>();

      list.add(new Dog("Shaggy",3));
      list.add(new Dog("Lacy",2));
      list.add(new Dog("Roger",10));
      list.add(new Dog("Tommy",4));
      list.add(new Dog("Tammy",1));

      System.out.println("\n---convert list to array ---");

      Dog[] array = new Dog[list.size()];
      list.toArray(array);
      Arrays.sort(array);   //to make it work the Dog class must implement <Comparable> interface compareTo
      System.out.println("\n---Sorted array in place array using comparable interface:");
      System.out.println(Arrays.toString(array));
      System.out.println("\n---Sorted array in place array using comparator interface:");
      Arrays.sort(array, Dog.NAME_COMPARATOR);
      System.out.println(Arrays.toString(array));
      Arrays.sort(array, Dog.AGE_COMPARATOR);
      System.out.println(Arrays.toString(array));
      System.out.println("\nBy deault, Arrays.sort() sorts an array in ascending order.");

      System.out.println("\n---Example of list  using Collection.sort:--------");
      Collections.sort(list);// Sorts the array list
      for(Dog a: list)//printing the sorted list of names
         System.out.print(a.getDogName() + ", ");

      // Sorts the array list using comparator
      Collections.sort(list, new Dog());  //second arg is comparator interface
      System.out.println(" ");
      for(Dog a: list)//printing the sorted list of ages
         System.out.print(a.getDogName() +"  : "+
		 a.getDogAge() + ", ");
    }


 public static void list_set_example(){
 	  System.out.println("\n---list_set_example---!");
 	  Integer[] arr = { 5, 2, 17, 13, 12, 19, 7, 3, 9, 15 };
 	  List<Integer> list = Arrays.asList(arr);
      Set<Integer> set = new HashSet<Integer>(list);
      int item=3;
      System.out.println("Is list  contains "+item+" ? "+list.contains(item));
      System.out.println("Is set  contains "+item+" ? "+set.contains(item));


 }

  public static void treeset_example(){
      //Both TreeSet and TreeMap store elements in sorted order. However, it is the comparator that defines precisely what sorted order means.
  }

  public static void map_example(){
  	 //http://coding-geek.com/how-does-a-hashmap-work-in-java/
  	 System.out.println("\n---map_example---!");
     Map<String, String> map = new HashMap<String, String>();

  	 map.put("k1", "V1");
     map.put("k2", "V2");
     map.put("k3", "V3");

     for(Map.Entry<String, String> entry : map.entrySet()){
         System.out.printf("Key : %s and Value: %s %n", entry.getKey(), entry.getValue());
     }

     if (map.containsKey("k2")) {
             System.out.println("map contains key k2");
  	 }
  	 if (map.containsValue("V2")) {
             System.out.println("map contains value V2");
  	 }
    String value = map.get("hello");
    System.out.println("For key='hello' the value="+value);
    // do something with value

  }

   public static void main(String... args) {   //(String[] args) {
    //assert true == false : "There is a problem";
    System.out.println("Hello, world!");
    string_manipulation();
    int_array_example();
    obj_array_sort();
    obj_array_example();
    list_set_example();
    map_example();
    reverse_list();
  }

}