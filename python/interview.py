https://www.tutorialspoint.com/questions/category/Python
  
#### sorted() vs list.sort() in place

a=[3,4,2]
sorted(a)
[2, 3, 4]
a.sort()
a
[2, 3, 4]

#### 3 sum problem

https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
  
https://medium.com/swlh/crack-leetcode-15-3sum-b0dfd80c3550
  
https://www.tutorialspoint.com/3sum-in-python

There are there elements a, b, c in the array, such that a + b + c = 0. 
Find all triplets.

Sort the array nums, and define an array res
for i in range 0 to length of nums – 3
  if i > 0 and nums[i] = nums[i - 1], then skip the next part and continue
  l := i + 1 and r := length of nums – 1
          
  while l < r
    sum := sum of nums[i], nums[l] and nums[r]
    if sum < 0, then l := l + 1, otherwise when sum > 0, then r := r – 1
    otherwise insert nums[i], nums[l], nums[r] into the res array

    while l < length of nums – 1 and nums[l] = nums[l + 1]
       increase l by 1

    while r > 0 and nums[r] = nums[r - 1]
       decrease r by 1
     
    increase l by 1 and decrease r by 1

     
def threeSum( nums):
      nums.sort()
      result = []
      for i in range(len(nums)-2):
         if i> 0 and nums[i] == nums[i-1]:
            continue
         l = i+1
         r = len(nums)-1
         while(l<r):
            sum = nums[i] + nums[l] + nums[r]
            if sum<0:
               l+=1
            elif sum >0:
               r-=1
            else:
               result.append([nums[i],nums[l],nums[r]])
               while l<len(nums)-1 and nums[l] == nums[l + 1] : l += 1
               while r>0 and nums[r] == nums[r - 1]: r -= 1
               l+=1
               r-=1
      return result

    
####  find three elements whose sum is closest to give value.    

```
import sys
def threeSumClosest(A, B):
    i , n = 0 , len(A)
    A = sorted(A)
    diff = sys.maxint
    close_sum = 0
    while i <= n-3:
        j , k = i+1 , n-1
        sum = A[i] + A[j] + A[k]
        if sum == B:
            return sum
        if diff > abs(sum - B):
            diff += abs(sum-B)
            close_sum = sum
        if sum < B:
            j += 1
        else:
            k -= 1
        i += 1
    return close_sum
print threeSumClosest([-1, 2, 1, -4], 1)
```
    
How many items   in a dictionary?

d={'a':1, 'b':2}
len(d)
len(d.keys()
sum(d.values()))

How many unique values are there in a list?

len(set(mystr))

#### frequency of every char in the string - use count():

for c in set(mystring):
     print (c, mystring.count(c))
    
    
from collections import Counter

def count_characters_one( string ):
    """ Counts with a for loop and a dict. """
    d = {}
    for s in string:
        d[s] = d.get(s,0)+1
    return d

def count_characters_two( string ):
    """ Counts using collections.Count """
    counter = Counter(string)
    return counter    
    
    
####    frequency of every char in the list
    use defaultdict or the following dictionary comprehention
    
counts = {value: things.count(value) for value in things}


#### dot product

  x_vector = (1, 2, 3)
  y_vector = (4, 5, 6)

>>> sum(x * y for x, y in zip(x_vector, y_vector))

what happens if you provide sequences with different lengths?
In that case, zip() ignores the extra values from the longest sequence, which leads to an incorrect result.

  def dot_product(x_vector, y_vector):
      if len(x_vector) != len(y_vector):
          raise ValueError("Vectors must have equal sizes")
      return sum(x * y for x, y in zip(x_vector, y_vector))

#### Flattening a List of Lists

 def flatten_list(a_list):
      flat = []
      for sublist in a_list:
          flat += sublist
      return flat
 
 >>> def flatten_list(a_list):
...     flat = []
...     for sublist in a_list:
...         for item in sublist:
...             flat.append(item)
...     return flat
...

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9],
... ]    

 matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
 ]

>>> flatten_list(matrix)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

#### determine if a string has all unique characters:

Time: O(n)
Space: Additional O(n)

https://github.com/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/unique_chars/unique_chars_solution.ipynb

     def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)

"""

    def has_unique_chars(self, string):
        if string is None:
            return False
        chars_set = set()
        for char in string:
            if char in chars_set:
                return False
            else:
                chars_set.add(char)
        return True


https://github.com/alexhagiopol/cracking-the-coding-interview/blob/master/python_solutions/chapter_01_arrays_and_strings/problem_01_01_is_unique.py

https://github.com/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/permutation/permutation_solution.ipynb

#### Implement an algorithm to determine if a string has all unique characters.
------------------------------------------------------------------------------
What if you cannot use additional data structures?
 
Solution:
Assume that the input string will contain only ASCII characters. Traverse the
string one character at a time and use a hash table to record which characters
have been observed. If a character is observed more than once, return False.
If no character is observed more than once, return True. Because we assumed that
the string would contain only ASCII characters, we can implement the hash table as
a 128-wide bit vector that uses a character's ASCII value as its hash code.
Time complexity: O(N) where N is the length of the of the linearly traversed string.
Space complexity: O(1) because bit vector size does not scale with input string length.
Follow-up discussion (unimplemented):
If we cannot use additional structures, we can do O(N^2) character comparisons
to check for uniqueness. If we are allowed to modify the original string, we
could sort it in place in N*log(N) time and test consecutive characters for equality.
"""


def is_unique(input_string):
    hash_table = [False]*128  # hash table implemented as 128 bit vector
    for character in input_string:  # inspect each character
        index = ord(character)  # convert character into its ASCII value
        if hash_table[index]:  # check if bit at this ASCII value is True
            return False
        hash_table[index] = True  # add unobserved character to hash table
    return True



#### Given two strings, write a method to decide if one is a permutation of the
other.
Example:
("alex", "lexa") -> True
Solution:
We assume that the input strings will contain only ASCII characters and that upper
case characters are distinct from lower case ones i.e. "Alex" is not a permutation
of "alex". We define a permutation as a rearrangement of characters i.e. two strings
that are permutations of each other must contain exactly the same characters with the
same frequency. If two strings have unequal length they cannot be permutations.
We count character appearances using a 128 wide bit vector. We
traverse each string one character at a time. Each time we observe a character, we flip
the bit corresponding at the index corresponding to its ASCII value. If we traverse two
strings which both contain exactly the same number of characters with the same character
frequency, the bit vector will be all 0s at the end of the two traversals. This is because
for two strings that are permutations, each bit will be flipped an even number of
times in total.
Time complexity: O(N) where N is the length of the linearly traversed strings.
Space complexity: O(1) because bit vector does not scale with string length.
"""
def are_permutations(s1, s2):
    if len(s1) != len(s2):  # unequal length means not permutations
        return False
    
    character_counts = 128 * [0]  # create counts vector
    for char in s1: 
        index = ord(char)
        character_counts[index] += 1  # count the number of each letter
    for char in s2: 
        index = ord(char)
        character_counts[index] -= 1
        if character_counts[index] < 0:
            return False
    return True



Time: O(n log n) from the sort, in general
Space: O(n)
    
def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        return sorted(str1) == sorted(str2)
    

Notes:

Since the characters are in ASCII, we could potentially use an array of size 128 (or 256 for extended ASCII), where each array index is equivalent to an ASCII value
Instead of using two hash maps, you could use one hash map and increment character values based on the first string and decrement based on the second string
You can short circuit if the lengths of each string are not equal, although len() in Python is generally O(1) unlike other languages like C where getting the length of a string is O(n)
Complexity:


Time: O(n)
Space: O(n)    
    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        unique_counts1 = defaultdict(int)
        unique_counts2 = defaultdict(int)
        for char in str1:
            unique_counts1[char] += 1
        for char in str2:
            unique_counts2[char] += 1
        return unique_counts1 == unique_counts2    
    
    
def merge_sorted_lists(l1, l2):
    sorted_list = []

    while (l1 and l2):
        if (l1[0] <= l2[0]): # Compare both heads
            item = l1.pop(0) # Pop from the head
        else:
            item = l2.pop(0)
            
        sorted_list.append(item)

    # Add the remaining of the lists
    sorted_list.extend(l1 if l1 else l2)

    return sorted_list


print " FIND 2 elements in list where sum=target"
#-------------------------------------------
l=[6,2,3,4,5,1]
target=6
d={}

for el in l:
    if d.has_key(target-el):
          print "Found:", el, d[target-el]
    else:
          d[el]=el

################
print " Dictionary examples"
################
print " dict traversal  #1"
for key in d.keys():
   print "key=", key, "value=", d[key]

print " dict traversal  #2"
for key, value in d.items():
   print "key=", key, "value=", value

missing=d.get(15,0)
print "missing key=15 default value=", missing
print d.keys()
print d.values()
print d.items()


print "Count the number of times each word is seen in a file"
myfile=("A","B","C","D","A")
words = {}

for word in myfile:
    occurrences = words.setdefault(word, 0)
    words[word] = occurrences + 1

for key, value in words.items():
   print "key=", key, "value=", value

##################
print " List examples"
###############
print "list=", l
l.sort()
print "sorted=", l
l.sort(reverse=True)
print "reverse sorted=",l

#################
print " SET examples"
################
my_list=[1,2,2,3,3,3,4]
a=set(my_list)
print a
b=set([3,4,22])
print b.issubset(a)
print a.difference(b)
print b.difference(a)
if len(a.difference(a)) == 0:
   print "No difference with myself"

a.discard(4)
a.discard(8)

union= a | b
print union
print a.union(b)

####################
print  "String examples"
####################
s='abcdef'
print len(s)
print "find example exists", s.find('a')
print "find example not exists", s.find('g')
try:
    s.index('g')
except:
   print "exceptioni in index()"
else:
  print "else"




def permutations(word):
    print "All permutations of " , word
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

print permutations("123")

