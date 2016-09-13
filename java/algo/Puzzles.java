import java.util.*;

public class Puzzles {

 public boolean isPalindrome(String s) {
  // remove all non alfanumer chars
  s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
  int len = s.length();
  if (len < 2)
    return true;
  Stack<Character> stack = new Stack<Character>();
  int index = 0;
  // put 1st half on string to stack and compare with 2nd part of string using pop
  while (index < len / 2) {
    stack.push(s.charAt(index));
    index++;
  }
  if (len % 2 == 1)
    index++;

  while (index < len) {
    if (stack.empty())
       return false;

    char temp = stack.pop();
    if (s.charAt(index) != temp)
       return false;
    else
       index++;
  }
  return true;
 }


 public static boolean isValidPalindrome2(String s){
    if(s==null||s.length()==0) return false;
    s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
    System.out.println(s);
    for(int i = 0; i < s.length() ; i++){
       if(s.charAt(i) != s.charAt(s.length() - 1 - i)){
         return false;
       }
    }
    return true;
  }

public static boolean match_brackets(String s){
  HashMap<Character, Character> map = new HashMap<Character, Character>();
  map.put('(', ')');
  map.put('[', ']');
  map.put('{', '}');


  Stack<Character> stack = new Stack<Character>();
  for (int i = 0; i < s.length(); i++) {
    char curr = s.charAt(i);
    if (map.keySet().contains(curr)) {
       stack.push(curr);
    } else if (map.values().contains(curr)) {
       if (!stack.empty() && map.get(stack.peek()) == curr) {
         stack.pop();
       } else {
         return false;
       }
    }
  }
  return stack.empty();
}

public static int[] find_2_el_to_sum( int[] numbers, int sum) {
   	HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    int[] result = new int[2];
    for (int i = 0; i < numbers.length; i++) {
       if (map.containsKey(numbers[i])) {
             int index = map.get(numbers[i]);
             result[0] = index ;
             result[1] = i;
              break;
        } else {
             map.put(sum - numbers[i], i);
        }
    }
    return result;
 }


public static int  find_duplicates( int[] numbers) {
   	HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    //put in map as key a value, and as avalue an index
    for (int i = 0; i < numbers.length; i++) {
       if (map.containsKey(numbers[i])) {
            return map.get(numbers[i]);   //returm index
        } else {
             map.put(numbers[i], i);
        }
    }
    return -1;
 }

// Count the number of unique elements in sorted array
public static int countUnique(int[] A) {
  int count_duplicates = 0;
  for (int i = 0; i < A.length - 1; i++) {
    if (A[i] == A[i + 1]) {
       count_duplicates++;
    }
  }
  return (A.length - count_duplicates);
}

 public String reverseWords(String s) {
    if (s == null || s.length() == 0) {
       return "";
    }
    // split to words by space
    String[] arr = s.split(" ");
    StringBuilder sb = new StringBuilder();
    for (int i = arr.length - 1; i >= 0; --i) {
       if (!arr[i].equals("")) {
         sb.append(arr[i]).append(" ");
       }
    }
    return sb.length() == 0 ? "" : sb.substring(0, sb.length() - 1);
  }

  public int majorityElement(int[] num) { //assumption: there is element which occures > n/2 times , where n is number of elements
     if (num.length == 1) {
         return num[0];
      }
      Arrays.sort(num);
      return num[num.length / 2];
  }


  public int[] range_in_sortad_array(int[] nums, int target){
    return null;
  //	if(nums == null || nums.length == 0) { return null; }
   //ArrayList<Integer> result = new ArrayList<Integer>();
   //todo
  }

   // Kth Largest Element in an Array  /n*Log(n)
   public static int findKthLargest(int[] nums, int k) {   //n*Log(n)
     Arrays.sort(nums);
     return nums[nums.length-k];
   }


  // Kth Largest Element in an Array  /linear time
   public static int findKthLargest2(int[] nums, int k) {
      if (k < 1 || nums == null) {
           return 0;
       }
       return getKth(nums.length - k +1, nums, 0, nums.length - 1);
   }

public static int getKth(int k, int[] nums, int start, int end) {
  int pivot = nums[end];
  int left = start;
  int right = end;
  while (true) {
    while (nums[left] < pivot && left < right) {
       left++;
    }
    while (nums[right] >= pivot && right > left) {
       right--;
    }
    if (left == right) {
       break;
    }
    swap(nums, left, right);
  } // end of while
  swap(nums, left, end);
  if (k == left + 1) {
    return pivot;
  } else if (k < left + 1) {
    return getKth(k, nums, start, left - 1);
  } else {
    return getKth(k, nums, left + 1, end);
  }
}
public static void swap(int[] nums, int n1, int n2) {
  int tmp = nums[n1];
  nums[n1] = nums[n2];
  nums[n2] = tmp;
}



private static int getMissingNumber(int[] numbers, int totalCount) {
        int expectedSum = totalCount * ((totalCount + 1) / 2);
        int actualSum = 0;
        for (int i : numbers) {
            actualSum += i;
        }
 
        return expectedSum - actualSum;
}
//-----------------------------------------------
 public static void main(String... args) {   //(String[] args) {
   	  int sum=30;
   	  int[] seq = {10,15,20,5,20};
      System.out.println(Arrays.toString(seq));
      //System.out.println("Unique size="+ countUnique(seq));  -- works only for sorted array
      System.out.println("Array size="+seq.length);


      int index = find_duplicates(seq);
      if (index > -1)
         System.out.println("duplicates in array at index="+index + " value="+seq[index] );
      else
        System.out.println("No duplicates in array");

      int[] res=find_2_el_to_sum(seq, sum);
      System.out.println("Find 2 elements to sum  "+ sum + " = " +seq[res[0]] + " +   " + seq[res[1]]);
      System.out.println("Find Kth largest = " +findKthLargest2(seq,2));

      String str="abc";
      boolean result  = match_brackets(str);
      System.out.println("Match brackets for "+ str + " result="+result);
      str="ab([{c}])";
      result  = match_brackets(str);
      System.out.println("Match brackets for "+ str + " result="+result);
      str="a[}bc";
      result  = match_brackets(str);
      System.out.println("Match brackets for "+ str + " result="+result);

 }

}
