def two_sum(nums, target):
    # Dictionary to store the index of each number
    num_to_index = {}
    
    # Iterate over the list
    for index, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], index]
        
        # Add the number and its index to the dictionary
        num_to_index[num] = index

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)  # Output: [0, 1]
