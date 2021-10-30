# https://medium.com/hackernoon/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

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
