https://medium.com/towards-data-engineering/array-problems-you-cant-miss-for-data-engineering-interviews-part-1-75b34b2c4e34

https://medium.com/towards-data-engineering/array-problems-you-cant-miss-for-data-engineering-interviews-part-2-94829bfe397e
 
https://python.plainenglish.io/top-string-manipulation-interview-questions-for-data-engineer-roles-with-comprehensive-solutions-13845eb5971b
 
https://python.plainenglish.io/coding-problems-every-data-engineer-should-know-lessons-from-multiple-interviews-faa1ceffc5b5

https://python.plainenglish.io/frequently-asked-binary-search-questions-for-data-engineering-interviews-top-questions-to-know-8321e10bb8b8

1. Second Largest
Write a Python program to find the second largest element in an array. You should solve this problem without sorting the array. If there are duplicate elements, they should be treated as individual values.

def find_second_largest(arr):
    # Check if the array has at least two unique elements
    if len(arr) < 2:
        return "Array does not have enough elements"

    first, second = float('-inf'), float('-inf')

    for num in arr:
        # If the current element is greater than the largest element found so far
        if num > first:
            second = first
            first = num
        # If the current element is not the largest but greater than the second largest
        elif num > second and num != first:
            second = num

    # Check if second largest was updated from its initial value
    if second == float('-inf'):
        return "No second largest element found"  # This means all elements are the same or there was no second distinct largest value

    return second

# Example usage
arr = [5, 7, 8, 8, 6, 4, 7]
second_largest = find_second_largest(arr)
print("The second largest element is:", second_largest)

# The second largest element is: 7
2. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates so each element appears only once. Return the length of the modified array and modify the input array to contain unique elements in the first `k` positions, where `k` is the length of the unique elements.

def remove_duplicates(nums):
    # Check if the array is empty
    if not nums:
        return 0

    unique_index = 0

    for i in range(1, len(nums)):
        # Check if the current number is different from the last unique number
        if nums[i] != nums[unique_index]:
            unique_index += 1  # Move the pointer for unique elements
            nums[unique_index] = nums[i]  # Place the unique element at the unique_index

    # The length of unique elements is unique_index + 1
    return unique_index + 1

# Test the function with an example input
arr = [1, 1, 2, 3, 3, 4]
k = remove_duplicates(arr)

# Output the result
print(f"The number of unique elements is: {k}")
print("Modified array:", arr[:k] + ['_'] * (len(arr) - k))

# The number of unique elements is: 4
# Modified array: [1, 2, 3, 4, '_', '_']
3. Rotate Array
You are given an array `arr` of integers and a number `k`. Your task is to rotate the array `k` steps to the right, meaning each element in the array should move `k` positions forward. If `k` exceeds the array's length, it should rotate circularly.

def rotate_array(arr, k):
    """
    Rotates an array to the right by k steps.

    """
    # handles cases where k is larger than the length of arr
    n = len(arr)
    k %= n
    
    # Step 1: Reverse the entire array
    arr.reverse()
    
    # Step 2: Reverse the first k elements
    arr[:k] = reversed(arr[:k])
    
    # Step 3: Reverse the remaining elements from k to end
    arr[k:] = reversed(arr[k:])
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
result = rotate_array(arr, k)
print("Rotated Array:", result)

# Rotated Array: [4, 5, 1, 2, 3]
4. Move Zeroes
Given an array nums, write a function to move all 0’s to the end of it while maintaining the relative order of the non-zero elements.

def move_zeroes(nums):
    """
    Moves all zeroes in the list 'nums' to the end while maintaining the order
    of non-zero elements. This is done in-place.

    """
    last_non_zero = 0

    for i in range(len(nums)):
        
        if nums[i] != 0:
            # Swap the elements to push the zero to the right
            nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]

            last_non_zero += 1

# Example usage
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print("Output:", nums) # Output: [1, 3, 12, 0, 0]
5. Union of Two Sorted Arrays with Duplicate Elements
Given two sorted arrays, arr1 and arr2, write a function to find the union of these two arrays. The union of two arrays is a list that includes all elements from both arrays. Since the arrays are sorted, the union should also be sorted. Duplicates from each array should be preserved in the result.

def union_of_two_sorted_arrays(arr1, arr2):
    
    i, j = 0, 0
    union_result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            # Add the smaller element and move the pointer in arr1
            union_result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            # Add the smaller element and move the pointer in arr2
            union_result.append(arr2[j])
            j += 1
        else:
            # If both elements are the same, add only once and move both pointers
            union_result.append(arr1[i])
            i += 1
            j += 1

    # Append remaining elements of arr1 (if any)
    while i < len(arr1):
        union_result.append(arr1[i])
        i += 1

    # Append remaining elements of arr2 (if any)
    while j < len(arr2):
        union_result.append(arr2[j])
        j += 1

    return union_result

# Test the function
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]
result = union_of_two_sorted_arrays(arr1, arr2)
print("Union of arr1 and arr2:", result) # [1, 2, 3, 4, 5, 6, 7]
6. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1s in the array.

def find_max_consecutive_ones(nums):
    max_count = 0  
    count = 0      
    
    for num in nums:
        if num == 1:
            count += 1
            # Update max_count if count exceeds the current max_count
            max_count = max(max_count, count)
        else:
            # Reset count if the current number is 0
            count = 0
    
    return max_count

# Example usage:
nums = [1, 1, 0, 1, 1, 1]
print("Max Consecutive Ones:", find_max_consecutive_ones(nums)) # 3
7. Longest Sub-Array with Sum K
Given an array of integers arr and an integer K, find the length of the longest sub-array whose sum is equal to K. If there is no such sub-array, return 0.

def longest_subarray_with_sum_k(arr, K):
    # Dictionary to store the first occurrence of each cumulative sum
    prefix_sum_map = {}
    current_sum = 0 
    max_length = 0  
    
    for i in range(len(arr)):
        current_sum += arr[i]  # Update cumulative sum
        
        # Check if current cumulative sum is equal to K
        if current_sum == K:
            max_length = i + 1
        
        # If (current_sum - K) exists in the map, update max_length
        if (current_sum - K) in prefix_sum_map:
            subarray_length = i - prefix_sum_map[current_sum - K]
            max_length = max(max_length, subarray_length)
        
        # Store the current_sum in the map if not already present
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
    
    return max_length

# Example usage
arr = [10, 5, 2, 7, 1, 9]
K = 15
result = longest_subarray_with_sum_k(arr, K)
print("The length of the longest sub-array with sum", K, "is:", result) # 4
8. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

def two_sum(nums, target):
    num_to_index = {}

    for index, num in enumerate(nums):
        # Calculate the complement that would add up to the target
        complement = target - num

        # Check if complement is already in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # Otherwise, store the index of the current number in the dictionary
        num_to_index[num] = index

    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
output = two_sum(nums, target)

print("Input: nums =", nums, "target =", target)
print("Output:", output) # [0, 1]
9. Maximum Subarray (Kadane’s Algorithm)
Given an integer array nums, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

def max_subarray(nums):
    max_sum = current_sum = nums[0]

    for i in range(1, len(nums)):
        # Determine whether to add nums[i] to current_sum or start fresh from nums[i].
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update max_sum if the current_sum is higher.
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print("The maximum subarray sum is:", result) # 6 ([4, -1, 2, 1])
10. Majority Element
Given an integer array nums, find all elements that appear more than n/3 times.

def majorityElement(nums):
    dict = {}
    result  = []
    for candidate in nums:
        if candidate in dict:
            dict[candidate] += 1
        else:
            dict[candidate] = 1
    for key in dict:
        if dict[key] > len(nums)//3:
            result .append(key)
    return result 

# Test cases
nums1 = [3, 2, 3]
nums2 = [1, 1, 1, 3, 3, 2, 2, 2]

print("Input:", nums1)
print("Output:", majorityElement(nums1))  # Output: [3]

print("\nInput:", nums2)
print("Output:", majorityElement(nums2))  # Output: [1, 2]

python.plainenglish.io


###  PArt 2 

1. 3Sum:
Given an arr[] and an integer sum. Find if a triplet in the array sums up the given integer sum.

def three_sum(arr, sum):
    n = len(arr)

    # Sort the elements
    arr.sort()

    # Fix the first element one by one
    # and find the other two elements
    for i in range(n - 2):
        l = i + 1  # index of the first element
        r = n - 1  # index of the last element

        while l < r:
            curr_sum = arr[i] + arr[l] + arr[r]
            if curr_sum == sum:
                print(f"Triplet is {arr[i]}, {arr[l]}, {arr[r]}")
                return True
            elif curr_sum < sum:
                l += 1
            else:
                r -= 1

    return False

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print("3Sum Result:", three_sum(nums, 3))

# Triplet is 0, 1, 2
# 3Sum Result: True
2. Array Leaders
Given an array, a leader is an element greater than all elements to its right.

def find_leaders(arr):
    """
    Function to find leaders in the given array.

    """
    n = len(arr)
    leaders = []       
    max_from_right = arr[-1]  # Start with the last element as the initial leader

    # Rightmost element is always a leader
    leaders.append(max_from_right)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        # If the current element is greater than the max_from_right
        if arr[i] > max_from_right:
            max_from_right = arr[i]  # Update the max_from_right
            leaders.append(max_from_right)

    leaders.reverse()
    return leaders

# Test the function with example input
arr = [16, 17, 4, 3, 5, 2]
leaders = find_leaders(arr)
print("Leaders:", leaders) # [17, 5, 2]
3. Rearrange Array Elements by Sign
Given an array nums containing both positive and negative integers, rearrange the elements so that the positives and negatives alternate.

def rearrange_by_sign(nums):
    # Separate positive and negative numbers while keeping their original order
    positives = [num for num in nums if num > 0]
    negatives = [num for num in nums if num < 0]
    
    # Initialize an empty list for the rearranged array
    rearranged = []
    
    # Iterate over both lists to append elements in an alternating order
    for pos, neg in zip(positives, negatives):
        rearranged.append(pos)  # Add positive number
        rearranged.append(neg)  # Add negative number
    
    return rearranged

# Test case
nums = [3, -1, 2, -2, -3, 1]
output = rearrange_by_sign(nums)
print("Output:", output) # [3, -1, 2, -2, 1, -3]
4. Maximum Product Subarray
You are given an integer array nums. Find the contiguous subarray within an array that has the largest product and return its product.

def max_product_subarray(nums):
    """
    Function to find the maximum product subarray.
    
    """
    if not nums:
        return 0 

    max_product = nums[0] 
    min_product = nums[0]
    result = nums[0]       

    for i in range(1, len(nums)):
        num = nums[i]
        
        # Since num can be negative, calculate temporary max before updating min_product
        temp_max = max(num, max_product * num, min_product * num)
        min_product = min(num, max_product * num, min_product * num)
        
        # Update max_product using the temporary value
        max_product = temp_max
        
        # Update the global maximum result
        result = max(result, max_product)
    
    return result


# Test cases and expected outputs
nums1 = [2, 3, -2, 4]  # Expected output: 6 (subarray: [2, 3])
nums2 = [-2, 0, -1]    # Expected output: 0 (subarray: [0])
nums3 = [-2, 3, -4]    # Expected output: 24 (subarray: [-2, 3, -4])
nums4 = [0, 2, -1, -3, 4]  # Expected output: 12 (subarray: [-1, -3, 4])
5. Best Time to Buy and Sell Stock
You are given an array of prices where prices[i] represent the price of a stock on the i-th day. Your task is to maximize your profit by choosing a single day to buy one stock and a different day to sell that stock in the future. If no profit can be achieved, return 0

def maxProfit(prices):
    """
    Function to calculate the maximum profit from a given list of stock prices.

    """

    min_price = float('inf')
    max_profit = 0            

    for price in prices:
        # Update the minimum price
        if price < min_price:
            min_price = price
        # Calculate profit for the current price and update max_profit
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example Input
prices = [7, 1, 5, 3, 6, 4]

# Function Call and Output
result = maxProfit(prices)
print("Maximum Profit:", result) # Maximum Profit: 5
6. Count subarrays with the given sum
You are given an array of integer numbers and an integer target. Write a function to count the subarrays that sum up to the given target.

def count_subarrays_with_sum(nums, target):
    """
    Count the number of subarrays with a given sum.

    """
    # Initialize with 0 for the case when the prefix sum itself equals the target
    prefix_sum_freq = {0: 1}  
    prefix_sum = 0 
    count = 0 

    for num in nums:
        # Add the current number to the running prefix sum
        prefix_sum += num

        # Check if there is a prefix sum that would form the required sum with the current prefix
        if prefix_sum - target in prefix_sum_freq:
            count += prefix_sum_freq[prefix_sum - target]

        # Update the prefix sum frequency map
        if prefix_sum in prefix_sum_freq:
            prefix_sum_freq[prefix_sum] += 1
        else:
            prefix_sum_freq[prefix_sum] = 1

    return count


# Example usage
nums = [1, 1, 1]
target = 2
result = count_subarrays_with_sum(nums, target)

# Display the result with input details
print("Number of Subarrays with Target Sum:", result) 
# Number of Subarrays with Target Sum: 2
7. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive element sequence.

def longest_consecutive(nums):
    """
    Function to find the length of the longest consecutive sequence in an unsorted array.

    """
    num_set = set(nums)
    longest_sequence = 0

    for num in num_set:
        # Check if it is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            # Update the longest sequence
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence

# Test the function with an example input
nums = [100, 4, 200, 1, 3, 2]
output = longest_consecutive(nums)
print(f"Longest Consecutive Sequence Length: {output}")
# Longest Consecutive Sequence Length: 4


### Part 3 

1. Remove Outermost Parentheses
Write a function to remove the outermost parentheses from a valid string containing only parentheses. The input will always be a valid string of parentheses, with no extra characters or spaces.

def remove_outer_parentheses(s: str) -> str:
    # Initialize an empty stack and an empty result list
    stack = []
    result = []

    for char in s:
        if char == '(':
            # Only add '(' to result if stack is not empty, which means it is not the outermost '('
            if stack:
                result.append(char)
            stack.append(char)  # Push '(' to stack
        elif char == ')':
            stack.pop()  # Pop the last '(' from stack
            # Only add ')' to result if stack is not empty after popping, which means it is not the outermost ')'
            if stack:
                result.append(char)

    # Join result list to form the output string
    return ''.join(result)

# Test cases
print(remove_outer_parentheses("(()())(())"))       # Expected output: "()()()"
print(remove_outer_parentheses("(()())(())(()(()))")) # Expected output: "()()()()(())"
print(remove_outer_parentheses("()()"))             # Expected output: ""
2. Reverse Words in a String
Function to reverse the order of words in a given string.

def reverse_words_in_string(s):
    """
    This function takes a string input and returns the string with the order of words reversed.

    """
    # Step 1: Split the string into words
    words = s.split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 3: Join the reversed list back into a single string
    reversed_string = " ".join(reversed_words)
    
    return reversed_string

# Example usage
input_string = "Hello World"
output_string = reverse_words_in_string(input_string)
print("Reversed String:", output_string)
# Reversed String: World Hello
3. Longest Common Prefix
Given an array of strings, find the longest common prefix among all strings. If there is no common prefix, return an empty string ‘ ’.

def longest_common_prefix(strs):
    """
    Function to find the longest common prefix among a list of strings.
    
    """
    # if the list is empty, return an empty string
    if not strs:
        return ""

    prefix = ""
    
    # Use zip to pair characters at the same position in each string
    for chars in zip(*strs):
        # Use a set to identify unique characters at this position
        if len(set(chars)) == 1:
            # All characters match, add it to the prefix
            prefix += chars[0]
        else:
    
            break

    return prefix

# Test cases
print(longest_common_prefix(["flower", "flow", "flight"]))  # Expected output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Expected output: ""
print(longest_common_prefix(["apple", "ape", "april"]))    # Expected output: "ap"
4. Rotate String
Given two strings, A and B, write a function that returns True if and only if B is a rotation of A. A string B is a rotation of A if we can shift the characters in A to get B.

def is_rotation(A: str, B: str) -> bool:
    """
    Checks if string B is a rotation of string A.
    
    """
    # Step 1: Check if lengths of A and B are the same
    if len(A) != len(B):
        return False

    # Step 2: Concatenate A with itself to capture all possible rotations
    double_A = A + A

    # Step 3: Check if B is a substring of the concatenated string
    return B in double_A

# Example Usage
A = "abcde"
B1 = "cdeab"  # Expected output: True
B2 = "abced"  # Expected output: False

# Test cases
print(f"Is '{B1}' a rotation of '{A}'? -> {is_rotation(A, B1)}")  # True
print(f"Is '{B2}' a rotation of '{A}'? -> {is_rotation(A, B2)}")  # False
5. Valid Anagram
Given two strings s and t, write a function to determine if t is an anagram of s. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, `anagram` and `nagaram` are anagrams.

def is_anagram(s: str, t: str) -> bool:
    """
    Function to check if string t is an anagram of string s.

    """

    # Check if the lengths of both strings are equal.
    # If not, they cannot be anagrams.
    if len(s) != len(t):
        return False

    # Create dictionaries to count the frequency of each character in both strings.
    char_count_s = {}
    char_count_t = {}

    # Count each character in string s
    for char in s:
        char_count_s[char] = char_count_s.get(char, 0) + 1

    # Count each character in string t
    for char in t:
        char_count_t[char] = char_count_t.get(char, 0) + 1

    # Compare the character counts; if they are the same, s and t are anagrams
    return char_count_s == char_count_t

# Test cases
s1 = "anagram"
t1 = "nagaram"
print(f"Is '{t1}' an anagram of '{s1}'? : {is_anagram(s1, t1)}")  # Output: True

s2 = "rat"
t2 = "car"
print(f"Is '{t2}' an anagram of '{s2}'? : {is_anagram(s2, t2)}")  # Output: False
6. Sort Characters By Frequency:
Write a function that takes a string s and returns a new string with the characters sorted in descending order based on their frequency in the original string. If two characters have the same frequency, their order in the output does not matter.

from collections import Counter

def sort_characters_by_frequency(s: str) -> str:
    # Step 1: Count the frequency of each character in the input string.
    # Gives us a dictionary-like object
    freq_counter = Counter(s)

    # Step 2: Sort characters by frequency in descending order.
    # - key=lambda x: x[1] sorts these pairs by frequency (x[1]) in descending order
    sorted_characters = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Build the result string by repeating each character according to its frequency.
    result = ''.join(char * freq for char, freq in sorted_characters)

    return result

# Test the function with example input
s = "tree"
output = sort_characters_by_frequency(s)
print(f"Input: {s}")
print(f"Output: {output}")
7. Maximum Nesting Depth of the Parentheses
Finding the Maximum Nesting Depth of Parentheses.

def maxDepth(s: str) -> int:
    current_depth = 0
    max_depth = 0

    for char in s:
        # If we encounter an opening parenthesis, increase the current depth
        if char == '(':
            current_depth += 1
            # Update the maximum depth if the current depth exceeds it
            max_depth = max(max_depth, current_depth)
        
        # If we encounter a closing parenthesis, decrease the current depth
        elif char == ')':
            current_depth -= 1

    return max_depth

# Test the function with a sample input
input_str = "(1+(2*3)+((8)/4))+1"
output = maxDepth(input_str)
print(f"Output: {output}")
# Output: 3
8. String Compression
Given a string s, write a function that compresses the string based on the counts of consecutive characters. For instance, the string “aaabbcc” would become “a3b2c2”.

def compress_string(s):
    # Check for an empty string
    if not s:
        return s
    
    # Initialize variables
    compressed = [] 
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # If current character is same as previous
            count += 1
        else:
            # Append the character and its count to compressed list
            compressed.append(s[i - 1] + str(count))
            count = 1  # Reset count for new character

    # Append the last character and its count
    compressed.append(s[-1] + str(count))

    # Join the list into a compressed string
    compressed_str = ''.join(compressed)

    return compressed_str 

# Example usage
input_str = "aabcccccaaa"
output_str = compress_string(input_str)
print(f"Input: {input_str}\nCompressed Output: {output_str}")

# Input: aabcccccaaa
# Compressed Output: a2b1c5a3
9. Count the number of substrings
Write a function that takes a string as input and counts the total number of possible substrings.

def count_substrings(s):
    # Initialize the count of substrings to zero
    count = 0
    n = len(s)

    for i in range(n):
        # For each starting point, iterate over all possible ending points
        for j in range(i, n):
            # A substring exists from index i to index j
            count += 1

    return count

# Test the function with an example input
input_str = "abc"
print(f"The total number of substrings in '{input_str}' is: {count_substrings(input_str)}")

# The total number of substrings in 'abc' is: 6
10. Next higher palindromic number using the same set of digits
Given a positive integer, find the next higher palindromic number that can be formed using the same digits as the input number. If no such palindrome exists, return -1.

from itertools import permutations

def is_palindrome(num_str):
    """Check if a string is a palindrome."""
    return num_str == num_str[::-1]

def next_palindromic_number(num):
    """
    Find the next higher palindromic number using the same set of digits.
    
    """
    # Convert number to list of digits and sort them
    digits = sorted(str(num))
    
    # Generate all unique permutations that are higher than the current number
    for perm in sorted(set(permutations(digits))):
        candidate = ''.join(perm)
        
        # Skip numbers that are not greater than the original number
        if int(candidate) <= num:
            continue
        
        # Check if the permutation is a palindrome
        if is_palindrome(candidate):
            return int(candidate)

    return -1

# Example usage
number = 12321
result = next_palindromic_number(number)
print(f"Next palindromic number using the same digits as {number} is: {result}")

#### Part 4


1. Find the Most Frequent Element in a List
Given a list of integers, find the element that appears the most frequently.

def most_frequent(arr):
   """

    The function uses a dictionary to store the frequency of each element and 
    then finds the element with the maximum frequency.

    """
       freq_dict = {}
       for num in arr:
           if num in freq_dict:
              # If the number is already in the dictionary, increment its frequency by 1
               freq_dict[num] += 1
           else:
              # If the number is not in the dictionary, add it with an initial frequency of 1
               freq_dict[num] = 1
       # Use the max function to find the key with the maximum value in the dictionary
       return max(freq_dict, key=freq_dict.get)


arr = [1, 3, 2, 1, 2, 2, 3, 3, 3, 1]
print(most_frequent(arr))  # Output: 3
2. Find the Missing Number in an Array
Find the missing number in an array containing `n` distinct numbers from 0 to `n`.

def missing_number(arr):
   """
    
    The function assumes that the array contains unique integers from 0 to n, 
    with one number missing, and finds the missing number using the formula 
    for the sum of the first n natural numbers.

    """
       n = len(arr)
       # Calculate the sum of numbers from 0 to n using the formula n * (n + 1) // 2
       total_sum = n * (n + 1) // 2
       return total_sum - sum(arr)


arr = [3, 0, 1]
print(missing_number(arr))  # Output: 2
3. Find Duplicates in an Array
Given an array of integers, find all duplicates in the array.

def find_duplicates(arr):
    """
    This function finds and returns all duplicate elements from the input array.

    """
       seen = set()
       duplicates = set()
       for num in arr:
           # If the number has been seen before, it's a duplicate
           if num in seen:
               duplicates.add(num)
           else:
              # If the number is new, add it to the 'seen' set
               seen.add(num)
       return list(duplicates)


   arr = [4, 3, 2, 7, 8, 2, 3, 1]
   print(find_duplicates(arr))  # Output: [2, 3]
4. Group Anagrams
Given an array of strings, group the anagrams together.

def group_anagrams(strs):
    """

    Anagrams are words that contain the same characters but in a different 
    order. This function sorts each word in the list, uses the sorted word 
    as a key, and groups all the words that share the same sorted characters 
    into sublists.

    """
    
    anagram_map = {}

    for s in strs:
        # Sort the characters in the string to get the key
        sorted_str = ''.join(sorted(s))
        
        # If the sorted string is already a key, append the word to its list
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(s)
        else:
            # Otherwise, create a new key with the word as the first entry
            anagram_map[sorted_str] = [s]

    # Return the values of the dictionary, which are lists of anagrams
    return list(anagram_map.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))

# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
5. Binary Search
Implement binary search to find an element in a sorted array.

def binary_search(arr, target):
    """
    Performs binary search on a sorted array to find the target element.

    """
       # Initialize left and right pointers
       left, right = 0, len(arr) - 1
       while left <= right:
           mid = (left + right) // 2
           # Check if the middle element is the target
           if arr[mid] == target:
               return mid
           # If target is greater, ignore the left half
           elif arr[mid] < target:
               left = mid + 1
           # If target is smaller, ignore the right half
           else:
               right = mid - 1
       return -1 # Target not found in the array


arr = [1, 2, 3, 4, 5, 6, 7]
target = 5
print(binary_search(arr, target))  # Output: 4 (index of 5)
6. Move Zeroes
Given an array `nums`, write a function to move all `0`s to the end of it while maintaining the relative order of the non-zero elements.

def move_zeroes(nums):
    """
    Moves all zeroes in the input list to the end while maintaining the 
    relative order of the non-zero elements.

    """
    zero_idx = 0
    
    for i in range(len(nums)):
        # If current element is non-zero, swap it with the element at zero_idx
        if nums[i] != 0:
            nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
            zero_idx += 1


# Example usage
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
7. Reverse a Linked List
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next # Store the next node
        curr.next = prev # Reverse the link by pointing the current node to the previous one
        prev = curr # Move the previous pointer to the current node
        curr = next_node # Move the current pointer to the next node in the original list
    
    return prev


# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
new_head = reverse_list(head)
# Output should be 3 -> 2 -> 1 -> None
8. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. It is the kth largest element in sorted order, not the kth distinct element.

def find_kth_largest(nums, k):
    """
    Find the k-th largest element in an unsorted list.

    """
    # Sort the list in descending order
    sorted_nums = sorted(nums, reverse=True)

    # Return the k-th largest element
    return sorted_nums[k-1]

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))  # Output: 5
9. Subarray Sum Equals K
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

def subarray_sum(a, K):
    """
    This function counts the number of subarrays in a given array 'a' that have a sum equal to 'K'.

    """
    
    n = len(a)

    hash = {}
    
    count, sum = 0, 0
    
    for i in range(n):
        # Add the current element to the cumulative sum
        sum += a[i]
        
        # If the cumulative sum equals K, increment the count
        if sum == K:
            count += 1
        
        # If (sum - K) exists in the hash, it means there's a subarray
        # that sums to K, so we add the frequency of that sum to the count
        if (sum - K) in hash:
            count += hash[sum - K]
        
        # Update the frequency of the current cumulative sum in the hash
        if sum in hash:
            hash[sum] += 1
        else:
            hash[sum] = 1
    
    return count


# Example usage:
nums = [1, 1, 1, -1]
k = 2
print(subarray_sum(nums, k))  # Output: 3
10. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

def longest_substring(s):
   """
    This function takes a string `s` as input and returns the length of the longest
    substring without repeating characters.

    """
       char_index_map = {}
       start = 0
       max_len = 0

       for i, char in enumerate(s):
            # If the character is already in the map and its index is greater than or equal to start,
            # move the start pointer to the right of the previous occurrence of the character
           if char in char_index_map and char_index_map[char] >= start:
               start = char_index_map[char] + 1
           char_index_map[char] = i
           # Calculate the length of the current substring and update the maximum length if necessary
           max_len = max(max_len, i - start + 1)

       return max_len


s = "abcabcbb"
print(longest_substring(s))  # Output: 3 ("abc")

### Part 5 
1. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if inserted in order.

def search_insert_position(nums, target):
    """
    Find the index at which a target should be inserted in a sorted array.
    
    """
    left, right = 0, len(nums) - 1
    
    # Perform binary search to find the correct position
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is equal to the middle element
        if nums[mid] == target:
            return mid  # Target found, return its position
        
        # If target is greater than middle element, search in the right half
        elif nums[mid] < target:
            left = mid + 1
        
        # If target is smaller than middle element, search in the left half
        else:
            right = mid - 1
    
    # If target is not found, return the insertion position
    return left


Example:
  >>> search_insert_position([1, 3, 5, 6], 5)
        2
  >>> search_insert_position([1, 3, 5, 6], 2)
        1
  >>> search_insert_position([1, 3, 5, 6], 7)
        4
  >>> search_insert_position([1, 3, 5, 6], 0)
        0

Time Complexity:
O(log n), where 'n' is the number of elements in the array.
    
Space Complexity:
O(1) since no extra space is used apart from variables.
2. Floor & Celi in a Sorted Array
Given a sorted array arr of n integers and a target integer x, your task is to find the floor and ceiling of x in the array. The floor of x is the greatest element in arr that is less than or equal to x, and the ceiling of x is the smallest element in arr that is greater than or equal to x

def find_floor_ceil(arr, target):
    """
    The floor is the greatest element in the array that is less than or 
    equal to the target.

    The ceil is the smallest element in the array that is greater than or 
    equal to the target.
    
    """
    
    # Initialize floor and ceil values as None
    floor, ceil = None, None
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            # If the target is exactly found, it's both the floor and ceil
            return arr[mid], arr[mid]
        
        if arr[mid] < target:
            # If the middle element is less than the target, it's a candidate for the floor
            floor = arr[mid]
            low = mid + 1  # Move right to search for closer floor
        else:
            # If the middle element is greater than the target, it's a candidate for the ceil
            ceil = arr[mid]
            high = mid - 1  # Move left to search for closer ceil
    
    return floor, ceil



Example:
    >>> find_floor_ceil([1, 2, 4, 6, 10], 5)
    (4, 6)
    >>> find_floor_ceil([1, 2, 4, 6, 10], 6)
    (6, 6)
    >>> find_floor_ceil([1, 2, 4, 6, 10], 11)
    (10, None)
    >>> find_floor_ceil([1, 2, 4, 6, 10], 0)
    (None, 1)
3. Find the First and Last Position of the Element in Sorted Array
Find a given target value's starting and ending position in an array of integer numbers sorted in non-decreasing order.

def find_first_and_last_position(nums: List[int], target: int) -> List[int]:
    """
    This function finds the first and last position of a target element in a 
    sorted array.
  
    """
    
    # Helper function to find the first occurrence of the target
    def find_first(nums, target):
        low, high = 0, len(nums) - 1
        first_pos = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first_pos = mid  # Found target, but continue searching in the left half
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first_pos
    
    # Helper function to find the last occurrence of the target
    def find_last(nums, target):
        low, high = 0, len(nums) - 1
        last_pos = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last_pos = mid  # Found target, but continue searching in the right half
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last_pos

    # Find the first and last occurrence of the target
    first_pos = find_first(nums, target)
    last_pos = find_last(nums, target)

    # If the target is not found, return [-1, -1]
    if first_pos == -1:
        return [-1, -1]

    return [first_pos, last_pos]


# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(find_first_and_last_position(nums, target))  # Output: [3, 4]
4. Search in Rotated Sorted Array
You are given a sorted integer array, which contains distinct values. However, the array has been rotated at an unknown pivot point, meaning that some portions of the array are shifted to the beginning while the rest remain in sorted order. Given a target value of k, your task is to find the index of k in the rotated array. If k is not present, return -1.

def search_in_rotated_array(nums, target):
    """
    Searches for a target value in a rotated sorted array using binary search.

    """
    # Initialize the start and end pointers for the binary search
    start, end = 0, len(nums) - 1
    
    while start <= end:
        # Find the middle index
        mid = (start + end) // 2
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        
        # Determine if the left half is sorted
        if nums[start] <= nums[mid]:
            # If target is in the left sorted portion, narrow the search to that half
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # Otherwise, the right half must be sorted
        else:
            # If target is in the right sorted portion, narrow the search to that half
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    # If the target is not found, return -1
    return -1

# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_in_rotated_array(nums, target)
print(f"Target found at index: {result}")  
# Output: 4
5. Determine how many times a sorted array has been rotated
You are given a sorted array that has been rotated k times. You need to find k, the number of rotations

def find_rotation_count(arr):
    low, high = 0, len(arr) - 1

    # If the array is not rotated at all
    if arr[low] <= arr[high]:
        return 0

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is the minimum (pivot) element
        if arr[mid] < arr[mid - 1] and arr[mid] <= arr[mid + 1]:
            return mid

        # Decide whether to search in the left or right half
        if arr[mid] <= arr[high]:
            high = mid - 1  # Search in the left half
        else:
            low = mid + 1   # Search in the right half

    return -1

# Test the function
arr = [15, 18, 2, 3, 6, 12]
rotation_count = find_rotation_count(arr)
print(f"The array has been rotated {rotation_count} times.") 
# Output: 2
6. Row with max 1s:
You are given a 2D binary matrix, where each row contains only 0s and 1s, sorted in non-decreasing order (all 0s appear before any 1s in each row). Your task is to find the index of the row with the highest number of 1s. If multiple rows have the same maximum count of 1s, return the index of the first such row. If no rows contain a 1, return -1.

# Define the matrix (each row is sorted)
matrix = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1]
]

# Initialize variables to track the maximum count of 1s and the row index
max_count = 0
row_index = -1

# Loop through each row to count the number of 1s
for i, row in enumerate(matrix):
    count_1s = row.count(1)  # Count 1s in the current row
    if count_1s > max_count:  # Update max_count and row_index if current row has more 1s
        max_count = count_1s
        row_index = i


# Output the row with the maximum number of 1s
print(f"Row with the maximum number of 1's is: Row {row_index} with {max_count} ones.")
# Output: Row with the maximum number of 1's is: Row 2 with 4 ones.
7. Search a 2D Matrix:
Given a 2D matrix with the following properties:

1. Each row is sorted in ascending order.
2. The first element of each row is greater than the last element of the previous row.

Write an efficient algorithm to search for a target integer in the matrix. Return `True` if the target exists, and `False` otherwise.

from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:  # Check for an empty matrix
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = matrix[mid // n][mid % n]

        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
    
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3


print(search_matrix(matrix, target))  # Output: True
8. Find Peak Element
Given an array `nums`, find a peak element and return its index. An element is considered a peak if it is greater than or equal to its neighbors. We only need to compare corner elements with one neighbor.

def find_peak_element(nums):
    # Initialize the left and right pointers
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2  # Calculate the mid index

        # Check if mid element is a peak
        if nums[mid] > nums[mid + 1]:
            # Peak is on the left side (including mid)
            right = mid
        else:
            # Peak is on the right side
            left = mid + 1

    # When left == right, we have found a peak
    return left

# Example usage:
nums = [1, 2, 3, 1]
print("Peak element index:", find_peak_element(nums))  # Output: 2


