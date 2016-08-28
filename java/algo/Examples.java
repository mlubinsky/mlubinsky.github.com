import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;
import java.util.Queue;
import java.util.Stack;
import java.io.IOException;
import java.util.Collections;

import java.util.IntSummaryStatistics;
import java.util.stream.Collectors;

public  class Examples {

	public static void main(String[] args) 
	{
		
		Integer[] inumbers = new Integer[] { 8, 27, 64, 125, 256 };
		System.out.println("BEFORE SORT");
		for ( Integer i : inumbers){
		   System.out.println(i);	
		}

        Arrays.sort(inumbers, Collections.reverseOrder());
        System.out.println("AFTER SORT");
        for ( Integer i : inumbers){
		   System.out.println(i);	
		}	

        // Count the empty strings
        List<String> strList = Arrays.asList("abc", "", "bcd", "", "defg", "jk");
        long count = strList.stream().filter(x -> x.isEmpty()).count();
        System.out.printf("List %s has %d empty strings %n", strList, count);

        // Count String with length more than 3
        long num = strList.stream().filter(x -> x.length()> 3).count();
        System.out.printf("List %s has %d strings of length more than 3 %n", strList, num);
     
     
        // Count number of String which startswith "a"
        count = strList.stream().filter(x -> x.startsWith("a")).count();
        System.out.printf("List %s has %d strings which startsWith 'a' %n", strList, count);
     
        // Remove all empty Strings from List
        List<String> filtered = strList.stream().filter(x -> !x.isEmpty()).collect(Collectors.toList());
        System.out.printf("Original List : %s, List without Empty Strings : %s %n", strList, filtered);
     
        // Create a List with String more than 2 characters
        filtered = strList.stream().filter(x -> x.length()> 2).collect(Collectors.toList());
        System.out.printf("Original List : %s, filtered list (>2 chars) : %s %n", strList, filtered);
     
     
        // Convert String to Uppercase and join them using coma
        List<String> G7 = Arrays.asList("USA", "Japan", "France", "Germany", "Italy", "U.K.","Canada");
        String G7Countries = G7.stream().map(x -> x.toUpperCase()).collect(Collectors.joining(", "));
        System.out.println(G7Countries);
     
        // Create List of square of all distinct numbers
        List<Integer> numbers = Arrays.asList(9, 10, 3, 4, 7, 3, 4);
        List<Integer> distinct = numbers.stream().map( i -> i*i).distinct().collect(Collectors.toList());
        System.out.printf("Original List : %s,  Square Without duplicates : %s %n", numbers, distinct);
     
        //Get count, min, max, sum, and average for numbers
        List<Integer> primes = Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29);
        IntSummaryStatistics stats = primes.stream().mapToInt((x) -> x).summaryStatistics();
        System.out.println("Highest prime number in List : " + stats.getMax());
        System.out.println("Lowest prime number in List : " + stats.getMin());
        System.out.println("Sum of all prime numbers : " + stats.getSum());
        System.out.println("Average of all prime numbers : " + stats.getAverage());

		List<Integer> listOfNumbers = Arrays.asList(1, 2, 3, 4, 5, 6, 12, 18);
        Integer lcm = listOfNumbers.stream()
                           .filter(i -> i % 2 == 0)
                           .filter(i -> i % 3 == 0)
                           .findFirst().get(); 
        System.out.println("STREAM divided by 2 and 3 : "+lcm);

        List<String> versions = new ArrayList<>();
        versions.add("Lollipop");
        versions.add("KitKat");
        versions.add("Jelly Bean");
        versions.add("Ice Cream Sandwidth");
        versions.add("Honeycomb");
        versions.add("Gingerbread");

        // Using one filter() 
        // print all versions whose length is greater than 10 character
        System.out.println("All versions whose length greater than 10");
        versions.stream()
                .filter(s -> s.length() > 10)
                .forEach(System.out::println);

        System.out.println("first element which has letter 'e' ");
        String first = versions.stream()
                .filter(s -> s.contains("e"))
                .findFirst().get();
        System.out.println(first);
        

        // Using multiple filter
        System.out.println("Element whose length is > 5 and startswith G");
        versions.stream()
                .filter(s -> s.length() > 8)
                .filter(s -> s.startsWith("G"))
                .forEach(System.out::println);
        

	} // end of main()	
}