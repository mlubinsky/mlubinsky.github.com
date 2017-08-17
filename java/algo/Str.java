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
				Integer val =  123; // ht.get(c) +1;  //error here
				ht.put(c, val);
			}else{
				ht.put(c, 1);
			}
		}
		for(int i=0;i<s2.length();i++){
			char c = s2.charAt(i);
			if(ht.containsKey(c)){
				int val = 1231313; // ht.get(c).intValue();  //error here
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

    public static String longestUniqSubString(String input){

        HashSet<Character> set = new HashSet<Character>();

        String longestOverAll = "";
        String longestTillNow = "";

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);

            if (set.contains(c)) {
                longestTillNow = "";
                set.clear();
            }
            longestTillNow += c;
            set.add(c);
            if (longestTillNow.length() > longestOverAll.length()) {
                longestOverAll = longestTillNow;
            }
        }

        return longestOverAll;
    }

public static String longestUniqueString(String S) {
    int start = 0, end = 0, length = 0;
    boolean bits[] = new boolean[256];
    int x = 0, y = 0;
    for (; x < S.length() && y < S.length() && length < S.length() - x; x++) {
        bits[S.charAt(x)] = true;
        for (y++; y < S.length() && !bits[S.charAt(y)]; y++) {
            bits[S.charAt(y)] = true;
        }
        if (length < y - x) {
            start = x;
            end = y;
            length = y - x;
        }
        while(y<S.length() && x<y && S.charAt(x) != S.charAt(y))
            bits[S.charAt(x++)]=false;
    }
    return S.substring(start, end);
}

public static int lengthOfLongestSubstring(String s) {
    if(s==null)
            return 0;
    boolean[] flag = new boolean[256];

    int result = 0;
    int start = 0;
    char[] arr = s.toCharArray();

    for (int i = 0; i < arr.length; i++) {
        char current = arr[i];
        if (flag[current]) {
            result = Math.max(result, i - start);
            // the loop update the new start point
            // and reset flag array
            // for example, abccab, when it comes to 2nd c,
            // it update start from 0 to 3, reset flag for a,b
            for (int k = start; k < i; k++) {
                if (arr[k] == current) {
                    start = k + 1;
                    break;
                }
                flag[arr[k]] = false;
            }
        } else {
            flag[current] = true;
        }
    }

    result = Math.max(arr.length - start, result);

    return result;
}

/*
use HashSet to store the characters in current window [i, j)    (j = i initially).
Then we slide the index j to the right. If it is not in the HashSet, we slide j further.
Doing so until s[j] is already in the HashSet.
At this point, we found the maximum size of substrings without duplicate characters start with index i.
If we do this for all i, we get our answer.
*/
    public int lengthOfLongestSubstring2(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));         ////increment the right border of sliding window
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));  //increment the left border of sliding window
            }
        }
        return ans;
    }


/*
The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps.
Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index.
Then we can skip the characters immediately when we found a repeated character.
The reason is that if s[j] have a duplicate in the range [i, j) with index j'
​​we don't need to increase i little by little. We can skip all the elements in the range [i, j'] and let i to be j' + 1 directly.
*/

    public int lengthOfLongestSubstring3(String s) {
        int n = s.length();
        int ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }


    public int lengthOfLongestSubstring4(String s) {
        int n = s.length();
        int ans = 0;
        int[] index = new int[128]; // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
    }


    public static void main(String... args) {
    	System.out.println(firstNonRepeatedChar1("abcdabd"));
    	System.out.println(firstNonRepeatedChar2("abcdabd"));
    	System.out.println(firstNonRepeatedChar3("abcdabd"));
        String s ="12abcd34";
        System.out.println(s+ " longestUniqSubString="+longestUniqSubString(s));
        System.out.println(s+ " longestUniqueString="+longestUniqueString(s));
        System.out.println(s+ " lengthOfLongestSubstring="+lengthOfLongestSubstring(s));

    }

}