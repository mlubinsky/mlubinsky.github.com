import java.util.*;

public class Puzzles {


    // Returns the smallest number that cannot be represented as sum
    // of subset of elements from set represented by sorted array arr[0..n-1]
    int findSmallest(int arr[], int n) 
    {
        int res = 1; // Initialize result
 
        // Traverse the array and increment 'res' if arr[i] is
        // smaller than or equal to 'res'.
        for (int i = 0; i < n && arr[i] <= res; i++)
            res = res + arr[i];
 
        return res;
    }



 public boolean isPalindrome(String s) {
  // remove all non alfa-numeric chars
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

public static boolean find_duplicate_using_set(String[] input) {
        Set tempSet = new HashSet();
        for (String str : input) {
            if (!tempSet.add(str)) {
                return true;
            }
        }
        return false;
}

public static int  find_duplicates_using_map( int[] numbers) {
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

//trick is to go from end of array to begimnning
  public int find_first_duplicate_element(int [] arrA){
    int index = -1;
    HashSet<Integer> hs = new HashSet<>();
    for(int i = arrA.length-1;i<=0;i--){
      if(hs.contains(arrA[i])){
        index = i;
      }else{
        hs.add(arrA[i]);
      }
    }
    return arrA[index];
  }

//http://algorithms.tutorialhorizon.com/find-a-peak-element-in-a-given-array/
  public int peak(int [] arrA,int low, int high, int size){
    int mid = (low+high)/2;
    if(   (mid==0||arrA[mid]>=arrA[mid-1]) && 
          (arrA[mid]>=arrA[mid+1]||mid==size-1)
      ){
      return mid;
    }
    else if (mid >0 && arrA[mid] < arrA[mid-1]) 
         return peak(arrA,low,mid-1,size);
    else 
       return   peak(arrA,mid+1,high,size);
  }


// in sorted array find occurence of the number
  public int findOccurrences(int [] arrA, int x){
    int count = 0;
    int startPoint = findFirstOccurrence(arrA,x,0,arrA.length-1);
    if(startPoint<0){
      return -1;
    }
    int endPoint = findLastOccurrence(arrA, x, 0, arrA.length-1);
    count = endPoint-startPoint+1;
    return count;
  }
  public int findFirstOccurrence(int [] arrA, int x,int start, int end ){
    if(end>=start){
      int mid = (start+end)/2;
      if((mid==0||(arrA[mid-1]<x)) && arrA[mid]==x){
        return mid;
      }else if(arrA[mid]<x){
        return findFirstOccurrence(arrA, x, mid+1, end);
      }else{
        return findFirstOccurrence(arrA, x, start, mid-1);

      }
    }else return -1;
  }
  public int findLastOccurrence(int [] arrA, int x,int start, int end ){
    if(end>=start){
      int mid = (start+end)/2;
      if((mid==arrA.length-1||arrA[mid+1]>x) &&(arrA[mid]==x)){
        return mid;
      }else if(arrA[mid]>x){
        return findLastOccurrence(arrA, x, start, mid-1);
      }else{
        return findLastOccurrence(arrA, x, mid+1, end);
      }
    }else return -1;
  }

//dynamic programming  - find subarray with max sum
// MS(i) = Max[MS(i-1) + A[i] , A[i]]
//bottom up approach
    public int max_sum_subarray(int [] a){
        int [] solution = new int[a.length+1];
        solution[0] = 0;

        for (int j = 1; j <solution.length ; j++) {
            solution[j] = Math.max(solution[j-1]+a[j-1],a[j-1]);
        }
         
        //System.out.println(Arrays.toString(solution));

        // return the maximum in the solution array
        int result = solution[0];
        for (int j = 1; j <solution.length ; j++) {
            if(result<solution[j])
                result = solution[j];
        }

        return result;
    }

/*Maximum Product Cutting Problem.
Objective: Given a rope of length n meters, write an algorithm to cut the rope in such a way that 
product of different lengths of rope is maximum. At least one cut has to be made.
*/
public int maxProdutRecursionSlow(int n) {
  // base case
  if (n == 0 || n == 1) {
    return 0;
  }
  // make all possible cuts and get the maximum
  int max = 0;
  for (int i = 1; i < n; i++) {
    // Either this cut will produce the max product OR
    // we need to make further cuts
    max = Math.max(max,
        Math.max(i * (n - i), i * maxProdutRecursionSlow(n - i)));
  }
  //return the max of all
  return max;
}

// good solution
public void maxProductCutting(int n) {
    int[] MPC = new int[n + 1];
    MPC[1] = 1;
    for (int i = 2; i < n + 1; i++) {
      int mp = Integer.MIN_VALUE;
      for (int j = 1; j < i; j++) {
        mp = Math.max(mp, Math.max(j * MPC[i - j], j * (i - j)));
      }
      MPC[i] = mp;
    }
    System.out.println("Dynamic Programming: Maximum product cutting in "
        + n + "is " + MPC[n]);
  }

//Given a rod of length n inches and a table of prices pi, i=1,2,…,n, 
//write an algo­rithm to find the max­i­mum rev­enue rn obtain­able by cut­ting up the rod and sell­ing the pieces.  

//There can be n-1 cuts can be made in the rod of length n, so there are 2n-1 ways to cut the rod.
//slow
  public static int profit(int[] value, int length) {
      if (length <= 0)
         return 0;
      // either we will cut it or don't cut it
      int max = -1;
      for(int i=0;i<length;i++)
        max = Math.max(max, value[i] + profit(value, length-(i+1)));      
      
      return max;   
  }
  //fast
  public static int profitDP(int[] value, int length) {
    int[] solution = new int[length + 1];
    solution[0] = 0;

    for (int i = 1; i <= length; i++) {
      int max = -1;
      for (int j = 0; j < i; j++) {
        max = Math.max(max, value[j] + solution[i - (j + 1)]);
        solution[i] = max;
      }
    }
    return solution[length];
  }
//-----------------------------------------------
 public static void main(String... args) {   //(String[] args) {
   	  int sum=30;
   	  int[] seq = {10,15,20,5,20};
      System.out.println(Arrays.toString(seq));
      //System.out.println("Unique size="+ countUnique(seq));  -- works only for sorted array
      System.out.println("Array size="+seq.length);


      int index = find_duplicates_using_map(seq);
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
