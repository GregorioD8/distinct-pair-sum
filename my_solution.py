def distinct_pair_sum(arr, k):
    pairs = set() # Use a set to store unique pairs, ensuring each pair is distinct and automatically ignoring duplicates
    
    for i in range(len(arr) - 1):
        # Form a pair of consecutive elements
        pair = (arr[i], arr[i + 1])
        
        # Check if their sum equals the target value k
        if sum(pair) == k:
            # Sort the pair to ensure unique representation
            sorted_pair = tuple(sorted(pair))
            pairs.add(sorted_pair)
    
    # Convert each tuple in pairs set to a list
    return [list(pair) for pair in pairs]

# Test cases
print(distinct_pair_sum([0, 1, 1, 2, 0, 1, 1], 2))  # Expected output: [[1, 1], [2, 0]]
print(distinct_pair_sum([3, 4, 2, 1, 5, 2, 8, 2], 10))  # Expected output: [[2, 8]]