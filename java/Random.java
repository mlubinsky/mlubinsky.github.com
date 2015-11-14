// http://www.programcreek.com/2013/11/arrays-sort-comparator/
import java.util.Objects;
import java.util.List;
import java.util.Arrays;
import java.util.Comparator;

//Object.clone() copy all instance variables; 
// but if there non primitive or non-immutable  members then clone share mutable state
//clonable interface - is required to make deep cloning
// if x.equals(y) then hashCodes should be equal

class Person  {
	String first;
	String second;
	public int hashCode (){
		return Objects.hash(first, second);
	}
}

class LenComparator implements Comparator<String> {
	public int compare (String a, String b){
		return a.length() - b.length();
	}
}
public class Random {
   static String[] names = {"Peter", "Paul", "Mary", "Michael"};

 
   public static void main(String args[])  {
       System.out.println("--  BEFORE SORT --");
       for (String s : names) { System.out.println(s);}
       Arrays.sort(names);
       System.out.println("--  AFTER LEXICAL SORT --");
       for (String s : names) { System.out.println(s);}

       	//Comparator<String> comp= new LenComparator();
       	Arrays.sort(names, new LenComparator());
        System.out.println("--  AFTER SORT BY LENGTH--");
        for (String s : names) { System.out.println(s);}

	    Arrays.sort(names, (a,b) -> a.length() - b.length());
        System.out.println("--  AFTER SORT BY LENGTH using Functional interface--");
        for (String s : names) { System.out.println(s);}	


         Arrays.sort(names, String::compareToIgnoreCase);

        // for each 
        System.out.println("--  foreach --");
        List<String> list = Arrays.asList(names);
        list.forEach(x->System.out.println(x));	

        list.removeIf(Objects::isNull);

    }

}