https://medium.com/towards-data-engineering/array-problems-you-cant-miss-for-data-engineering-interviews-part-1-75b34b2c4e34

https://medium.com/towards-data-engineering/array-problems-you-cant-miss-for-data-engineering-interviews-part-2-94829bfe397e
 
https://python.plainenglish.io/top-string-manipulation-interview-questions-for-data-engineer-roles-with-comprehensive-solutions-13845eb5971b
 
https://python.plainenglish.io/coding-problems-every-data-engineer-should-know-lessons-from-multiple-interviews-faa1ceffc5b5

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
