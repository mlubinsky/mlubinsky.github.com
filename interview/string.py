# https://medium.com/hackernoon/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed


def decode(inp):
  out=''
  for i, item in enumerate(inp):
    if  item.isdigit():
       out += int(item) * inp[i-1]
  return out
#------------------------------
def encode(message):
  encoded_string = ""
  i = 0
  while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
        #if the character at the current index is the same as the character at the next index. If the characters are the same, the count is incremented to 1'''
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        #the count and the character is concatenated to the encoded string'''
        encoded_string += ch + str(count)
        i = j + 1

  return encoded_string
#-------------------------

s='a2z4'
print(s)
print(decode(s))

#-------------------------
#  Max wather container
#-------------------------
def maxArea( A):
    l = 0
    r = len(A) -1
    area = 0
     
    while l < r:
        # Calculating the max area
        area = max(area, min(A[l], A[r]) * (r - l))
     
        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return area


# ------------------------------------- 
#  Find subarray  with sum as given value
# ------------------------------------- 
# Returns true if the there is a subarray
# of arr[] with sum  equal to 'sum'
# otherwise returns false. Also, prints  the result.

def subArraySum(arr,   sum_):
    n = len(arr) 
    # Initialize curr_sum as value of first element  and starting point as 0
    curr_sum = arr[0]
    start = 0
 
    # Add elements one by  one to curr_sum and
    # if the curr_sum exceeds sum, then remove starting element
    i = 1
    while i <= n:
         
        # If curr_sum exceeds the sum, then remove the starting elements
        while curr_sum > sum_ and start < i-1:
         
            curr_sum = curr_sum - arr[start]
            start += 1
             
        # If curr_sum becomes equal to sum, then return true
        if curr_sum == sum_:
            print ("Sum found between indexes")
            print ("% d and % d"%(start, i-1))
            return 1
 
        # Add this element to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
 
    # If we reach here, then no subarray
    print ("No subarray found")
    return 0
 
# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]

sum_ = 23
 
subArraySum(arr,   sum_)


https://www.techiedelight.com/4-sum-problem/ 
#----------------------------------------------------------
# Check if quadruplet exists in a list with the given sum
#----------------------------------------------------------
def hasQuadruplet(nums, target):
 
    # create an empty dictionary
    # key —> target of a pair in the list
    # value —> list storing an index of every pair having that sum
    d = {}
 
    # consider each element except the last element
    for i in range(len(nums) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):
 
            # calculate the remaining sum
            val = target - (nums[i] + nums[j])
 
            # if the remaining sum is found on the dictionary,
            # we have found a quadruplet
            if val in d:
 
                # check every pair having a sum equal to the remaining sum
                for pair in d[val]:
                    x, y = pair
 
                    # if quadruplet doesn't overlap, print it and return true
                    if (x != i and x != j) and (y != i and y != j):
                        print('Quadruplet Found', (nums[i], nums[j], nums[x], nums[y]))
                        return True
 
            # insert the current pair into the dictionary
            d.setdefault(nums[i] + nums[j], []).append((i, j))
 
    # return false if quadruplet doesn't exist
    return False
 
 
if __name__ == '__main__':
 
    nums = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 20
 
    if not hasQuadruplet(nums, target):
        print('Quadruplet doesn\'t exist')


# ----------------------------------------------
# Longest substr with at most 2 distinct chars
# ----------------------------------------------
int lengthOfLongestSubstringTwoDistinct(string s) {
        vector<int> map(128, 0);
        int counter=0, begin=0, end=0, d=0; 
        while(end<s.size()){
            if(map[s[end++]]++==0) counter++;
            while(counter>2) 
                 if(map[s[begin++]]--==1) counter--;
            d=max(d, end-begin);
        }
        return d;
    }
#-------------------------------------------------
# Longest Substring Without Repeating Characters (C++)
#-------------------------------------------------
int lengthOfLongestSubstring(string s) {
        vector<int> map(128,0);
        int counter=0, begin=0, end=0, d=0; 
        while(end<s.size()){
            if(map[s[end++]]++>0) counter++; 
            while(counter>0) 
                 if(map[s[begin++]]-->1) counter--;
            d=max(d, end-begin); //while valid, update d
        }
        return d;
    }

# ---------------------------------------------------------------------------
# longest consequitive sequence which can be constructed in array by reshuffling elements
# ---------------------------------------------------------------------------
# for each  element n from input we check if (n-1) and (n+1) in the set
# if they are we increase len and erase these numbers
s= set()
maxlen=0
for n in numbers:
   tmp=n
   len=0
  
   while n in s:
      s.remove(n)
      n+=1
      len+=1
      
    n = temp-1
    while n in s:
      s.remove(n)
      n -=1
      len++
      
    maxlen = max(maxlen, len)
 
return maxlen

#--------------------------
# The Sieve Of Eratosthenes
#--------------------------
def sieve_of_eratosthenes(upper_bound):
    primes = [True] * upper_bound
    primes[0] = False
    primes[1] = False
    for i in range(2, isqrt(upper_bound)+1):
        if primes[i]:
            for x in range(i*i, upper_bound, i):
                primes[x]=False
    return primes.count(True)

print(sieve_of_eratosthenes(10000000))

# Not only lists but also strings can be reversed with slicing.

numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])
#[5, 4, 3, 2, 1]

s = "Hello"
print(s[::-1])
# olleH

#--------------------------------------------------
# Find the second largest element in a list or the second smallest element in a list.
#-------------------------------------------------
# list of numbers - length of list should be at least 2
list1 = [10, 20, 4, 45, 99]
 
mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and \
        mx != list1[i]:
        secondmax=list1[i]
 
print("Second highest number is : ",\
      str(secondmax))


[100,4,200,1,2,3] - answer
#-----------------

def second_largest(numbers):
    minimum = float('-inf')
    first, second = minimum, minimum
    for n in numbers:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second if second != minimum else None
  
# or   
numbers = set(numbers)
numbers.remove(max(numbers))
max(numbers)

# or 
sorted(set(numbers))[-2]

###. using sorting
my_list = [13, 51, 1, -14, 0, 91, 43]
my_list.sort()
print(my_list[-2])  # 51

# or
largest_element = max(my_list)
my_list.remove(largest_element)
print(max(my_list))  # 51



list_1 = [1, 2, 3]
list_2 = ['one', 'two', 'tree']
list(zip(list_1, list_2))

# [(1,one),(2,two),(3,tree)]

#------------------------------------------
# Max substring without repeating chars
#------------------------------------------
"""
  Linear Time:   using the window sliding technique.
 Whenever we see repetition, we remove the window till the repeated string.
"""

def longestUniqueSubsttr(string):
 
    # last index of every character
    last_idx = {}
    max_len = 0
 
    # starting index of current
    # window to calculate max_len
    start_idx = 0
 
    for i in range(0, len(string)):
       
        # Find the last index of str[i]
        # Update start_idx (starting index of current window)
        # as maximum of current value of start_idx and last
        # index plus 1
        if string[i] in last_idx:
            start_idx = max(start_idx, last_idx[string[i]] + 1)
 
        # Update result if we get a larger window
        max_len = max(max_len, i-start_idx + 1)
 
        # Update last index of current char.
        last_idx[string[i]] = i
 
    return max_len
 
 
# Driver program to test the above function
string = "geeksforgeeks"
print("The input string is " + string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character" +
      " substring is " + str(length))

https://www.callicoder.com/minimum-window-substring/

#---------------------------------------------------------------------------------  
# Find the smallest window in a string containing all characters of another string
#---------------------------------------------------------------------------------  
https://stackoverflow.com/questions/2459653/how-to-find-smallest-substring-which-contains-all-characters-from-a-given-string

https://www.interviewkickstart.com/problems/minimum-window-substring 

""" 
 we create an array named frequency to keep a count of occurrences of each character in string t (O(length of t)). 
 Now we start traversing the string S and keep a variable “cnt” which increases whenever we encounter a character present in string t.
 When the value of count reaches the length of t, this substring contains all the characters present in string t. 
 We try removing extra characters as well as unwanted characters from the beginning of the obtained string. 
 The resultant string is checked whether it can become the minimum window, and the answer is updated accordingly.

This algorithm uses the 2 pointer method, which is widely used in solving various problems. 
You can refer https://www.geeksforgeeks.org/two-pointers-technique/ article 
 
 
 Time Complexity:
O(n) where n is the length of string s.

Since each character of string s is traversed at most 2 times, the time complexity of the algorithm is O(n) + O(m).

Auxiliary Space Used:
O(1).

We are creating 2 frequency arrays of size 128, which use extra space O(128) + O(128). Hence it is O(1).

Space Complexity:
O(n+m) where n is the length of string s and m is the length of string t.

For storing input it will take O(n+m), as we are storing two strings of length n and length m and the auxiliary space used is O(1) hence total complexity will be O(n+m).

Note: We could use an array of length 62 (with some mapping) instead of 128, but this is a general solution which works for the input string containing any ASCII characters.
"""
    public static String minimum_window(String s, String t){

        String result = "";

        if(t.length()>s.length()) {
            return "-1";
        }
        int n = s.length(), m = t.length();   
        int freq1[] = new int[128]; /*creating a frequency array to store the 
                                    frequencies of the characters in string t*/
        int freq2[] = new int[128]; /*creating a frequency array to store the 
                                    frequencies of the characters in string s*/
        for (char c : t.toCharArray()) {
            freq1[c]++;
        }
        int l = 0, len = n+1; 
        int cnt = 0;
        /*This part uses "2 pointer method." You can find a link 
        for the same in the editorial of this problem.*/
        for (int i = 0; i < n ; i++){
            char temp = s.charAt(i);
            freq2[temp]++;
            //if a character is present in string t we increment the count of cnt variable.
            if (freq1[temp]!=0 && freq2[temp]<=freq1[temp]) {
                cnt++; 
            }
            /*if we match all the characters present in string t, 
            we try to find the minimum window possible*/
            if (cnt==m) {
                /*if any character is occuring more than the required times, we try to remove it
                from the starting and also try to remove the unwanted characters that are 
                not a part of string t from the starting. We check the remainder string if it 
                can become the smallest window.*/
                while (freq2[s.charAt(l)]>freq1[s.charAt(l)] || freq1[s.charAt(l)]==0) { 
                    if (freq2[s.charAt(l)]>freq1[s.charAt(l)]) { 
                        freq2[s.charAt(l)]--; 
                    }
                    l++; 
                }
                //check if this can become the smallest window and update the result accordingly.
                if (len > i-l+1) { 
                    len = i-l+1;
                    result = s.substring(l,l+len);
                } 
            } 
        } 
        return result.length()==0?"-1":result;
    }
"""
1. First check if the length of the string is less than the length of the given pattern, 
if yes then “no such window can exist “.

2. Store the occurrence of characters of the given pattern in a hash_pat[].

3. we will be using two pointer technique basically

4. Start matching the characters of pattern with the characters of string i.e. increment count if a character matches.

5. Check if (count == length of pattern ) this means a window is found.
6. If such a window found, try to minimize it by removing extra characters from the beginning of the current window.
7. delete one character from first and again find this deleted key at right, once found apply step 5 .
8. Update min_length.
9. Print the minimum length window.
"""

#-----------------------------------------------------------------
# Find the smallest window containing all characters of a pattern
#------------------------------------------------------------------
no_of_chars = 256

def findSubString(string, pat):
    len1 = len(string)
    len2 = len(pat)
 
    # Check if string's length is
    # less than pattern's
    # length. If yes then no such
    # window can exist
    if len1 < len2:
 
        print("No such window exists")
        return ""
 
    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars
 
    # Store occurrence ofs characters of pattern
    for i in range(0, len2):
        hash_pat[ord(pat[i])] += 1
 
    start, start_index, min_len = 0, -1, float('inf')
 
    # Start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):
 
        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1
 
        # If string's char matches with
        # pattern's char then increment count
        if (hash_str[ord(string[j])] <=
                hash_pat[ord(string[j])]):
            count += 1
 
        # if all the characters are matched
        if count == len2:
 
            # Try to minimize the window
            while (hash_str[ord(string[start])] >
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):
 
                if (hash_str[ord(string[start])] >
                        hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1
 
            # update window size
            len_window = j - start + 1
            if min_len > len_window:
 
                min_len = len_window
                start_index = start
 
    # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""
 
    # Return substring starting from
    # start_index and length min_len
    return string[start_index: start_index + min_len]
 
 
# Driver code
if __name__ == "__main__":
 
    string = "this is a test string"
    pat = "tist"
 
    print("Smallest window is : ")
    print(findSubString(string, pat))
 
#-----------------------------------------
# difference between remove, del and pop?
#-----------------------------------------
#remove() remove the first matching value.
li = ['a','b','c','d']
li.remove('b')
li
#=> ['a', 'c', 'd']

# del removes an element by index.
li = ['a','b','c','d']
del li[0]
li
#=> ['b', 'c', 'd']

# pop() removes an element by index and returns that element.
li = ['a','b','c','d']
li.pop(2)
#=> 'c'
li
#=> ['a', 'b', 'd']


#------------------------------------------
# Check if a string only contains numbers
#------------------------------------------
'123a'.isnumeric()
#=> False
'123'.isnumeric()
#=> True

#------------------------------------------
# Check if a string only contains letters.
#------------------------------------------
'123a'.isalpha()
#=> False
'a'.isalpha()
#=> True

'123abc...'.isalnum()
#=> False
'123abc'.isalnum()
#=> True

#------------------------------------------
# Return a list of keys from a dictionary.
#------------------------------------------
d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
list(d)
#=> ['id', 'name', 'color', 'speed']


# How to combine two lists into a list of tuples?
a = ['a','b','c']
b = [1,2,3]
[(k,v) for k,v in zip(a,b)]
#=> [('a', 1), ('b', 2), ('c', 3)]

#------------------------------------------
# Sort a dictionary by key, alphabetically?
#------------------------------------------
# You can’t “sort” a dictionary because dictionaries don’t have order
# but you can return a sorted list of tuples which has the keys and values that are in the dictionary.
d = {'c':3, 'd':4, 'b':2, 'a':1}
sorted(d.items())
#=> [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

###  How do any() and all() work?
### Any takes a sequence and returns true if any element in the sequence is true.
### All returns true only if all elements in the sequence are true.
a = [False, False, False]
b = [True, False, False]
c = [True, True, True]
print( any(a) )
print( any(b) )
print( any(c) )
#=> False
#=> True
#=> True
print( all(a) )
print( all(b) )
print( all(c) )
#=> False
#=> False
#=> True

#------------------------------------------
# Given a non-empty string s, you may delete at most one character. 
# Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.
#------------------------------------------

s = 'radkar'
def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True

    return s == s[::-1]
  
solution(s)
#------------------------------------------
# Given an array of integers, determine whether the array is monotonic or not.
#------------------------------------------
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def solution(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 
  
print(solution(A)) 
print(solution(B)) 
print(solution(C))

#------------------------------------------
# Given an array nums, write a function to move all zeroes to the end of it 
# while maintaining the relative order of the non-zero elements.
#------------------------------------------
array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def solution(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

solution(array1)
solution(array2)

#------------------------------------------
# Given an array containing None values 
# fill in the None values with most recent  non None value in the array 
#------------------------------------------
array1 = [1,None,2,3,None,None,5,None]

def solution(array):
    valid = 0            
    res = []                 
    for i in nums: 
        if i is not None:    
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

solution(array1)
#------------------------------------------
# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common. 
#------------------------------------------
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    
    return sorted(list(set1^set2)), sorted(list(set1&set2)) # ^ A.symmetric_difference(B), & A.intersection(B)

print(solution(sentence1, sentence2))

#------------------------------------------
# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
#------------------------------------------
n = 35
def solution(n):
    prime_nums = []
    for num in range(n):
        if num > 1: # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0: # if the modulus == 0 is means that the number can be divided by a number preceding it
                    break
            else:
                prime_nums.append(num)
    return prime_nums
solution(n)
