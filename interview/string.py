# https://medium.com/hackernoon/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

# Find the smallest window in a string containing all characters of another string
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

# Python3 program to find the smallest window
# containing all characters of a pattern.
no_of_chars = 256
 
# Function to find smallest window
# containing all characters of 'pat'
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
 





# difference between remove, del and pop?
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



# Check if a string only contains numbers.
'123a'.isnumeric()
#=> False
'123'.isnumeric()
#=> True

#Check if a string only contains letters.

'123a'.isalpha()
#=> False
'a'.isalpha()
#=> True

'123abc...'.isalnum()
#=> False
'123abc'.isalnum()
#=> True

# Return a list of keys from a dictionary.

d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
list(d)
#=> ['id', 'name', 'color', 'speed']


# How to combine two lists into a list of tuples?
a = ['a','b','c']
b = [1,2,3]
[(k,v) for k,v in zip(a,b)]
#=> [('a', 1), ('b', 2), ('c', 3)]

# How can you sort a dictionary by key, alphabetically?
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

# Given a non-empty string s, you may delete at most one character. 
# Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

s = 'radkar'
def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True

    return s == s[::-1]
  
solution(s)

# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def solution(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 
  
print(solution(A)) 
print(solution(B)) 
print(solution(C))


#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

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

# Given an array containing None values fill in the None values with most recent 
# non None value in the array 
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

# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    
    return sorted(list(set1^set2)), sorted(list(set1&set2)) # ^ A.symmetric_difference(B), & A.intersection(B)

print(solution(sentence1, sentence2))


# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

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
