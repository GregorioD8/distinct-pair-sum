def distinct_pair_sum(arr, k):
    """
    Function to find all distinct pairs of consecutive numbers that add up to a given target k.
    
    Parameters:
    arr (list): List of integers to search through.
    k (int): Target sum for each consecutive pair.
    
    Returns:
    list: A list of unique pairs (as lists) that sum to k.
    """
    
    # Step 1: Initialize a set to store unique pairs.
    # Using a set ensures each pair is distinct, and duplicates are automatically ignored.
    pairs = set()
    
    # Step 2: Iterate over the array up to the second-to-last element to check consecutive pairs.
    for i in range(len(arr) - 1):
        # Form a pair with the current and next element
        pair = (arr[i], arr[i + 1])
        
        # Step 3: Check if the sum of the current pair equals the target value k.
        if sum(pair) == k:
            # Sort the pair to ensure unique representation in the set (e.g., (1, 2) and (2, 1) are the same)
            sorted_pair = tuple(sorted(pair))
            # Add the sorted pair to the set (duplicates will be ignored)
            pairs.add(sorted_pair)
    
    # Step 4: Convert each tuple in the pairs set to a list for the final output format
    return [list(pair) for pair in pairs]


# Example test cases
print(distinct_pair_sum([0, 1, 1, 2, 0, 1, 1], 2))  # Expected output: [[1, 1], [2, 0]]
print(distinct_pair_sum([3, 4, 2, 1, 5, 2, 8, 2], 10))  # Expected output: [[2, 8]]
print(distinct_pair_sum([3, 4, 2, 1, 5, 2, 8, 2], 100))  # Expected output: []
print(distinct_pair_sum([], 2))  # Expected output: []
print(distinct_pair_sum([59, 41], 100))  # Expected output: [[59, 41]]
