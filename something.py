def Measure(weights, l1, l2):
    sum_l1 = sum(weights[i] for i in l1)
    sum_l2 = sum(weights[i] for i in l2)
    
    if sum_l1 > sum_l2:
        return -1  # l1 is heavier
    elif sum_l1 < sum_l2:
        return 1   # l2 is heavier
    else:
        return 0   # Equal weights (should not happen in this problem)

def find_heavy(weights, indices):
    # Base case: If there's only one element left, return its index
    if len(indices) == 1:
        return indices[0]  # Return the index of the heavier box
    
    # Split the indices into two halves
    mid = len(indices) // 2
    left_half = indices[:mid]
    right_half = indices[mid:]

    # Compare the two halves using Measure function
    result = Measure(weights, left_half, right_half)

    # Recursively search in the heavier half
    if result == -1:  # Left side is heavier
        return find_heavy(weights, left_half)
    else:  # Right side is heavier
        return find_heavy(weights, right_half)

# Example case
weights = [5, 5, 5, 5, 5, 6, 5, 5, 5]  # The heavy box is at index 5
size = len(weights)

# Start with the full list of indices
indices = list(range(size))

# Find and print the index of the heavier box
heavier_index = find_heavy(weights, indices)
print("Index of the heavier box:", heavier_index)
