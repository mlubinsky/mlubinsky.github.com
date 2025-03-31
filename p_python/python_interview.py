https://medium.com/towards-data-engineering/array-problems-you-cant-miss-for-data-engineering-interviews-part-1-75b34b2c4e34

https://medium.com/towards-data-engineering/array-problems-you-cant-miss-for-data-engineering-interviews-part-2-94829bfe397e
 
https://python.plainenglish.io/top-string-manipulation-interview-questions-for-data-engineer-roles-with-comprehensive-solutions-13845eb5971b
 
 
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
 
