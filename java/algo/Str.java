import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class Str {
    
    /*
     * Using LinkedHashMap to find first non repeated character of String
     * Algorithm :
     *            Step 1: get character array and loop through it to build a 
     *                    hash table with char and their count.
     *            Step 2: loop through LinkedHashMap to find an entry with 
     *                    value 1, that's your first non-repeated character,
     *                    as LinkedHashMap maintains insertion order.
     */
    public static char firstNonRepeatedChar1(String str) {
        Map<Character,Integer> counts = new LinkedHashMap<>(str.length());
        
        for (char c : str.toCharArray()) {
            counts.put(c, counts.containsKey(c) ? counts.get(c) + 1 : 1);
        }
        
        for (Entry<Character,Integer> entry : counts.entrySet()) {
            if (entry.getValue() == 1) {
                return entry.getKey();
            }
        }
        throw new RuntimeException("didn't find any non repeated Character");
    }


    /*
     * Finds first non repeated character in a String in just one pass.
     * It uses two storage to cut down one iteration, standard space vs time
     * trade-off.Since we store repeated and non-repeated character separately,
     * at the end of iteration, first element from List is our first non
     * repeated character from String.
     */
    public static char firstNonRepeatedChar2(String word) {
        Set<Character> repeating = new HashSet<>();
        List<Character> nonRepeating = new ArrayList<>();
        for (int i = 0; i < word.length(); i++) {
            char letter = word.charAt(i);
            if (repeating.contains(letter)) {
                continue;
            }
            if (nonRepeating.contains(letter)) {
                nonRepeating.remove((Character) letter);
                repeating.add(letter);
            } else {
                nonRepeating.add(letter);
            }
        }
        return nonRepeating.get(0);
    }


    /*
     * Using HashMap to find first non-repeated character from String in Java.
     * Algorithm :
     * Step 1 : Scan String and store count of each character in HashMap
     * Step 2 : traverse String and get count for each character from Map.
     *          Since we are going through String from first to last character,
     *          when count for any character is 1, we break, it's the first
     *          non repeated character. Here order is achieved by going
     *          through String again.
     */
    public static char firstNonRepeatedChar3(String word) {
        HashMap<Character,Integer> scoreboard = new HashMap<>();
        // build table [char -> count]
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (scoreboard.containsKey(c)) {
                scoreboard.put(c, scoreboard.get(c) + 1);
            } else {
                scoreboard.put(c, 1);
            }
        }
        // since HashMap doesn't maintain order, going through string again
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (scoreboard.get(c) == 1) {
                return c;
            }
        }
        throw new RuntimeException("Undefined behaviour");
    }


    public static void StringFunc() {
       String s = "Gold:Stocks:Fixed Income:Commodity:Interest Rates";
       String[] splits = s.split(":");

       System.out.println("splits.size: " + splits.length);

       for(String asset: splits) {
           System.out.println(asset);
       }
    }

    public boolean isPermutation(String s1, String s2){
/*
Check if both Strings are hav­ing the same length, if not , return false.
Create a Hash Table, make char­ac­ter as key and its count as value
Navigate the string one tak­ing each char­ac­ter at a time
check if that char­ac­ter already exist­ing in hash table, if yes then increase its count by 1 and if it doesn’t exist insert into hash table with the count as 1.
Now nav­i­gate the sec­ond string tak­ing each char­ac­ter at a time
check if that char­ac­ter exist­ing in hash table, if yes then decrease its count by 1 and if it doesn’t exist then return false.
At the end nav­i­gate through hash table and check if all the keys has 0 count against it if yes then return true else return false.
*/

		if(s1.length()!=s2.length()){
			return false;
		}
		Hashtable ht = new Hashtable<Character, Integer>();
		for(int i=0;i<s1.length();i++){
			char c = s1.charAt(i);
			if(ht.containsKey(c)){	
				Integer val = ht.get(c) +1;
				ht.put(c, val);
			}else{
				ht.put(c, 1);
			}
		}
		for(int i=0;i<s2.length();i++){
			char c = s2.charAt(i);
			if(ht.containsKey(c)){
				int val = ht.get(c).intValue();
				if(val==0){
					return false;
				}
				val--;
				ht.put(c, val);
			}else{
				return false;
			}
		}
		Set<Character> keys = ht.keySet();
		for(Character k : keys ){
			if(ht.get(k) != null){
				return false;
			}
		}
		return true;
	}



    public static void main(String... args) {
    	System.out.println(firstNonRepeatedChar1("abcdabd"));
    	System.out.println(firstNonRepeatedChar2("abcdabd"));
    	System.out.println(firstNonRepeatedChar3("abcdabd"));
    	
    }

}